import discord
from discord.ext import commands, tasks
from discord import File
import time
import asyncio
from itertools import cycle
import random

class Discordbot(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        channel1name = "spaceengine-suggestions"
        channel1 = self.client.get_channel(589513723010351144)
        channel2name = 'suggestions'
        author = message.author
        channel2 = self.client.get_channel(596840023752704000)
        if '@everyone' in message.content:
            return
        if str(message.channel.id) == str(589513723010351144):
            if message.content.startswith('`Dev Response`'):
                return
            if message.content.startswith('.c'):
                return
            else:
                for attachment in message.attachments:
                    filename = attachment.filename
                    await attachment.save('/home/SE/{}'.format(filename))
                    await channel2.send(message.content + "\n", file=File('/home/SE/' + str(filename)))
                    return
                await channel2.send(message.content)
        if str(message.channel.id) == str(596840023752704000):
            if message.author.bot:
                return
            if message.content.startswith('.c'):
                return
            else:
                if message.content.startswith('.p'):
                    return
                else:
                    for attachment in message.attachments:
                        filename = attachment.filename
                        await attachment.save('/home/SE/{}'.format(filename))
                        await channel1.send("`Dev Response`\n*From " + str(author) + "*\n" + message.content, file=File('/home/SE/' + str(filename)))
                        return
                    await channel1.send("`Dev Response`\n*From " + str(author) + "*\n" + message.content)


def setup(client):
    client.add_cog(Discordbot(client))
