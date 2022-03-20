import discord
from discord.ext import commands, tasks
from discord import File
import re
import csv

bad = []
command = False
with open('unepic.csv', 'r',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        bad.append(row)

print(bad)

class filter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        global bad
        global command
        if message.author.id == 319042188967280640 and command is True:
            await message.delete()
            command = False
            return

        if message.author.id == 279002069741076483 and message.guild.id == 573622896300261381:
            pmessage = (message.content.lower()).replace(" ", "")
            for i in range(len(bad)):
                if bad[i][0] in pmessage:
                    await message.delete()
                    if message.content.startswith("v!say"):
                        command = True
                    return
            result = re.sub('[^epic]', '', pmessage)
            if "epic" in result:
                if message.content.startswith("v!say"):
                    command = True
                await message.delete()
                return
            resulte = "".join(dict.fromkeys(result))
            if "epic" in resulte:
                if message.content.startswith("v!say"):
                    command = True
                await message.delete()

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        admin = discord.utils.get(user.guild.roles, name="Supreme Goose")
        if admin in user.roles:
            if reaction.emoji == '➕':
                m = reaction.message.content.lower().replace(" ", "")
                bad.append(m)
                await reaction.message.delete()
                with open('unepic.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([m])



def setup(client):
    client.add_cog(filter(client))
