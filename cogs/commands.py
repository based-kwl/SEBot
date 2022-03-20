import discord
from discord.ext import commands, tasks
from discord import File
import time
import asyncio
from itertools import cycle
from itertools import islice
import itertools
import random


class coms(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx,):
        em1 = discord.Embed(
            title='List of available commands:',
            description='.help - opens this window.\n.suggest - Makes a suggestion.\n.ask - for asking yes/no & when questions.\n.gen - opens the nebula generator window\n.fov help - opens the .fov command window.\n.color [#FFFFFF]- (nitro boosters only) Sets the user color.\n.info - Displays a lot of (useless) information.\n.analyze [file] - Displays useful SE troubleshooting info.\n.pl8 [astrophotograph of stars/DSOs] - Plate solves the image with labels.\n.plan help - Astronomy planner help.\n .frame help - frame command help.\n.wcis help - "What can I see?" help.',
            color=0x1e73e3
        )
        em99 = discord.Embed(
            title='Other non-accessible commands:',
            description='.c - Indiscriminate purge\n.clear - Selective purge\n.load/unload/reload - load/unload/reload modules\n.stats - Sets the status\n.terminate - Kills the bot\n.acolor [FFFFFF] [argument] - Admin color.',
            color=0x1e73e3
        )
        em2 = discord.Embed(
            title='List of functions:',
            description='-Message relay between servers and channels.\n-Self assign role with reaction.\n',
            color=0x1e73e3
        )
        em2.set_footer(text='Bot made by Phunnie.')
        await ctx.channel.send(embed=em1)
        await ctx.channel.send(embed=em99)
        await ctx.channel.send(embed=em2)

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx, *, arg):
        await self.client.change_presence(activity=discord.Game(name=str(arg)))
        await ctx.channel.send('Status set.')

    @commands.command(pass_context=True)
    async def c(self, ctx, limit: int):
        role = discord.utils.get(ctx.author.guild.roles, id=390675873206108181)
        if role in ctx.author.roles:
            channel = ctx.channel
            limit += 1
            deleted = await ctx.channel.purge(limit=limit)
            msg = await channel.send('Deleted {} message(s)'.format(len(deleted)-1))
            await asyncio.sleep(5)
            await msg.delete()

    @commands.command(pass_context=True)
    async def clear(self, ctx, arg, limit: int):
        channel = ctx.channel
        author = ctx.message.author
        role = discord.utils.get(author.guild.roles, id=390675873206108181)
        deleted = 0
        if role in author.roles:
            user = str(ctx.message.mentions[0])
            if str(author) in user:
                limit += 1
            for i in range(1, limit+1):
                check = await channel.history().get(author__name=user[:-5])
                if check is None:
                    break
                await check.delete()
                deleted += 1
            if str(author) in user:
                deleted -= 1
                msg = await channel.send('Deleted {} (+1) message(s)'.format(str(deleted)))
                await asyncio.sleep(5)
                await msg.delete()
                await ctx.message.delete()
                return
            msg = await channel.send('Deleted {} message(s)'.format(str(deleted)))
            await asyncio.sleep(5)
            await msg.delete()
            await ctx.message.delete()

    @commands.command()
    @commands.is_owner()
    async def aclear(self, ctx, arg, limit: int):
        channel = ctx.channel
        author = ctx.message.author
        deleted = 0
        user = str(ctx.message.mentions[0])
        if str(author) in user:
            limit += 1
        for i in range(1, limit + 1):
            check = await channel.history().get(author__name=user[:-5])
            if check is None:
                break
            await check.delete()
            deleted += 1
        if str(author) in user:
            deleted -= 1
            msg = await channel.send('Deleted {} (+1) message(s)'.format(str(deleted)))
            await asyncio.sleep(5)
            await msg.delete()
            await ctx.message.delete()
            return
        msg = await channel.send('Deleted {} message(s)'.format(str(deleted)))
        await asyncio.sleep(5)
        await msg.delete()
        await ctx.message.delete()


    @commands.command(pass_context=True)
    @commands.is_owner()
    async def terminate(self, ctx):
        valid_users = ['Phunnie#0990']
        if str(ctx.message.channel) and str(ctx.message.author) in valid_users:
            exit()

    @commands.command(pass_context=True)
    async def info(self, ctx):
        members = set(ctx.message.guild.members)
        offline = filter(lambda m: m.status is discord.Status.offline, members)
        offline = set(offline)
        bots = filter(lambda m: m.bot, members)
        bots = set(bots)
        channel= ctx.channel
        users = members - bots
        servericon = ctx.message.guild.icon_url
        server_passed = (ctx.message.created_at - ctx.message.guild.created_at).days

        server_created_at = (
            "Created on {} ({} days ago!)".format(ctx.message.guild.created_at.strftime("%d %b %Y %H:%M"),
                                                  server_passed))
        try:
            em = discord.Embed(color=0x1e73e3, title="Server Info")
            em.set_thumbnail(url=servericon)
            em.add_field(name="Server Name", value=str(ctx.message.guild.name))
            em.add_field(name="Server ID", value=str(ctx.message.guild.id))
            em.add_field(name="Server Region", value=str(ctx.message.guild.region))
            em.add_field(name="Server Verification", value=str(ctx.message.guild.verification_level))
            em.add_field(name="Server Created At", value=str(server_created_at))
            em.add_field(name="Server Roles", value=str(len(ctx.message.guild.roles) - 1))
            em.add_field(name="Server Owner", value=str(ctx.message.guild.owner.name))
            em.add_field(name="Owner ID", value=str(ctx.message.guild.owner.id))
            em.add_field(name="Owner Nick", value=str(ctx.message.guild.owner.nick))
            em.add_field(name="Owner Status", value=str(ctx.message.guild.owner.status))
            em.add_field(name="Total Bots", value=str(len(bots)))
            em.add_field(name="Bots Online", value=str(len(bots - offline)))
            em.add_field(name="Bots Offline", value=str(len(bots & offline)))
            em.add_field(name="Total Users", value=str(len(users)))
            em.add_field(name="Online Users", value=str(len(users - offline)))
            em.add_field(name="Offline Users", value=str(len(users & offline)))
            await ctx.channel.send(embed=em)
        except discord.HTTPException:
            await ctx.channel.send("An unknown error occured while sending the embedded message.")


def setup(client):
    client.add_cog(coms(client))
