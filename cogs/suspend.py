import os
import discord
import time
from discord.ext import commands


class loading(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def suspend(self, ctx, *, target):
        victim = ctx.message.mentions[0]
        author = ctx.message.author
        staff = discord.utils.get(author.guild.roles, name="Staff")
        banished = discord.utils.get(author.guild.roles, name="Banished")
        steam = discord.utils.get(author.guild.roles, name="STEAM")
        offtopic = discord.utils.get(author.guild.roles, name="OffTopic")
        if staff in ctx.message.author.roles:
            if banished in victim.roles:
                await victim.remove_roles(banished)
            else:
                try:
                    await victim.remove_roles(steam)
                    await victim.remove_roles(offtopic)
                except:
                    try:
                        await victim.remove_roles(offtopic)
                    except:
                        print("Yeet")
                await victim.add_roles(banished)


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        author = reaction.message.author
        staff = discord.utils.get(author.guild.roles, id=390675873206108181)
        banished = discord.utils.get(author.guild.roles, name="Banished")
        steam = discord.utils.get(author.guild.roles, name="STEAM")
        offtopic = discord.utils.get(author.guild.roles, name="OffTopic")
        if staff in user.roles and reaction.emoji == '🔨':
            if banished in user.roles:
                await author.remove_roles(banished)
            else:
                try:
                    await author.remove_roles(steam)
                    await author.remove_roles(offtopic)
                except:
                    try:
                        await author.remove_roles(offtopic)
                    except:
                        print("Yeet")
                await author.add_roles(banished)




def setup(client):
    client.add_cog(loading(client))
