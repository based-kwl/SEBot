import discord
from discord.ext import commands, tasks
from discord import File
import requests
import json
import time
import asyncio
from itertools import cycle
from itertools import islice
import itertools
import random
import datetime
import subprocess

class ben(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def vote(self, ctx, *, arg: str = None):
        channel = ctx.channel
        message = ctx.message
        user = ctx.message.author
        role = discord.utils.get(user.guild.roles, name="Staff")
        oui = self.client.get_emoji(427589893904924682)
        non = self.client.get_emoji(427589893196087326)
        if role in user.roles:
            try:
                message_id = int(arg)
                vote = await channel.history().get(id=message_id)
                await vote.add_reaction(emoji=oui)
                await vote.add_reaction(emoji=non)
                await message.delete()
            except:
                await message.add_reaction(emoji=oui)
                await message.add_reaction(emoji=non)


def setup(client):
    client.add_cog(ben(client))