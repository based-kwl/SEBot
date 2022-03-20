import discord
from discord.ext import commands, tasks
from discord import File
import requests
import json
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
from time import sleep
import urllib.request


def get_and_check(key, url, interval):
    login_req = requests.post('http://nova.astrometry.net/api/login',
                              data={'request-json': json.dumps({'apikey': 'wfboqxszgjsyeszk'})})  # Post the login

    session = login_req.json()['session']  # Get the session

    image_req = requests.get(url)  # The image request, gets the image
    image = BytesIO(image_req.content)  # stores it in a file like object

    # UPLOAD FILE START
    form_data = {
        'request-json': (None, json.dumps(
            {'publicly_visible': 'd', 'allow_modifications': 'd', 'session': session, 'allow_commerical_use': 'd'}),
                         'text/plain'),

        'file': ('test', image, 'application/octet-stream')
    }

    subid_req = requests.post('http://nova.astrometry.net/api/upload', files=form_data)
    subid = str(subid_req.json()['subid'])
    print(subid)
    # UPLOAD FILE END

    subid_status_req = requests.get('http://nova.astrometry.net/api/submissions/' + subid)  # Get submission info
    subid_status_json = subid_status_req.json()  # Turn it into json
    if ((not subid_status_json['jobs']) or (
            subid_status_json['jobs'] != [None])):  # If jobs array is empty or contains a null
        while (True):  # go into an endless loop
            subid_status_req = requests.get(
                'http://nova.astrometry.net/api/submissions/' + subid)  # Get submission info
            subid_status_json = subid_status_req.json()  # Turn it into json
            if ((subid_status_json['jobs']) and (
                    None not in subid_status_json['jobs'])):  # If Job array is not empty and it's not a null
                jobnum = str(subid_status_json['jobs'][0])  # get job number and assign it to a variable
                break  # Break out of endless  loop
            else:
                sleep(interval)  # Else sleep for (interval) (supplied in function parameter)

    # Get into an infinite loop of trying to see if it's solved or not
    while (True):
        job_status_req = requests.get('http://nova.astrometry.net/api/jobs/' + jobnum)  # Get job info
        job_status_req_json = job_status_req.json()  # Turn it into json
        if (job_status_req_json['status'] == 'success' or job_status_req_json[
            'status'] == 'failure'):  # If it's success OR failure
            break  # break out of endless loop
        else:
            sleep(interval)  # Else sleep for (interval) (supplied in function parameter)

    if (job_status_req_json['status'] == 'success'):
        urllib.request.urlretrieve('http://nova.astrometry.net/annotated_full/' + str(jobnum), 'plate.jpg')
        return {'status': 'success', 'jobnum': jobnum}

    return {'status': 'failure', 'jobnum': jobnum}

class pl8(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pl8(self, ctx, *, arg: str = None):
        channel = ctx.channel
        for attachment in ctx.message.attachments:
            url = ctx.message.attachments[0].url
        if arg is not None:
            if 'http' in arg:
                url = arg
            else:
                await channel.send('Invalid URL.')
                return
        await ctx.send('Processing your image, this could take a while. I\'ll ping you when it\'s done.')
        loop = asyncio.get_event_loop()
        try:
            result = await loop.run_in_executor(ThreadPoolExecutor(), get_and_check, 'key', url, 1)
            em = discord.Embed(
                color=0x654321
            )
            em.set_image(url='http://nova.astrometry.net/annotated_full/' + result['jobnum'])
            if (result['status'] == 'success'):
                await channel.send(ctx.author.mention, file=File('/home/SE/plate.jpg'))
            if (result['status'] == 'failure'):
                await channel.send('Sorry' + ctx.author.mention + ', the image you posted could not be solved.')
        except:
            await channel.send('An error has occurred.')


def setup(client):
    client.add_cog(pl8(client))