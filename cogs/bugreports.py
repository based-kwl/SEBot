import discord
from discord.ext import commands, tasks
from discord import File
import time
import asyncio
from itertools import cycle
import random
import os

class Discordbot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Started')
        await self.client.change_presence(activity=discord.Game(name='.help for commands'))

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channelid = payload.channel_id
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        server = self.client.get_guild(148933808811409408)
        user = server.get_member(payload.user_id)
        emoji = '👌'
        if str(channelid) == str(594393482228137988):
            if str(payload.emoji) == emoji:
                beta = discord.utils.get(server.roles, name="Beta Tester")
                bot = discord.utils.get(server.roles, name="SEBot")
                if bot in user.roles:
                    return
                if beta in user.roles:
                    await user.remove_roles(beta)
                    await channel.send('Removed ' + str(user) + " from Beta Testers.")
                    await asyncio.sleep(3)
                    await message.remove_reaction(emoji, user)
                    return
                await user.add_roles(beta)
                await channel.send('Added ' + str(user) + " to Beta Testers.")
                await asyncio.sleep(3)
                await message.remove_reaction(emoji, user)

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        channel4 = "bots-and-voice"
        channel4get = self.client.get_channel(217142893440270346)
        channel = message.channel
        valid_users = ['Phunnie#0990']
        if str(message.channel) and str(message.author) in valid_users:
            if message.content.startswith('.no'):
                await channel.send('No.')
            if message.content.startswith('.ping'):
                before = time.monotonic()
                message = await channel.send("Pong!")
                ping = (time.monotonic() - before) * 1000
                await message.edit(content=f"Pong!  `{int(ping)}ms`")
                print(f'Ping {int(ping)}ms')

        em1 = discord.Embed(
            title='1. Go to your Steam library and locate SpaceEngine.',
            color=0x1e73e3
        )
        em1.set_image(url='https://cdn.discordapp.com/attachments/606295484000370702/606296542110023705/2019-06-30_00-06-28.png')

        em2 = discord.Embed(
            title='2. Right click on SpaceEngine and click "Properties".',
            color=0x1e73e3
        )
        em2.set_image(url='https://cdn.discordapp.com/attachments/606295484000370702/606296538913701888/2019-06-30_00-10-17.png')

        em3 = discord.Embed(
            title='3. Go to the "BETAS" tab and select "beta - public beta branch" in the drop-down menu.',
            color=0x1e73e3
        )
        em3.set_image(url='https://cdn.discordapp.com/attachments/606295484000370702/606296936127135744/Steam_2019-06-30_00-11-18.png')
        em3.set_footer(text='Then close the window and let SpaceEngine update.')

        valid_users = ['Phunnie#0990', 'SEBot#2221', 'SpaceEngine Bot#2221']
        if str(message.channel) and str(message.author) in valid_users:
            if message.content.startswith('.kill'):
                exit()
            channel3get = self.client.get_channel(594393482228137988)
            channel3 = 'beta-testing'
            if str(message.channel) == 'beta-test':
                if message.content.startswith('.beta'):
                    await channel.purge(limit=6)
                    await channel3get.send('**To opt into the public beta, follow these instructions:**\n')
                    await channel3get.send(embed=em1)
                    await channel3get.send(embed=em2)
                    await channel3get.send(embed=em3)
                    await channel3get.send('''**Once you have installed the public beta and are ready to test, click the :ok_hand: reaction below.** \n\n**Warning**: The public beta might not always be stable. Make backups regularly.\n*If you wish to leave the beta, simply react again.*\n\n If the reaction is not working (the role isn't being given), ping <@180472764552052736>.''')
                if message.content.startswith('**Once you have'):
                    await message.add_reaction(emoji='👌')
                if message.content.startswith('.beta'):
                    await message.delete()
                if message.content.startswith('Removed'):
                    await asyncio.sleep(3)
                    await message.delete()
                if message.content.startswith('Added'):
                    await asyncio.sleep(3)
                    await message.delete()

        channel = message.channel
        channel4 = "bots-and-voice"
        channel4get = self.client.get_channel(217142893440270346)
        channel1 = "report-bugs"
        channel1get = self.client.get_channel(588014726726942730)
        channel2 = "bug-reports"
        channel2get = self.client.get_channel(528682486168027182)
        #channeltest = "general2"
        #channeltestget = client.get_channel(430054839607885850)
        author = message.author
        author_id = author.id

        if message.content.startswith('.c'):
            return
        if '@everyone' in message.content:
            return
        if message.author.bot:
            return
        if str(message.channel.id) == str(588014726726942730):
            for attachment in message.attachments:
                name = attachment.filename
                filename, file_extension = os.path.splitext('/home/SE/{}'.format(name))
                await attachment.save('/home/SE/attachment{}'.format(file_extension))
                await channel2get.send("*From " + str(author) + "*\n```<@" + str(author_id) + ">```\n" + message.content + "\n", file=File('/home/SE/attachment{}'.format(file_extension)))
                return
            await channel2get.send("*From " + str(author) + "*\n```<@" + str(author_id) + ">```\n" + message.content + "\n")
        if str(message.channel.id) == str(528682486168027182):
            if message.content.startswith('.p'):
                return
            else:
                for attachment in message.attachments:
                    name = attachment.filename
                    filename, file_extension = os.path.splitext('/home/SE/{}'.format(name))
                    await attachment.save('/home/SE/attachment{}'.format(file_extension))
                    await channel1get.send("`Dev Response`\n*From " + str(author) + "*\n" + message.content + "\n", file=File('/home/SE/attachment{}'.format(file_extension)))
                    return
                await channel1get.send("`Dev Response`\n*From " + str(author) + "*\n" + message.content + "\n")


def setup(client):
    client.add_cog(Discordbot(client))





