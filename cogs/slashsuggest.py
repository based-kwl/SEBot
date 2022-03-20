import discord
from discord.ext import commands, tasks
from discord import File
import asyncio
from itertools import cycle
import random
import os
from discord_slash import cog_ext
from discord_slash import SlashCommand
from discord_slash import SlashContext

class suggest(commands.Cog):
    def __init__(self, bot):
        if not hasattr(bot, "slash"):
            # Creates new SlashCommand instance to bot if bot doesn't have.
            bot.slash = SlashCommand(bot, override_type=True)
        self.bot = bot
        self.bot.slash.get_cog_commands(self)

    def cog_unload(self):
        self.bot.slash.remove_cog_commands(self)

    @cog_ext.cog_slash(name="suggest")
    async def suggest(self, ctx: SlashContext, name, explanation, reason, type):
        print("e")
        server = self.bot.get_guild(148933808811409408)
        user = await server.fetch_member(ctx.author)
        channel = ctx.channel
        channel1 = self.bot.get_channel(595671069004922880)
        content = "Suggestion: " + name + "\nExplanation: " + explanation + "\nReason: " + reason + "\nType: " + type
        msg2 = await channel1.send(str(content) + "\n\n*Suggestion by: " + user.name + '*\n' + str(ctx.author))
        await ctx.send(content='Suggestion sent.')
        await channel1.send("``` ```")
        await msg2.add_reaction('✅')
        await msg2.add_reaction('❌')

def setup(client):
    client.add_cog(suggest(client))
