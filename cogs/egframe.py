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
    coordinates = 'icrs'
    target_name = None if isinstance(target, SkyCoord) else target.name
    test = str(SkyView.get_image_list(position=position, coordinates=coordinates,
                                      survey=survey, radius=fov_radius, grid=grid, pixels=1500, scaling="HistEq"))
    url = test[2:-6] + "jpg"
    urllib.request.urlretrieve(url, 'frame.jpg')

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
                title='Help for frame.',
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
            result = await loop.run_in_executor(ThreadPoolExecutor(), frame, fov, targetname)
            await channel.send(ctx.author.mention + ', ' + str(targetname) + " at " + str(argfov) + ' °:', file=File("/home/econgreg/frame.jpg"))
        except:
            em = discord.Embed(
                title='Sorry, an error occured.',
                description='Command usage: .frame [fov] [Valid DSO].'
            )
            await channel.send(embed=em)

def setup(client):
    client.add_cog(filter(client))
