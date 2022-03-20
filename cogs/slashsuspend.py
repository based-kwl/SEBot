import os
import discord
import time
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash import SlashCommand
from discord_slash import SlashContext


class SlashSuspend(commands.Cog):
    def __init__(self, bot):
        if not hasattr(bot, "slash"):
            # Creates new SlashCommand instance to bot if bot doesn't have.
            bot.slash = SlashCommand(bot, override_type=True)
        self.bot = bot
        self.bot.slash.get_cog_commands(self)

    def cog_unload(self):
        self.bot.slash.remove_cog_commands(self)

    @cog_ext.cog_slash(name="suspend")
    async def suspend(self, ctx: SlashContext, target):
        server = self.bot.get_guild(148933808811409408)
        victim = await server.fetch_member(target)
        author = await server.fetch_member(ctx.author)
        print(author)
        staff = discord.utils.get(author.guild.roles, name="Staff-Moderator")
        banished = discord.utils.get(author.guild.roles, name="Banished")
        steam = discord.utils.get(author.guild.roles, name="STEAM")
        offtopic = discord.utils.get(author.guild.roles, name="OffTopic")
        if staff in author.roles:
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
                await ctx.send(content="Suspended " + victim.name)

def setup(client):
    client.add_cog(SlashSuspend(client))
