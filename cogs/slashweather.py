import discord
from discord.ext import commands, tasks
from discord import File
from datetime import date, datetime, timezone
from discord_slash import cog_ext
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash import SlashCommandOptionType
from discord_slash.utils import manage_commands
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

class SlashWeather(commands.Cog):
    def __init__(self, bot):
        if not hasattr(bot, "slash"):
            # Creates new SlashCommand instance to bot if bot doesn't have.
            bot.slash = SlashCommand(bot, override_type=True)
        self.bot = bot
        self.bot.slash.get_cog_commands(self)

    def cog_unload(self):
        self.bot.slash.remove_cog_commands(self)

    @cog_ext.cog_slash(name="weather")
    async def weather(self, ctx: SlashContext, arg0):
        channel = ctx.channel
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
            await ctx.send(content="Fetching...")
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

def setup(bot):
    bot.add_cog(SlashWeather(bot))
