import os
import discord
import time
from discord.ext import commands


class loading(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        valid_users = ['Phunnie#0990', 'SpaceEngine Bot#2221']
        channel = message.channel
        content = message.content
        author = message.author
        yeet = discord.utils.get(author.guild.roles, name="yeet")
        if str(message.author) in valid_users:
            if 'yeet' in content:
                victim = message.mentions[0]
                await victim.add_roles(yeet)

            if 'yote' in content:
                victim = message.mentions[0]
                await victim.remove_roles(yeet)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        valid_users = ['Phunnie#0990', 'SpaceEngine Bot#2221']
        author = reaction.message.author
        yeet = discord.utils.get(author.guild.roles, name="yeet")
        if str(user) in valid_users:
            if reaction.emoji == '🔨':
                await author.add_roles(yeet)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        valid_users = ['Phunnie#0990', 'SpaceEngine Bot#2221']
        author = reaction.message.author
        yeet = discord.utils.get(author.guild.roles, name="yeet")
        if str(user) in valid_users:
            if reaction.emoji == '🔨':
                await author.remove_roles(yeet)




def setup(client):
    client.add_cog(loading(client))
