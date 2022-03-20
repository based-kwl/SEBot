import discord
from discord.ext import commands, tasks
from discord import File
import time
import asyncio
from itertools import cycle
import random

class archivebeta(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel
        channel1 = "beta"
        channel1get = self.client.get_channel(595469776298442755)
        if str(channel) == 'rules':
            if reaction.emoji == '👌':
                verified = discord.utils.get(user.guild.roles, name="Verified")
                bot = discord.utils.get(user.guild.roles, name="Bots")
                unverified = discord.utils.get(user.guild.roles, name="Unverified")
                if bot in user.roles:
                    return
                if verified in user.roles:
                    await reaction.remove(user)
                    return
                await user.add_roles(verified)
                await channel.send('Verified ' + str(user))
                await asyncio.sleep(3)
                await reaction.remove(user)
                await user.remove_roles(unverified)

    @commands.command()
    async def rules(self, ctx):
        message = ctx.message
        channel = message.channel
        valid_users = ['Phunnie#0990']

        em1 = discord.Embed(
            title='1. Go to your Steam library and locate SpaceEngine.',
            color=0x1e73e3
        )
        em1.set_image(url='https://cdn.discordapp.com/attachments/594235690733273088/594741323349884938/unknown.png')

        em2 = discord.Embed(
            title='2. Right click on SpaceEngine and click "Properties".',
            color=0x1e73e3
        )
        em2.set_image(url='https://cdn.discordapp.com/attachments/594235690733273088/594741491256262656/unknown.png')

        em3 = discord.Embed(
            title='3. Go to the "BETAS" tab and select "beta - public beta branch" in the drop-down menu.',
            color=0x1e73e3
        )
        em3.set_image(url='https://cdn.discordapp.com/attachments/594235690733273088/594741772190744586/unknown.png')
        em3.set_footer(text='Then close the window and let SpaceEngine update.')

        valid_users = ['Phunnie#0990', 'SEBot#2221', 'SpaceEngine Bot#2221']
        if str(message.author) in valid_users:
            if message.content.startswith('.rules'):
                await channel.purge(limit=8)
                await channel.send('**1. Keep your conversations in the right channel. So no memes outside of #memes**\n``` ```')
                await channel.send('**2. Stay polite and civil. If there is a disagreement, respect each other\'s opinions.**\n``` ```')
                await channel.send('**3. No spam. At all.**\n``` ```')
                await channel.send('**4. No chat in #event-submissions  or #astrophotography-gallery**\n``` ```')
                await channel.send('**5. No NSFW content is allowed, keep it at pg-13. **\n``` ```')
                await channel.send('**If you break these rules, you will first get a warning, and possibly be muted. If you continue, you will be kicked, if you continue further you will be banned.**\n``` ```')
                await channel.send('''**React with :ok_hand: to get verified**\n\n *If the reaction is not working (the role isn't being given), ping @Phunnie#0990.*''')
            if message.content.startswith('**React with'):
                await message.add_reaction(emoji='👌')
            if message.content.startswith('.rules'):
                await message.delete()
            if message.content.startswith('Verified'):
                await asyncio.sleep(3)
                await message.delete()

def setup(client):
    client.add_cog(archivebeta(client))





