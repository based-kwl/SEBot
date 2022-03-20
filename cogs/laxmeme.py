import discord
from discord.ext import commands, tasks
import random


class Discordbot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        bot = self.client.get_channel(217142893440270346)
        poop = ['Lax Jaguar#7600']
        if str(message.author) in poop:
            if random.randint(1, 1000) == 42:
                await message.send(message.author.mention + ' contest')

def setup(client):
    client.add_cog(Discordbot(client))
