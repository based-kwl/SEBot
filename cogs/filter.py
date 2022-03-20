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
        users = ['Lukas Quintus Gladius#1948']
        content = message.content
        filter = any(s in content for s in ['cringe', 'cronge', 'Cringe', 'Cronge', 'Crange', 'Croge', 'Crunge', 'crunge', 'cring', 'crange', 'c r i', 'n g e', ' c r'])
        if filter:
            if str(message.author) in users:
                await message.delete()

def setup(client):
    client.add_cog(filter(client))
