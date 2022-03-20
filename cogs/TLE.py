import discord
from discord.ext import commands, tasks
from discord import File
import time
import asyncio
from itertools import cycle
from itertools import islice
import itertools
import random


class TLE(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def then(self, ctx, *, arg):
        fp = open('/home/SE/Full_Catalog-20190704T1600.3le', 'r')
        channel = ctx.message.channel
        msg = ctx.message
        lineNums = []
        lineNum = 0
        lines = []
        for line in fp:
            lineNum = lineNum + 1
            lines.append(line);
            if arg.upper() in line:
                lineNums.append(lineNum)

        for i in lineNums:
            await channel.send(lines[i] + "\n" + lines[i + 1] + "\n" + lines[i + 2])

        await asyncio.sleep(0.5)
        await msg.delete()


def setup(client):
    client.add_cog(TLE(client))