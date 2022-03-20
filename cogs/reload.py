import discord
from discord.ext import commands, tasks
from discord import File
import time
import asyncio
from itertools import cycle
from itertools import islice
import itertools
import random


class reload(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        valid_users = ['Phunnie#0990']
        if str(ctx.message.channel) and str(ctx.message.author) in valid_users:
            try:
                self.client.load_extension(f'cogs.{extension}')
                msg2 = await ctx.channel.send(str(extension) + ' loaded')
                await asyncio.sleep(3)
                await msg2.delete()
            except:
                msg2 = await ctx.channel.send('Extension does not exist or is already loaded.')
                await asyncio.sleep(3)
                await msg2.delete()

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        valid_users = ['Phunnie#0990']
        if str(ctx.message.channel) and str(ctx.message.author) in valid_users:
            try:
                self.client.unload_extension(f'cogs.{extension}')
                msg2 = await ctx.channel.send(str(extension) + ' unloaded')
                await asyncio.sleep(3)
                await msg2.delete()
            except:
                msg2 = await ctx.channel.send('Extension does not exist or is already unloaded.')
                await asyncio.sleep(3)
                await msg2.delete()

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        valid_users = ['Phunnie#0990']
        if str(ctx.message.channel) and str(ctx.message.author) in valid_users:
            try:
                self.client.unload_extension(f'cogs.{extension}')
            except:
                msg1 = await ctx.channel.send('Extension does not exist or is already unloaded.')
                await msg1.delete()
            try:
                self.client.load_extension(f'cogs.{extension}')
                msg2 = await ctx.channel.send(str(extension) + ' reloaded')
                await asyncio.sleep(3)
                await msg2.delete()
            except:
                msg3 = await ctx.channel.send('Extension does not exist or is already loaded.')
                await asyncio.sleep(3)
                await msg3.delete()


def setup(client):
    client.add_cog(reload(client))
