import discord
from discord.ext import commands, tasks
from discord import File
import time
import asyncio
from itertools import cycle
import random

class filter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 321272723634389002:
            await message.add_reaction(emoji="🇰🇷")

def setup(client):
    client.add_cog(filter(client))
