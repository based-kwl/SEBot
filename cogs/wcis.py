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

iers.conf.auto_download = False
clear_download_cache()
iers.conf.auto_max_age = None

def wcis(min, loc):
    from datetime import date
    today = date.today()
    g = geocoders.GoogleV3(api_key='AIzaSyBxURcQKJy_Nl4ZRrH2bNSzJv60sxjNC1M')
    inputAddress = loc
    place, (lat, lng) = g.geocode(inputAddress, timeout=10)
    timezone = g.reverse_timezone((lat, lng))
    local_time = datetime.datetime.now(timezone.pytz_timezone)
    date = today.strftime('%Y-%m-%d')
    LOC = EarthLocation(lat=float(lat) * u.deg, lon=float(lng) * u.deg, height=195 * u.m)
    local = str(local_time)
    localperiod = str(local[11:-13])
    utcoffset = int(local[26:-3]) * u.hour
    time = Time(str(date) + " " + str(localperiod)) - utcoffset

    nebulae = ""
    galaxies = ""
    clusters = ""
    f = open("objectlist.txt", "r")
    f.readline()
    for line in f:
        target = SkyCoord.from_name(str(line.split(",")[0].split(" ")[0]))
        targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))
        fix = str(targetaltaz)[:-2]
        try:
            alt = float(fix[-12:])
        except:
            try:
                alt = float(fix[-11:])
            except:
                try:
                    alt = float(fix[-10:])
                except:
                    try:
                        alt = float(fix[-9:])
                    except:
                        try:
                            alt = float(fix[-8:])
                        except:
                            alt = float(fix[-7:])
        if alt > float(min):
            if "Nebula" in line.split(",")[0].split(" ")[1]:
                nebulae += "{:<30}".format(line.split(",")[1][1:-1]) + "| Mag: " + "{:<4}".format(line.split(",")[0].split(" ")[2]) + "| ASize: " + "{:<9}".format(line.split(",")[0].split(" ")[3]) + "| Alt: " + str("{0.alt:.5}".format(targetaltaz))[:-4] + "\n"
            if "Galaxy" in line.split(",")[0].split(" ")[1]:
                galaxies += "{:<30}".format(line.split(",")[1][1:-1]) + "| Mag: " + "{:<4}".format(line.split(",")[0].split(" ")[2]) + "| ASize: " + "{:<9}".format(line.split(",")[0].split(" ")[3]) + "| Alt: " + str("{0.alt:.5}".format(targetaltaz))[:-4] + "\n"
            if "Cluster" in line.split(",")[0].split(" ")[1]:
                clusters += "{:<30}".format(line.split(",")[1][1:-1]) + "| Mag: " + "{:<4}".format(line.split(",")[0].split(" ")[2]) + "| ASize: " + "{:<9}".format(line.split(",")[0].split(" ")[3]) + "| Alt: " + str("{0.alt:.5}".format(targetaltaz))[:-4] + "\n"

    return (nebulae + "+" + galaxies + "+" + clusters)

class analysis(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def wcis(self, ctx, min: str=None, loc: str=None):
        channel = ctx.channel
        message = ctx.message
        content = message.content
        author = message.author
        loop = asyncio.get_event_loop()
        if min == 'help':
            em0 = discord.Embed(
                title='Help for wcis (What can I see?)',
                description='.wcis [min altitude (default 30)] [location] - displays a list of DSOs above input altitude.\nExample: .wcis 30 Macon',
                color=0x1e73e3
            )
            await channel.send(embed=em0)
            return
        try:
            int(min)
        except:
            loc = min
            min = 30
        if float(min) < 0:
            em = discord.Embed(
                title='Altitude limit too low.',
                description='Limit must be the horizon (>0)'
            )
            await channel.send(embed=em)
            return
        if float(min) > 90:
            em = discord.Embed(
                title='Altitude limit too high.',
                description='Limit must be below the zenith (<90)'
            )
            await channel.send(embed=em)
            return
        try:
            result = await loop.run_in_executor(ThreadPoolExecutor(), wcis, min, loc)
        except:
            em1 = discord.Embed(
                title="An error has occured.",
                description="Make sure you are entering a valid location."
            )
            await channel.send(embed=em1)
            return
        nebulae = result.split("+")[0]
        galaxies = result.split("+")[1]
        clusters = result.split("+")[2]

        await channel.send(author.mention + " List of objects currently above " + str(min) + " altitude.")
        if len(nebulae) < 2000:
            await channel.send("**Nebulae**```" + nebulae + " ```")
        else:
            await channel.send("**Nebulae**```" + nebulae[:2000] + "... ```")
            await channel.send("```..." + nebulae[2000:] + " ```")
        if len(galaxies) < 2000:
            await channel.send("**Galaxies**```" + galaxies + " ```")
        else:
            await channel.send("**Galaxies**```" + galaxies[:2000] + "... ```")
            await channel.send("```..." + galaxies[2000:] + " ```")
        if len(clusters) < 2000:
            await channel.send("**Clusters**```" + clusters + " ```")
        else:
            await channel.send("**Clusters**```" + clusters[:2000] + "... ```")
            await channel.send("```..." + clusters[2000:] + " ```")


def setup(client):
    client.add_cog(analysis(client))
