import discord
from discord.ext import commands, tasks
from discord import File
import time
from itertools import cycle
import random


class Discordbot(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        poop = ['Lukas Quintus Gladius#0989', 'crapkas the bringer of pant yeet']
        if str(message.author) in poop:
            await message.delete()

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        poop = ['Lukas Quintus Gladius#0989', 'crapkas the bringer of pant yeet']
        if user in poop:
            await reaction.remove(user)




def setup(client):
    client.add_cog(Discordbot(client))
