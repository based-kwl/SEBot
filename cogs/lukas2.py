import discord
from discord.ext import commands, tasks
from discord import File
import time
from itertools import cycle
import random


class lukas2(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        poop = ['Lukas Quintus Gladius#0989', 'crapkas the bringer of pant yeet']
        if str(message.author) in poop:
            await message.add_reaction(emoji='🇧')
            await message.add_reaction(emoji='🇦')
            await message.add_reaction(emoji='🇩')



def setup(client):
    client.add_cog(lukas2(client))
