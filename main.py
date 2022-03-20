import discord
from discord.ext.commands import Bot
from discord.ext import commands, tasks
import os
from os import listdir
from os.path import isfile, join
import asyncio
import sys, traceback
from itertools import cycle
import asyncio
from discord_slash import SlashCommand
from discord_slash import SlashCommandOptionType
from discord_slash.utils import manage_commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.default())
slash = SlashCommand(bot, auto_register=False)
bot.remove_command("help")
token = 'NTk0MjM1OTg3NDM4MDc1OTE1.XRbEmQ.SJd9xt0XbRFT_tVPb-XJucu5FSI'

f=open("secogs.txt","r")
cogslist = f.readlines()
f.close()
print(cogslist)
for cog in cogslist:
    cog = cog.replace("\n","")
    bot.load_extension(f'cogs.' + str(cog))
    print('Loaded ' + str(cog))


bot.run(token)