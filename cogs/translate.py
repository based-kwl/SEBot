import discord
from discord.ext import commands, tasks
import random
import csv
import requests
import json
from googletrans import Translator
import logging
from asyncio import sleep
import threading
intranslate = 0
timer = 0

async def googletranslateloop(randtrans, langs, flow, prevlangname, prevtrans, prevlang):
    translator = Translator()
    for i in range(randtrans):
        randint = random.randint(0, len(langs) - 1)
        print("translating from " + prevlangname + " to " + langs[randint][0])
        prevtrans = translator.translate(prevtrans, src=prevlang, dest=langs[randint][1]).text
        prevlang = langs[randint][1]
        prevlangname = langs[randint][0]
        flow += " → " + prevlangname

    translation = translator.translate(prevtrans, src=prevlang, dest="en").text
    flow += " → English"
    print("used google translate")
    return translation, flow

async def microsofttranslateloop(randtrans, langs, flow, prevlangname, prevtrans, prevlang):

    headers = {
        'Ocp-Apim-Subscription-Key': '3252cece92f4494595929576b72d0867',
        'Ocp-Apim-Subscription-Region': 'canadacentral',
        'Content-Type': 'application/json'
    }

    for i in range(randtrans):
        randint = random.randint(0, len(langs) - 1)
        url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=" + langs[randint][
            1] + "&from=" + prevlang
        payload = [{'Text': prevtrans}]
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print("translating from " + prevlangname + " to " + langs[randint][0])
        prevlang = langs[randint][1]
        prevlangname = langs[randint][0]
        flow += " → " + prevlangname
        prevtrans = json.loads(r.content.decode('utf-8')[1:-1])['translations'][0]['text']
    url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=en&from=" + prevlang
    payload = [{'Text': prevtrans}]
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    translation = json.loads(r.content.decode('utf-8')[1:-1])['translations'][0]['text']
    flow += " → English"
    print("used microsoft")
    return translation, flow

class translate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def translate(self, ctx, *, arg):
        global timer
        global intranslate
        if intranslate == 1:
            await ctx.channel.send("Something is already being translated. Please wait for that request to finish.")
            return
        if timer != 0:
            await ctx.channel.send("Please wait " + str(timer) + " seconds before trying again. (This cooldown is shared between all servers)")
            return
        if len(ctx.message.content) > 64:
            await ctx.channel.send("Please keep the request under 64 characters long.")
            return
        intranslate = 1
        langs = []
        prevlang = "en"
        prevtrans = arg
        prevlangname = "English"
        flow = "English"
        try:
            with open("lang2.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    langs.append(row)

            randtrans = random.randint(5, 12)
            try:
                translation, flow = await googletranslateloop(randtrans, langs, flow, prevlangname, prevtrans, prevlang)

            except:
                logging.exception("msg")
                langs = []
                prevlang = "en"
                prevtrans = arg
                prevlangname = "English"
                flow = "English"
                with open("lang.csv", "r", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        langs.append(row)
                translation, flow = await microsofttranslateloop(randtrans, langs, flow, prevlangname, prevtrans, prevlang)

        except:
            intranslate = 0
            await ctx.channel.send("And error occured")
            return

        await ctx.channel.send("Translated " + str(randtrans+1) + " times, from " + flow + ":")
        await ctx.channel.send("`" + translation + "`")
        timer = 5
        intranslate = 0
        for x in range(5):
            if timer < 1:
                return
            timer = timer - 1
            await sleep(1)


def setup(client):
    client.add_cog(translate(client))
