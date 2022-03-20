import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import json
from discord import File
import time
from itertools import cycle
import random
import asyncio
from discord_slash import cog_ext
from discord_slash import SlashCommand
from discord_slash import SlashContext


class ask(commands.Cog):
    def __init__(self, bot):
        if not hasattr(bot, "slash"):
            # Creates new SlashCommand instance to bot if bot doesn't have.
            bot.slash = SlashCommand(bot, override_type=True)
        self.bot = bot
        self.bot.slash.get_cog_commands(self)

    def cog_unload(self):
        self.bot.slash.remove_cog_commands(self)

    @cog_ext.cog_slash(name="ask")
    async def ask(self, ctx: SlashContext, type, question):
        channel = ctx.channel
        ansdict = {}
        intanswer = 0
        if type == "quantity":
            ansdict = {
                1: '1',
                2: '10',
                3: '1 000 000',
                4: 'Infinity',
                5: '42',
                6: '0',
                7: '-5',
                8: '-64',
                9: '''128''',
                10: 'G64',
                11: '''More than 0''',
                12: '''Less than 0''',
                13: 'Too many',
                14: '''Not enough''',
                15: '''Exactly 69''',
                16: '''-Infinity''',
                17: '''Undefined''',
                18: '''When you will realize how stupid your questions are''',
                19: 'Wtf?',
                20: 'Who knows?',
                21: 'No comment',
                22: 'Stop asking questions',
                23: '''Of course it's you that would ask that''',
                24: 'That questions almost sounds as stupid as you',
                25: "I'm not a mathematician",
                26: 'Less than infinity',
                27: '''I don't know''',
                28: '''What are you trying to imply here?''',
                29: '''Just enough''',
            }
            intanswer = random.randint(1, 29)

        elif type == "time":
            ansdict = {
                1: 'Tomorrow',
                2: 'Today',
                3: 'Never',
                4: 'Yesterday',
                5: 'Two years before you were born',
                6: 'In 2001',
                7: 'Probably never',
                8: 'In a million years',
                9: '''It won't happen''',
                10: 'I am uncertain',
                11: '''Haha I ain't answering that one''',
                12: '''When you'll die''',
                13: 'Before the Big Bang',
                14: '''In a year''',
                15: '''Soon''',
                16: '''In a week''',
                17: '''In a month''',
                18: '''When you will realize how stupid your questions are''',
                19: 'Wtf?',
                20: 'Who knows?',
                21: 'No comment',
                22: 'Stop asking questions',
                23: '''Of course it's you that would ask that''',
                24: 'That questions almost sounds as stupid as you',
                25: 'Hopefully never',
                26: 'I hope that happens today',
                27: '''I don't know''',
                28: '''What are you trying to imply here?''',
            }
            intanswer = random.randint(1, 28)

        elif type == "y_n":
            ansdict = {
                1: 'Yes',
                2: 'No',
                3: 'Perhaps',
                4: 'Maybe',
                5: 'Absolutely',
                6: 'No, but maybe tomorrow',
                7: 'Why would you think that?',
                8: 'No way',
                9: 'Probably?',
                10: 'Probably not?',
                11: '''Haha I ain't answering that one''',
                12: 'I hope so',
                13: 'Please no',
                14: '''No, but I'll make sure it happens''',
                15: '''I don't know''',
                16: '''Why would you ask that?''',
                17: '''I don't feel like answering that''',
                18: '''It's a secret''',
                19: 'Wtf?',
                20: 'Of course',
                21: 'No comment',
                22: 'Stop asking questions',
                23: '''Of course it's you that would ask that''',
                24: 'That questions almost sounds as stupid as you',
                25: 'Most likely',
                26: 'Unlikely',
                27: '''The objective answer to that question is yes''',
                28: '''The objective answer to that question is no''',
                29: '''Wtf?''',
                30: '''What are you trying to imply here?''',
                31: '''Yep''',
                32: '''Nope''',
                33: '''Idk, but btw Python > C and that is a fact''',
                34: '''Idk, but btw C++ > C and that is a fact''',
                35: '''Idk, but btw C# > C and that is a fact''',
                36: '''Idk, but btw Java > C and that is a fact''',
                37: '''Idk, but btw lua > C and that is a fact'''
            }
            intanswer = random.randint(1, 37)

        await ctx.send(content= question + "\n" + str(ansdict[intanswer]))

def setup(client):
    client.add_cog(ask(client))