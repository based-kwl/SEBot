import discord
from discord.ext import commands, tasks
from discord import File
import time
import asyncio
from itertools import cycle
from itertools import islice
import itertools
import random


class autochat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        scr = 'screenshots-and-findings'
        se = 'spaceengine'
        if str(channel) in scr:
            if message.content.contains('nebula'):
                    async with channel.typing():
                        await asyncio.sleep(5)
                    msg1 = await channel.send('test')

def setup(client):
    client.add_cog(autochat(client))
