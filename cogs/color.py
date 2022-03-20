import discord
from discord.ext import commands
from discord import File
import time
import asyncio
from itertools import cycle
from itertools import islice
import itertools
import random


class color(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def color(self, ctx, arg1, *, arg2: str = None):
        user = ctx.message.author
        user1 = str(user)
        name = user1[:-5]
        channel = ctx.message.channel
        server = ctx.message.guild
        content = ctx.message.content
        Nitro = discord.utils.get(user.guild.roles, name="very cool kids (Nitro Booster)")
        color = discord.utils.get(user.guild.roles, name=str(name))
        nitrorolepos = discord.utils.get(user.guild.roles, name="━━━━ Nitro Boosters")
        nitropos = nitrorolepos.position
        if 'help' in content:
            emc = discord.Embed(
                title='**.color command usage:**',
                description='Nitro boosters only.',
                color=0x1e73e3
            )
            emc.add_field(name='.color [#FFFFFF]', value='Sets the color with hex values(use without [brackets].)')
            emc.add_field(name='.color clear', value='Clears the color.')
            await channel.send(embed=emc)
            return
        if Nitro in user.roles:
            try:
                if arg1 == 'clear':
                    await color.delete()
                    emc = discord.Embed(
                        title='Color Removed.',
                        color=0x000000
                    )
                    await channel.send(embed=emc)
                    return

                if '0x' in arg1:
                    hex_str = arg1[2:]
                elif '#' in arg1:
                    hex_str = arg1[1:]
                elif '[' in arg1:
                    hex_str = arg1[1:-1]
                else:
                    hex_str = arg1
                hex_int = int(hex_str, 16)

                try:
                    await color.edit(color=discord.Color(int(hex_int)))
                    emc = discord.Embed(
                        title='Color Changed.',
                        color=hex_int
                    )
                    await channel.send(embed=emc)
                    return
                except:
                    await server.create_role(name=str(name), color=discord.Color(int(hex_int)))
                    await asyncio.sleep(0.5)
                    rc = discord.utils.get(user.guild.roles, name=str(name))
                    await asyncio.sleep(0.5)
                    await rc.edit(position=nitropos)
                    await asyncio.sleep(0.5)
                    await user.add_roles(rc)
                    emc = discord.Embed(
                        title='Color Changed.',
                        color=hex_int
                    )
                    await channel.send(embed=emc)
                    return
            except:
                emc = discord.Embed(
                    title='Invalid color parameter',
                    color=0x000000
                )
                await channel.send(embed=emc)
                return
        emc = discord.Embed(
            title='Sorry, this feature is for Nitro Boosters only.',
            description='If you believe there was a mistake, ping @Phunnie#0990',
            color=0x000000
        )
        await channel.send(embed=emc)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.guild.id != 148933808811409408:
            return
        userb = before
        usera = after

        try:
            nitro = discord.utils.get(usera.guild.roles, name="very cool kids (Nitro Booster)")
            if nitro in usera.roles and nitro in userb.roles and userb.name != usera.name:
                print(userb.name)
                print(usera.name)
                colorb = discord.utils.get(usera.guild.roles, name=str(userb.name))
                await colorb.edit(name=str(usera.name))
        except:
            print("err")


        try:
            nitro = discord.utils.get(usera.guild.roles, name="very cool kids (Nitro Booster)")
            if nitro in usera.roles:
                return
            if nitro not in userb.roles:
                return
        except:
            return
        color = usera.name
        try:
            colorrole = discord.utils.get(usera.guild.roles, name=color)
            await colorrole.delete()
        except:
            return


def setup(client):
    client.add_cog(color(client))
