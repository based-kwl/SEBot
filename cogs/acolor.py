import discord
from discord.ext import commands, tasks
from discord import File
import time
import asyncio
from itertools import cycle
from itertools import islice
import itertools
import random


class color(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def acolor(self, ctx, arg1, *, arg2: str = None):
        user = ctx.message.author
        channel = ctx.message.channel
        server = ctx.message.guild
        e = ['Phunnie#0990']
        if str(user) in e:
            if arg1 == 'clear':
                rc = discord.utils.get(user.guild.roles, name=str(arg2))
                await rc.delete()
                emc = discord.Embed(
                    title='Color Removed.',
                    color=0x000000
                )
                await channel.send(embed=emc)
                return

            rc = discord.utils.get(user.guild.roles, name=str(arg2))
            try:
                if '0x' in arg1:
                    hex_str = arg1[2:]
                elif '#' in arg1:
                    hex_str = arg1[1:]
                elif '[' in arg1:
                    hex_str = arg1[1:-1]
                else:
                    hex_str = arg1
                hex_int = int(hex_str, 16)

                await rc.edit(color=discord.Color(int(hex_int)))
                emc = discord.Embed(
                    title='Color Changed.',
                    color=hex_int
                )
                await channel.send(embed=emc)
                return

            except:
                arg2t = arg2[2:-1].replace('!', '')
                author = str(self.client.get_user(int(arg2t)))
                if '0x' in arg1:
                    hex_str = arg1[2:]
                elif '#' in arg1:
                    hex_str = arg1[1:]
                elif '[' in arg1:
                    hex_str = arg1[1:-1]
                else:
                    hex_str = arg1
                hex_int = int(hex_str, 16)
                await server.create_role(name=str(author[:-5]), color=discord.Color(int(hex_int)))
                await asyncio.sleep(0.5)
                rc = discord.utils.get(user.guild.roles, name=str(author[:-5]))
                await asyncio.sleep(0.5)
                await rc.edit(position=24)
                await asyncio.sleep(0.5)
                await ctx.message.mentions[0].add_roles(rc)
                emc = discord.Embed(
                    title='Color Changed.',
                    color=hex_int
                )
                await channel.send(embed=emc)
                return



def setup(client):
    client.add_cog(color(client))
