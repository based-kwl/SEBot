import discord
from discord.ext import commands, tasks
from discord import File
import asyncio
from itertools import cycle
import random
import os

class suggest(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel
        message = reaction.message
        content = reaction.message.content
        channelgood = 'suggestions-approval'
        bot = discord.utils.get(user.guild.roles, name="SEBot")
        channel1 = self.client.get_channel(589513723010351144)
        if str(channel) in channelgood:
            if reaction.message.content.startswith('**Rejected'):
                return
            if reaction.message.content.startswith('**Approved'):
                return
            if bot in user.roles:
                return
            if reaction.emoji == '✅':
                for attachment in reaction.message.attachments:
                    name = attachment.filename
                    filename, file_extension = os.path.splitext('/home/SE/{}'.format(name))
                    await attachment.save('/home/SE/attachment{}'.format(file_extension))
                    await channel1.send(str(content) + '*', file=File('/home/SE/attachment{}'.format(file_extension)))
                    await reaction.message.edit(content='**Approved by **' + str(user) + '\n' + str(reaction.message.content))
                    return
                await channel1.send(reaction.message.content)
                await reaction.message.edit(content='**Approved by **' + str(user) + '\n' + str(reaction.message.content))

            if reaction.emoji == '❌':
                msg = await channel.send('**Please provide a reason:**')

                def check(message):
                    print(message.channel.id)
                    return message.channel.id == 595671069004922880 and not message.author.bot

                try:
                    ans = await self.client.wait_for('message', check=check, timeout=300)
                    lines = content.split('\n')
                    author_id = int(lines[-1])
                    author = self.client.get_user(author_id)
                    em = discord.Embed(
                        title='Your suggestion has been rejected for the following reason(s):',
                        description=str(ans.content),
                        color=0x1e73e3
                    )
                    await author.send(embed=em)
                    await msg.edit(content='**Reason sent to user:\n**' + ans.content)
                    await reaction.message.edit(content='**Rejected by **' + str(user) + '\n' + str(reaction.message.content))
                    return
                except:
                    await msg.edit(content='Timed out after 5 minutes. Please try again.')
                    await message.remove_reaction(emoji='❌', member=user)
                    return


    @commands.command()
    async def suggest(self, ctx, *, arg):
        msg = ctx.message
        content = ctx.message.content
        user = ctx.message.author
        channel = ctx.channel
        channel1 = self.client.get_channel(595671069004922880)

        if len(msg.content) > 1900:
            em = discord.Embed(
                title='Suggestion not sent.',
                color=0x1e73e3
            )
            em.add_field(name='Message Length', value='**Your suggestion must be less than 1900 characters long.**\n Your current suggestion is ' + str(len(msg.content)) + ' characters long.')

            error_message = await channel.send(embed=em)
            await asyncio.sleep(30)
            await error_message.delete()
            return

        suggestion = any(s in content for s in ['Suggestion', '*Suggestion', '**Suggestion', '***Suggestion',])
        explanation = any(s in content for s in ['Explanation', '*Explanation', '**Explanation', '***Explanation',])
        reason = any(s in content for s in ['Reason', '*Reason', '**Reason', '***Reason',])
        type_code = any(s in content for s in ['Type', '*Type', '**Type', '***Type',])
        tag = any(s in content for s in ['Feature', 'QOL', 'VR', 'Utility', 'Other',])

        if suggestion and explanation and reason and type_code and tag:
            for attachment in ctx.message.attachments:
                name = attachment.filename
                filename, file_extension = os.path.splitext('/home/SE/{}'.format(name))
                await attachment.save('/home/SE/attachment{}'.format(file_extension))
                msg3 = await channel1.send('``` ```' + str(content[8:]) + "\n\n*Suggestion by: " + str(user) + '*\n' + str(ctx.message.author.id), file=File('/home/SE/attachment{}'.format(file_extension)))
                await msg3.add_reaction('✅')
                await msg3.add_reaction('❌')
                return
            msg2 = await channel1.send('``` ```' + str(content[8:]) + "\n\n*Suggestion by: " + str(user) + '*\n' + str(ctx.message.author.id))
            await msg2.add_reaction('✅')
            await msg2.add_reaction('❌')
            await channel.send('Suggestion sent.')
        else:
            em = discord.Embed(
                title='Suggestion rejected for the following reason(s):',
                color=0x1e73e3
            )
            messages = []
            if not suggestion:
                em.add_field(name='Missing "Suggestion"', value='**Your suggestion must have "Suggestion: [suggestion name]"**')
            if not explanation:
                em.add_field(name='Missing "Explanation"', value='**Your suggestion must have "Explanation: [explanation]"**')
            if not reason:
                em.add_field(name='Missing "Reason"', value='**Your suggestion must have "Reason: [reason]"**')
            if not type_code:
                em.add_field(name='Missing "Type"', value='**Your suggestion must have "Type: [Tag]"**')
            if not tag:
                em.add_field(name='Missing a Tag', value='**Your suggestion must have a valid tag (case sensitive and no markdown): "Feature, QOL, VR, Utility, Other"**\n')

            error_message = await channel.send(embed=em)
            await asyncio.sleep(30)
            await error_message.delete()


def setup(client):
    client.add_cog(suggest(client))
