import os
import discord
import time
from discord.ext import commands


class yote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        author = message.author
        yeet = discord.utils.get(author.guild.roles, name="yeet")
        if yeet in author.roles:
            await message.delete()



def setup(client):
    client.add_cog(yote(client))
