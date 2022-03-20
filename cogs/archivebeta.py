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
        if str(reaction.message.channel.id) == "595469776298442755":
            if reaction.emoji == '👌':
                beta = discord.utils.get(user.guild.roles, name="Public Beta Tester")
                bot = discord.utils.get(user.guild.roles, name="Bot")
                if bot in user.roles:
                    return
                if beta in user.roles:
                    await user.remove_roles(beta)
                    await channel1get.send('Removed ' + str(user) + " from Public Beta Testers.")
                    await asyncio.sleep(3)
                    await reaction.remove(user)
                    return
                await user.add_roles(beta)
                await channel1get.send('Added ' + str(user) + " to Public Beta Testers.")
                await asyncio.sleep(3)
                await reaction.remove(user)

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        channel4 = "bots-and-voice"
        channel4get = self.client.get_channel(217142893440270346)
        channel = message.channel
        valid_users = ['Phunnie#0990']

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
            channel3get = self.client.get_channel(595469776298442755)
            channel3 = 'beta'
            if str(message.channel.id) == "595469776298442755":
                if message.content.startswith('.beta'):
                    await channel.purge(limit=6)
                    await channel3get.send('**To opt into the public beta, follow these instructions:**\n')
                    await channel3get.send(embed=em1)
                    await channel3get.send(embed=em2)
                    await channel3get.send(embed=em3)
                    await channel3get.send('''**Once you have installed the public beta and are ready to test, click the :ok_hand: reaction below.** \n\n**Warning**: The public beta might not always be stable. Make backups regularly.\n*If you wish to leave the beta, simply react again.*\n\n If the reaction is not working (the role isn't being given), ping @Phunnie#0990.''')
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

def setup(client):
    client.add_cog(archivebeta(client))





