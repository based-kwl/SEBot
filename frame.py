from __future__ import (absolute_import, division, print_function, unicode_literals)
import discord
from discord.ext import commands, tasks
from discord import File
from datetime import date
import datetime
from astropy.coordinates import get_sun
from astropy.coordinates import get_moon
import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import astropy.units as u
from geopy import geocoders
import asyncio
from concurrent.futures import ThreadPoolExecutor
from astroplan.plots import plot_finder_image
from astroplan import FixedTarget
import astroquery
from astroquery.skyview import SkyView
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS
from astropy.utils import iers
from astropy.utils.data import clear_download_cache
import urllib
from urllib import request

iers.conf.auto_download = False
clear_download_cache()
iers.conf.auto_max_age = None

def frame(fov, targetname):
    target = FixedTarget.from_name(targetname)
    survey="DSS2 Red"
    grid= True
    fov_radius = fov * u.arcmin
    coord = target if not hasattr(target, 'coord') else target.coord
    position = coord.icrs
    pos = str(position).split("\n")[1]
    pos = pos.replace(" ", "")
    pos = pos.replace("(", "")
    pos = pos.replace(")", "")
    pos = pos.replace(">", "")
    ra = pos.split(",")[0]
    dec = pos.split(",")[1]

    coordinates = 'icrs'
    target_name = None if isinstance(target, SkyCoord) else target.name
    test = str(SkyView.get_image_list(position=position, coordinates=coordinates,
                                      survey=survey, radius=fov_radius, grid=grid, pixels=1500, scaling="Log"))
    url = test[2:-6] + "jpg"
    print(url)
    urllib.request.urlretrieve(url, 'frame.jpg')
    return ra, dec, url

def planetarium(fov, targetname):
    target = FixedTarget.from_name(targetname)
    survey="DSS2 Red"
    grid= True
    fov_radius = fov * u.arcmin
    coord = target if not hasattr(target, 'coord') else target.coord
    position = coord.icrs
    pos = str(position).split("\n")[1]
    pos = pos.replace(" ", "")
    pos = pos.replace("(", "")
    pos = pos.replace(")", "")
    pos = pos.replace(">", "")
    ra = pos.split(",")[0]
    dec = pos.split(",")[1]

    coordinates = 'icrs'
    target_name = None if isinstance(target, SkyCoord) else target.name
    test = str(SkyView.get_image_list(position=position, coordinates=coordinates,
                                      survey=survey, radius=fov_radius, grid=grid, pixels=1500, scaling="Log"))
    url = test[2:-6] + "jpg"
    print(url)

    return ra, dec, url


class filter(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def frame(self, ctx, argfov, *, targetname: str = None):
        channel = ctx.channel
        message = ctx.message
        content = message.content
        author = message.author
        loop = asyncio.get_event_loop()
        if argfov == 'help':
            em0 = discord.Embed(
                title='Help for frame',
                description='.frame [fov] [DSO] - displays target DSO at a certain fov with RA and DEC.',
                color=0x1e73e3
            )
            await channel.send(embed=em0)
            return
        if float(argfov) > 30:
            em = discord.Embed(
                title='Sorry, fov too large.',
                description='Please use a fov smaller than 30.'
            )
            await channel.send(embed=em)
            return
        if float(argfov) < 0.01:
            em = discord.Embed(
                title='Sorry, fov too small.',
                description='Please use a fov larger than 0.01.'
            )
            await channel.send(embed=em)
            return
        fov = float(argfov) * 60
        try:
            await channel.send("Fetching image... The larger the fov, the longer it will take.")
            ra, dec, url = await loop.run_in_executor(ThreadPoolExecutor(), frame, fov, targetname)
            ori = await channel.send(ctx.author.mention + ', ' + str(targetname) + " at " + str(argfov) + ' °:',
                               file=File("/home/SE/frame.jpg"))
            prompt = await channel.send("React with \"🪐\" below to enter planetarium mode.")
            await prompt.add_reaction(emoji="🪐")
            try:
                reaction, user = await self.client.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author, timeout=60)
                if reaction.emoji == "🪐":
                    em0 = discord.Embed(
                        title="Current Position: \nRA: " + ra + "\nDec: " + dec
                    )
                    em0.set_image(url=url)
                    em0.set_footer(
                        text="React with ◀️ or ▶️ to shift RA. React with 🔽 or 🔼 to shift DEC. Shifts are by half the fov. Times out after 60 seconds.")
                    msg = await channel.send(embed=em0)
                    await ori.delete()
                    while True:
                        try:
                            await msg.add_reaction(emoji="◀")
                            await msg.add_reaction(emoji="🔽")
                            await msg.add_reaction(emoji="🔼")
                            await msg.add_reaction(emoji="▶")
                            reaction, user = await self.client.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author, timeout=60)

                            prevra = ra
                            prevdec = dec

                            if reaction.emoji == "◀":
                                if float(ra) - float(fov)/60*0.5 < 0:
                                    ra = float(ra) - float(fov)/60*0.5 + 360
                                else:
                                    ra = float(ra) - float(fov)/60*0.5

                            if reaction.emoji == "▶":
                                if float(ra) + float(fov)/60 * 0.5 > 360:
                                    ra = float(ra) + float(fov)/60 * 0.5 - 360
                                else:
                                    ra = float(ra) + float(fov)/60 * 0.5

                            if reaction.emoji == "🔽":
                                if float(dec) - float(fov)/60 * 0.5 < -90:
                                    dec = -90
                                else:
                                    dec = float(dec) - float(fov)/60 * 0.5

                            if reaction.emoji == "🔼":
                                if float(dec) + float(fov)/60 * 0.5 > 90:
                                    dec = 90
                                else:
                                    print(dec)
                                    dec = float(dec) + (float(fov)/60 * 0.5)
                            print(fov)
                            targetname = str(ra) + " " + str(dec)
                            print(targetname)

                            try:
                                ra, dec, url = await loop.run_in_executor(ThreadPoolExecutor(), planetarium, fov, targetname)

                                em0 = discord.Embed(
                                    title="Current Position: \nRA: " + ra + "\nDec: " + dec,
                                    description="Previous:\nRA: " + prevra + "\nDec: " + prevdec
                                )
                                em0.set_image(url=url)
                                em0.set_footer(text="React with ◀️ or ▶️ to shift RA. React with 🔽 or 🔼 to shift DEC. Shifts are by half the fov.")
                                await msg.edit(embed=em0)
                                await msg.clear_reactions()
                            except:
                                em1 = discord.Embed(
                                    title="Error."
                                )
                                await channel.send(em1)

                        except:
                            em0 = discord.Embed(
                                title="Current Position: \nRA: " + ra + "\nDec: " + dec
                            )
                            em0.set_image(url=url)
                            em0.set_footer(
                                text="Planetarium Stopped.")
                            await msg.edit(embed=em0)
                            await msg.clear_reactions()
                            return
            except:
                await prompt.delete()
                return
        except:
            em = discord.Embed(
                title='Sorry, an error occured.',
                description='Command usages: .frame [fov] [Valid DSO]\n.frame [fov] [hh mm ss], [deg am as].'
            )
            await channel.send(embed=em)

def setup(client):
    client.add_cog(filter(client))
