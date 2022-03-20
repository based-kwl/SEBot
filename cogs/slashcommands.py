import discord
from discord.ext import commands, tasks
from discord import File
import time
import asyncio
from itertools import cycle
from itertools import islice
import itertools
import random
from discord_slash import cog_ext
from discord_slash import SlashCommand
from discord_slash import SlashContext

class SlashCommands(commands.Cog):
    def __init__(self, bot):
        if not hasattr(bot, "slash"):
            # Creates new SlashCommand instance to bot if bot doesn't have.
            bot.slash = SlashCommand(bot, override_type=True)
        self.bot = bot
        self.bot.slash.get_cog_commands(self)

    def cog_unload(self):
        self.bot.slash.remove_cog_commands(self)

    @cog_ext.cog_slash(name="purge")
    async def purge(self, ctx: SlashContext, limit):
        server = self.bot.get_guild(148933808811409408)
        user = await server.fetch_member(ctx.author)
        role = discord.utils.get(user.guild.roles, id=390675873206108181)
        if role in user.roles:
            channel = ctx.channel
            deleted = await channel.purge(limit=limit)
            await ctx.send(content='Deleted {} message(s)'.format(len(deleted)))


    @cog_ext.cog_slash(name="clear")
    async def clear(self, ctx: SlashContext, target, limit):
        channel = ctx.channel
        server = self.bot.get_guild(148933808811409408)
        author = await server.fetch_member(ctx.author)
        user = await server.fetch_member(target)
        role = discord.utils.get(author.guild.roles, id=390675873206108181)
        deleted = 0
        if role in author.roles:
            for i in range(1, limit+1):
                check = await channel.history(limit=1000).get(author__name=user.name)
                if check is None:
                    break
                await check.delete()
                deleted += 1
            await ctx.send(content='Deleted {} message(s)'.format(str(deleted)) + " sent by " + user.name)

    @cog_ext.cog_slash(name="info")
    async def info(self, ctx: SlashContext):
        members = set(ctx.channel.guild.members)
        offline = filter(lambda m: m.status is discord.Status.offline, members)
        offline = set(offline)
        bots = filter(lambda m: m.bot, members)
        bots = set(bots)
        channel= ctx.channel
        users = members - bots
        servericon = ctx.channel.guild.icon_url

        try:
            em = discord.Embed(color=0x1e73e3, title="Server Info")
            em.set_thumbnail(url=servericon)
            em.add_field(name="Server Name", value=str(ctx.channel.guild.name))
            em.add_field(name="Server ID", value=str(ctx.channel.guild.id))
            em.add_field(name="Server Region", value=str(ctx.channel.guild.region))
            em.add_field(name="Server Verification", value=str(ctx.channel.guild.verification_level))
            em.add_field(name="Server Roles", value=str(len(ctx.channel.guild.roles) - 1))
            em.add_field(name="Server Owner", value=str(ctx.channel.guild.owner.name))
            em.add_field(name="Owner ID", value=str(ctx.channel.guild.owner.id))
            em.add_field(name="Owner Nick", value=str(ctx.channel.guild.owner.nick))
            em.add_field(name="Owner Status", value=str(ctx.channel.guild.owner.status))
            em.add_field(name="Total Bots", value=str(len(bots)))
            em.add_field(name="Bots Online", value=str(len(bots - offline)))
            em.add_field(name="Bots Offline", value=str(len(bots & offline)))
            em.add_field(name="Total Users", value=str(len(users)))
            em.add_field(name="Online Users", value=str(len(users - offline)))
            em.add_field(name="Offline Users", value=str(len(users & offline)))
            await ctx.send(content="Server info", embeds=[em])
        except discord.HTTPException:
            await ctx.send("An unknown error occured while sending the embedded message.")

    @cog_ext.cog_slash(name="ping")
    async def ping(self, ctx: SlashContext):
        await ctx.send(content=f"Pong! ({self.bot.latency*1000}ms)")

def setup(client):
    client.add_cog(SlashCommands(client))
