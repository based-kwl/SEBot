import discord
from discord.ext import commands, tasks
from discord import File
from datetime import date, datetime, timezone
import time
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
import requests
import urllib.request
import logging

today = date.today()
def plot(arg0):
    g = geocoders.GoogleV3(api_key='AIzaSyBxURcQKJy_Nl4ZRrH2bNSzJv60sxjNC1M')
    inputAddress = arg0
    place, (lat, lng) = g.geocode(inputAddress, timeout=10)
    urllib.request.urlretrieve("https://clearoutside.com/forecast_image_large/" + "{:.2f}".format(lat) + "/" + "{:.2f}".format(
        lng) + "/forecast.png", "weather.png")
    lat=str(lat)+"N"
    lng=str(lng)+"E"

    e = requests.request('POST', 'https://www.meteoblue.com/en/weather/week/' + lat + lng)
    print(lat)
    print(lng)
    urllib.request.urlretrieve("https://" +
        str(e.content).split(
        '''<input type="text" id="meteogram_src" readonly style="width: 100%;" tabindex="-1" value=\\'<img src="//''')[
              1].split('''" srcset="''')[0].replace("&amp;", "&"), "meteoblue.png")
    return

class Weather(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def weather(self, ctx, *, arg0: str = None):
        channel = ctx.channel
        message = ctx.message
        content = message.content
        author = message.author
        loop = asyncio.get_event_loop()
        if arg0 == 'help':
            em0 = discord.Embed(
                title='Help for weather forecast',
                description='.weather [location] - Queries clearoutside for weather forecast.\n',
                color=0x1e73e3
            )
            await channel.send(embed=em0)
            return
        try:
            await loop.run_in_executor(ThreadPoolExecutor(), plot, arg0)
            await channel.send("Forecast for the upcoming days: ",file=File("weather.png"))
            await channel.send("Meteograms for the next 5 days: ",file=File("meteoblue.png"))
        except:
            logging.exception("msg")
            em = discord.Embed(
                title='Sorry, an error occured.',
                description='Please make sure you are using a real location.'
            )
            await channel.send(embed=em)

def setup(client):
    client.add_cog(Weather(client))
