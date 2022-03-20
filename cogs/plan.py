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

class Target:
    def __init__(self, day, alt):
        self.day = day
        self.alt = alt

def plot(arg1):
    from datetime import date
    today = date.today()
    args = arg1.split(';')
    arg1 = args[0]
    arg2 = args[1]
    print(arg1)
    print(arg2)
    g = geocoders.GoogleV3(api_key='AIzaSyBxURcQKJy_Nl4ZRrH2bNSzJv60sxjNC1M')
    inputAddress = arg2
    place, (lat, lng) = g.geocode(inputAddress, timeout=10)
    timezone = g.reverse_timezone((lat, lng))
    local_time = datetime.datetime.now(timezone.pytz_timezone)
    date = today.strftime('%Y-%m-%d')
    target = SkyCoord.from_name(str(arg1))
    LOC = EarthLocation(lat=float(lat) * u.deg, lon=float(lng) * u.deg, height=195 * u.m)
    local = str(local_time)
    localperiod = str(local[11:-13])
    utcoffset = int(local[26:-3]) * u.hour
    time = Time(str(date) + " " + str(localperiod)) - utcoffset

    targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))

    midnight = Time(str(date) + ' 00:00:00') - utcoffset

    delta_midnight = np.linspace(-12, 12, 1000) * u.hour
    times = midnight + delta_midnight
    frame = AltAz(obstime=times, location=LOC)
    sunaltazs = get_sun(times).transform_to(frame)


    moon = get_moon(times)
    moonaltazs = moon.transform_to(frame)

    #Find the coords

    targetsaltz = target.transform_to(frame)

    #Graph

    plt.plot(delta_midnight, moonaltazs.alt, color='#d9d5a7', ls='--', label='Moon')
    plt.scatter(delta_midnight, targetsaltz.alt,
                c=targetsaltz.az, label=str(arg1), lw=0, s=8,
                cmap='viridis')
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -0 * u.deg, color='0.95', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -2 * u.deg, color='0.9', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -4 * u.deg, color='0.8', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -6 * u.deg, color='0.7', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -8 * u.deg, color='0.5', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -10 * u.deg, color='0.3', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -12 * u.deg, color='0.2', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -14 * u.deg, color='0.1', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -16 * u.deg, color='0.05', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -18 * u.deg, color='k', zorder=0)
    plt.colorbar().set_label('Azimuth [deg]')
    plt.legend(loc='upper left')
    plt.xlim(-12, 12)
    plt.xticks(np.arange(13) * 2 - 12)
    plt.ylim(0, 90)
    plt.xlabel('Hours from Midnight')
    plt.ylabel('Altitude [deg]')
    plt.savefig('shid.png')
    plt.close()
    return targetaltaz

def plot2(arg0, arg1):
    from datetime import date
    today = date.today()
    args = arg1.split(';')
    arg1 = args[0]
    arg2 = args[1]
    g = geocoders.GoogleV3(api_key='AIzaSyBxURcQKJy_Nl4ZRrH2bNSzJv60sxjNC1M')
    inputAddress = arg2
    place, (lat, lng) = g.geocode(inputAddress, timeout=10)
    timezone = g.reverse_timezone((lat, lng))
    local_time = datetime.datetime.now(timezone.pytz_timezone)
    date = today.strftime('%Y-%m-%d')
    target = SkyCoord.from_name(str(arg1))
    LOC = EarthLocation(lat=float(lat) * u.deg, lon=float(lng) * u.deg, height=195 * u.m)
    local = str(local_time)
    localperiod = str(local[11:-13])
    utcoffset = int(local[26:-3]) * u.hour
    time = Time(str(arg0) + " " + str(localperiod)) - utcoffset

    targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))

    midnight = Time(str(arg0) + ' 00:00:00') - utcoffset

    delta_midnight = np.linspace(-12, 12, 1000) * u.hour
    times = midnight + delta_midnight
    frame = AltAz(obstime=times, location=LOC)
    sunaltazs = get_sun(times).transform_to(frame)


    moon = get_moon(times)
    moonaltazs = moon.transform_to(frame)

    #Find the coords

    targetsaltz = target.transform_to(frame)

    #Graph

    plt.plot(delta_midnight, moonaltazs.alt, color='#d9d5a7', ls='--', label='Moon')
    plt.scatter(delta_midnight, targetsaltz.alt,
                c=targetsaltz.az, label=str(arg1), lw=0, s=8,
                cmap='viridis')
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -0 * u.deg, color='0.95', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -2 * u.deg, color='0.9', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -4 * u.deg, color='0.8', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -6 * u.deg, color='0.7', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -8 * u.deg, color='0.5', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -10 * u.deg, color='0.3', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -12 * u.deg, color='0.2', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -14 * u.deg, color='0.1', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -16 * u.deg, color='0.05', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -18 * u.deg, color='k', zorder=0)

    plt.colorbar().set_label('Azimuth [deg]')
    plt.legend(loc='upper left')
    plt.xlim(-12, 12)
    plt.xticks(np.arange(13) * 2 - 12)
    plt.ylim(0, 90)
    plt.xlabel('Hours from Midnight')
    plt.ylabel('Altitude [deg]')
    plt.savefig('shid.png')
    plt.close()
    return targetaltaz

def plot3(arg1):
    from datetime import date
    today = date.today()
    args = arg1.split(';')
    arg1 = args[0]
    arg2 = args[1]
    print(arg1)
    print(arg2)
    g = geocoders.GoogleV3(api_key='AIzaSyBxURcQKJy_Nl4ZRrH2bNSzJv60sxjNC1M')
    inputAddress = arg2
    place, (lat, lng) = g.geocode(inputAddress, timeout=10)
    timezone = g.reverse_timezone((lat, lng))
    local_time = datetime.datetime.now(timezone.pytz_timezone)
    date = today.strftime('%Y-%m-%d')
    target = SkyCoord.from_name(str(arg1))
    LOC = EarthLocation(lat=float(lat) * u.deg, lon=float(lng) * u.deg, height=195 * u.m)
    local = str(local_time)
    localperiod = str(local[11:-13])
    utcoffset = int(local[26:-3]) * u.hour
    time = Time(str(date) + " " + str(localperiod)) - utcoffset

    targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))

    midnight = Time(str(date) + " " + str(localperiod)) - utcoffset

    delta_midnight = np.linspace(0, 24, 1000) * u.hour
    times = midnight + delta_midnight
    frame = AltAz(obstime=times, location=LOC)
    sunaltazs = get_sun(times).transform_to(frame)


    moon = get_moon(times)
    moonaltazs = moon.transform_to(frame)

    #Find the coords

    targetsaltz = target.transform_to(frame)

    #Graph

    plt.plot(delta_midnight, moonaltazs.alt, color='#d9d5a7', ls='--', label='Moon')
    plt.scatter(delta_midnight, targetsaltz.alt,
                c=targetsaltz.az, label=str(arg1), lw=0, s=8,
                cmap='viridis')
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -0 * u.deg, color='0.95', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -2 * u.deg, color='0.9', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -4 * u.deg, color='0.8', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -6 * u.deg, color='0.7', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -8 * u.deg, color='0.5', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -10 * u.deg, color='0.3', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -12 * u.deg, color='0.2', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -14 * u.deg, color='0.1', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -16 * u.deg, color='0.05', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90,
                     sunaltazs.alt < -18 * u.deg, color='k', zorder=0)
    plt.colorbar().set_label('Azimuth [deg]')
    plt.legend(loc='upper left')
    plt.xlim(0, 24)
    plt.xticks(np.arange(13) * 2 + 0)
    plt.ylim(0, 90)
    plt.xlabel('Hours from now')
    plt.ylabel('Altitude [deg]')
    plt.savefig('shid.png')
    plt.close()
    return targetaltaz

def plotyear(arg1):
    from datetime import date
    today = date.today()
    args = arg1.split(';')
    arg1 = args[0]
    arg2 = args[1]
    g = geocoders.GoogleV3(api_key='AIzaSyBxURcQKJy_Nl4ZRrH2bNSzJv60sxjNC1M')
    inputAddress = arg2
    place, (lat, lng) = g.geocode(inputAddress, timeout=10)
    timezone = g.reverse_timezone((lat, lng))
    local_time = datetime.datetime.now(timezone.pytz_timezone)
    date = today.strftime('%Y-%m-%d')
    target = SkyCoord.from_name(str(arg1))
    LOC = EarthLocation(lat=float(lat) * u.deg, lon=float(lng) * u.deg, height=195 * u.m)
    local = str(local_time)
    localperiod = str(local[11:-13])
    utcoffset = int(local[26:-3]) * u.hour
    times = []
    day=[]
    best = Target("January 1", 0)
    for f in range(1, 366):
        day.append(f)
    for jan in range(1, 32):
        time = Time("2018-01-" + str(jan) + " " + "00:00:00.000") - utcoffset
        targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))
        alt = float((targetaltaz.alt.to_string(unit=u.deg, decimal=True)))
        times.append(alt)
        if alt > best.alt:
            best.day = "January " + str(jan)
            best.alt = alt

    for feb in range(1, 29):
        time = Time("2018-02-" + str(feb) + " " + "00:00:00.000") - utcoffset
        targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))
        alt = float((targetaltaz.alt.to_string(unit=u.deg, decimal=True)))
        times.append(alt)
        if alt > best.alt:
            best.day = "February " + str(feb)
            best.alt = alt

    for mar in range(1, 32):
        time = Time("2018-03-" + str(mar) + " " + "00:00:00.000") - utcoffset
        targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))
        alt = float((targetaltaz.alt.to_string(unit=u.deg, decimal=True)))
        times.append(alt)
        if alt > best.alt:
            best.day = "March " + str(mar)
            best.alt = alt

    for apr in range(1, 31):
        time = Time("2018-04-" + str(apr) + " " + "00:00:00.000") - utcoffset
        targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))
        alt = float((targetaltaz.alt.to_string(unit=u.deg, decimal=True)))
        times.append(alt)
        if alt > best.alt:
            best.day = "April " + str(apr)
            best.alt = alt

    for may in range(1, 32):
        time = Time("2018-05-" + str(may) + " " + "00:00:00.000") - utcoffset
        targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))
        alt = float((targetaltaz.alt.to_string(unit=u.deg, decimal=True)))
        times.append(alt)
        if alt > best.alt:
            best.day = "May " + str(may)
            best.alt = alt

    for jun in range(1, 31):
        time = Time("2018-06-" + str(jun) + " " + "00:00:00.000") - utcoffset
        targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))
        alt = float((targetaltaz.alt.to_string(unit=u.deg, decimal=True)))
        times.append(alt)
        if alt > best.alt:
            best.day = "June " + str(jun)
            best.alt = alt

    for jul in range(1, 32):
        time = Time("2018-07-" + str(jul) + " " + "00:00:00.000") - utcoffset
        targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))
        alt = float((targetaltaz.alt.to_string(unit=u.deg, decimal=True)))
        times.append(alt)
        if alt > best.alt:
            best.day = "July " + str(jul)
            best.alt = alt

    for aug in range(1, 32):
        time = Time("2018-08-" + str(aug) + " " + "00:00:00.000") - utcoffset
        targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))
        alt = float((targetaltaz.alt.to_string(unit=u.deg, decimal=True)))
        times.append(alt)
        if alt > best.alt:
            best.day = "August " + str(aug)
            best.alt = alt

    for sep in range(1, 31):
        time = Time("2018-09-" + str(sep) + " " + "00:00:00.000") - utcoffset
        targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))
        alt = float((targetaltaz.alt.to_string(unit=u.deg, decimal=True)))
        times.append(alt)
        if alt > best.alt:
            best.day = "September " + str(sep)
            best.alt = alt

    for oct in range(1, 32):
        time = Time("2018-10-" + str(oct) + " " + "00:00:00.000") - utcoffset
        targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))
        alt = float((targetaltaz.alt.to_string(unit=u.deg, decimal=True)))
        times.append(alt)
        if alt > best.alt:
            best.day = "October " + str(oct)
            best.alt = alt

    for nov in range(1, 31):
        time = Time("2018-11-" + str(nov) + " " + "00:00:00.000") - utcoffset
        targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))
        alt = float((targetaltaz.alt.to_string(unit=u.deg, decimal=True)))
        times.append(alt)
        if alt > best.alt:
            best.day = "November " + str(nov)
            best.alt = alt

    for dec in range(1, 32):
        time = Time("2018-12-" + str(dec) + " " + "00:00:00.000") - utcoffset
        targetaltaz = target.transform_to(AltAz(obstime=time, location=LOC))
        alt = float((targetaltaz.alt.to_string(unit=u.deg, decimal=True)))
        times.append(alt)
        if alt > best.alt:
            best.day = "December " + str(dec)
            best.alt = alt

    plt.scatter(day, times, c=times, label=str(arg1), lw=0, s=8,
                cmap='brg')
    plt.ylim(0, 90)
    plt.xlim(1, 366)
    plt.title(arg1)
    plt.xticks([])
    plt.xlabel('Jan    Feb    Mar    Apr    May    Jun    Jul    Aug    Sep    Oct    Nov    Dec')
    plt.ylabel('Altitude at midnight')
    plt.savefig('shid.png')
    plt.close()
    return best

class filter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def plan(self, ctx, arg0: str = None, *, arg1: str = None):
        channel = ctx.channel
        message = ctx.message
        content = message.content
        author = message.author
        loop = asyncio.get_event_loop()
        if arg0 == 'help':
            em0 = discord.Embed(
                title='Usage of astronomy planner:',
                description='.plan [argument\*] [DSO];[Location]. Ex: .plan year andromeda; montreal\n'
                            '.plan [DSO]; [Location] - Gives the Alt and Az of the target today.\n'
                            '\n'
                            '\*Valid arguments:\n'
                            'year - displays a graph of the altitude of the DSO at midnight.\n'
                            'now - displays a graph of alt and az of target for the next 24 hours.\n'
                            'YYYY-MM-DD - displays a graph of alt and az of target at that date.',                color=0x1e73e3
            )
            await channel.send(embed=em0)
            return
        try:
            arg = arg1.split(';')
            if arg0 == 'now':
                result = await loop.run_in_executor(ThreadPoolExecutor(), plot3, arg1)
                await channel.send(ctx.author.mention + " Altitude of " + str(arg[0]) + " for the next 24 hours.\nCurrent altitude: {0.alt:.5}".format(result), file=File("shid.png"))
                return
            if arg0 == 'year':
                best = await loop.run_in_executor(ThreadPoolExecutor(), plotyear, arg1)
                await channel.send(ctx.author.mention + " Altitude of " + str(arg[0]) + " at mignight throughout the year. Object will be at highest on " + best.day + " with an altitude of " + str(best.alt) + ".", file=File("shid.png"))
                return
            else:
                result = await loop.run_in_executor(ThreadPoolExecutor(), plot2, arg0, arg1)
                await channel.send(ctx.author.mention + " Altitude of " + str(arg[0]) + " on " + str(arg0), file=File("shid.png"))
        except:
            try:
                arg1 = str(arg0) + ' ' + str(arg1)
                arg = arg1.split(';')
                result = await loop.run_in_executor(ThreadPoolExecutor(), plot, arg1)
                await channel.send(ctx.author.mention + " Current altitude of " + str(arg[0]) + " = {0.alt:.5}".format(result), file=File("shid.png"))
            except:
                em = discord.Embed(
                    title='Sorry, an error occured.',
                    description='Please make sure you are selecting an existing DSO and are using a real location.'
                )
                await channel.send(embed=em)

def setup(client):
    client.add_cog(filter(client))
