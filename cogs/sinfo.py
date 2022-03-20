import discord
from discord.ext import commands, tasks
from discord import File
import requests
import json
import time
import asyncio
from itertools import cycle
from itertools import islice
import itertools
import random
import datetime
import subprocess
from discord import Webhook, AsyncWebhookAdapter
import aiohttp


class sinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def sinfo(self, ctx, *, arg: str = None):
        channel = ctx.channel
        channelinfo = self.client.get_channel(343784038169051146)
        user = ctx.message.author
        em0 = discord.Embed(
            color=0x1e73e3
        )
        em0.set_image(url='https://cdn.discordapp.com/attachments/348935513845137408/577970875266105344/SpaceEngine_Modern_logo.png')
        p0 = '**Welcome to the official Space Engine Discord Server!**\nBe friendly and feel free to share your experiences with others.\n\n'
        p1 = '''> **SPACEENGINE CHANNELS**\n<#363775829681111042>: Serious discussions about anything and everything, excluding shitposts and memes.\n<#412022496372457472>: Discussions about screenshot contests.\n<#148934978095415296>: Screenshots and findings in Space Engine. Discussions about those screenshots are allowed.\n<#419636411361132555>: Space Engine videos.\n<#148935097041682432>: Troubleshooting channel.\n<#467052910359085066>: Share your SE addons here. Discussion of those addons should stay in #spaceengine.\n<#588014726726942730> \n<#589513723010351144>: Instructions on how to submit a suggestion are in the channel description\n<#594362001044799488>: For instructions on how to enter the public beta and gain access to this channel read #beta-test\n\n'''
        p2 = '''> **STEM CHANNELS**\n<#356978443675762688>: Discussions about science and math related topics.\n<#399446196512358401>: Discussions about space.\n<#405081658308558848>: Discussions about technology and coding.\n<#467509087685443604>: Discuss weather.\n<#446814919904460810>: A channel where you can share photos, specifically of the sky and celestial objects, and discussion of equipment and processing techniques.\n<#414680778430218240>: Discussions and pictures about your travel experiences.\n<#532299787198791720>: Paranormal.\n\n'''
        p3 = '''> **GENERAL-OFFTOPIC-CHANNELS**\n*For anything not related to SpaceEngine.*\n<#515597308902113280>: Generally offtopic discussions.\n<#515597377017479181>: Pictures, videos, music, etc.\n<#365665769800859649>: Share things you've created such as pictures, art, etc. here.\n<#527260011211128852>: For discussions about movies, books, TV shows and the likes.\n<#515597387029413898>: Video games.\n<#217142893440270346>: Bot commands and text for voice chat.\n\n> **VOICE CHANNELS**\n'''
        p4 = '''🔊 General To discuss anything SpaceEngine related (or unrelated!) with other members.\n🔊 General [64kbps] For people with poorer internet connections\n🔊 Music For use with @Vexera +help - Music/Fun , check <#217142893440270346>'s pins for a list of commands.\n🔊 Idle - AFK voice chat users will be placed here after 30 minutes.\n\n'''
        p5 = '''> **ROLES**\n**<@&343494473373974529>** - Self-explanatory\n**<@&588538639533735957>** - Ping this role if you need help with anything SpaceEngine related\n**<@&390675873206108181>** - Feel free to ping any of us if there are any problems on the discord.\n**<@&348863894128951297>** - Additional helping hands.\n**<@&588794853232607242>** - Trial moderators\n\n'''
        p6 = '''> *Honors*\n**Screenshot Contest** (**<@&428334989382385664>**/**<@&416040106214948877>**/**<@&413071228379594753>**/**<@&358223135083986944>**/**<@&413064624863313931>**/**<@&366636608268664833>**) - <#355439997337206784>\n**<@&359127230980292609>** - Users who have helped translate SpaceEngine\n**<@&585605306734870538>** - People who had 0.990 during its private beta testing stage\n**<@&353260908174376960>** - Verified Youtuber or streamer\n**<@&590541677287178240>** - Owners of the PRO DLC on Steam\n**<@&344844953463291909>** - Users with experience with modding and/or creating addons\n**<@&352863798161309706>** - People who have shown themselves to be very knowledgeable in a field of science.\n**<@&600811378562957314>** - People who spend time photographing the night sky.\n**<@&585606666431496233>** - Nitro users who have boosted our server. Acess to .color command.\n\n'''
        p7 = '''> *Base roles*\n <@&371046859692572682> - People that are active and don't break rules. i.e. Role models, people that don't shitpost, always stay on topic, bring interesting ideas, etc.\n• Pioneer permissions + a few other things.\n'''
        p8 = '''<@&371046337506050081> - Active Users\n• Can change nickname + Explorer permissions.\n<@&371046950679740426> - Users that have sent a reasonable amount of messages in chat.\n• Can view Audit Log, use external emoji, attach files, and embed images anywhere\n<@&391637024693813249> - Users that have read and agreed to <#402607834639892480>.\n• Permission to participate in chat.\n\n'''
        em4 = discord.Embed(
            title='**USEFUL LINKS**',
            color=0x1e73e3
        )
        em4.add_field(name='Website', value='[Official SpaceEngine Website](<http://spaceengine.org/>)', inline=False)
        em4.add_field(name='Purchase SpaceEngine', value='[STEAM](https://store.steampowered.com/app/314650/SpaceEngine/)', inline=False)
        em4.add_field(name='Archives', value='[Download older versions](<http://forum.spaceengine.org/viewtopic.php?t=182>)', inline=False)
        em4.add_field(name='Reddit', value='[r/spaceengine](<https://www.reddit.com/r/spaceengine>)', inline=False)
        em3 = discord.Embed(
            title='**DISCORD LINKS**',
            color=0x1e73e3
        )
        em3.add_field(name='SpaceEngine Official (this)', value='https://discord.gg/spaceengine', inline=False)
        em3.add_field(name='SpaceEngine Italian', value='https://discord.gg/t5BJpfv', inline=False)
        em3.add_field(name='SpaceEngine French', value='https://discord.gg/ctMXRYx', inline=False)
        em3.add_field(name='SpaceEngine Russian', value='https://discord.gg/aEJ42Ej', inline=False)
        em3.add_field(name='SpaceEngine Addons', value='https://discord.gg/RpaDp5q', inline=False)
        role = discord.utils.get(user.guild.roles, name="Staff")
        await channelinfo.purge(limit=7)
        print(len(p4 + p5 + p6 + p7))
        if role in user.roles:
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url('https://discordapp.com/api/webhooks/607619873605943296/jVyWpovoO4Yv2cQYpIKrYByV421N-nVWbe2PPAgkOucSKulAH4PWT3S63zJPG5S3MwGa', adapter=AsyncWebhookAdapter(session))
                await webhook.send(embed=em0, username='SpaceEngine Bot', avatar_url='https://cdn.discordapp.com/attachments/358372741952438273/583423507912982569/SELogo-BlackContour.png')
                await asyncio.sleep(0.2)
                await webhook.send(content=str(p0) + str(p1) + str(p2) + str(p3), username='SpaceEngine Bot', avatar_url='https://cdn.discordapp.com/attachments/358372741952438273/583423507912982569/SELogo-BlackContour.png')
                await webhook.send(content=str(p4) + str(p5) + str(p6) + str(p7), username='SpaceEngine Bot',
                                   avatar_url='https://cdn.discordapp.com/attachments/358372741952438273/583423507912982569/SELogo-BlackContour.png')
                await webhook.send(content=str(p8), username='SpaceEngine Bot',
                                   avatar_url='https://cdn.discordapp.com/attachments/358372741952438273/583423507912982569/SELogo-BlackContour.png')
                await asyncio.sleep(0.2)
                await webhook.send(embeds=[em4, em3], username='SpaceEngine Bot', avatar_url='https://cdn.discordapp.com/attachments/358372741952438273/583423507912982569/SELogo-BlackContour.png')
                await webhook.send(content='Have fun and please visit the official SpaceEngine forums and subreddit! **If you have any problems in this Discord server please ping or DM a moderator!**', username='SpaceEngine Bot',
                                   avatar_url='https://cdn.discordapp.com/attachments/358372741952438273/583423507912982569/SELogo-BlackContour.png')



def setup(client):
    client.add_cog(sinfo(client))