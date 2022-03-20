import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import json
from discord import File
import time
from itertools import cycle
import random
import asyncio


class ask(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ask(self, ctx, *, args):
        await ctx.channel.send("I don't know, but maybe my creator Lax Jaguar#7600 the troglodyte knows.")


def setup(client):
    client.add_cog(ask(client))