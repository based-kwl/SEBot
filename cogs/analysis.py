import discord
from discord.ext import commands, tasks
from discord import File
import time
import asyncio
from itertools import cycle
from itertools import islice
import itertools
import random


class analysis(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def analyze(self, ctx, *, arg: str = None):
        channel = ctx.channel
        message = ctx.message
        author = ctx.message.author
        users = ['Phunnie#0990']
        try:
            message_id = int(arg)
            msg = await channel.history().get(id=message_id)
            for attachment in msg.attachments:
                await attachment.save('/home/SE/analysis.txt')
                Errorbuffer = ''
                Warningbuffer = ''
                Ecount = 0
                Wcount = 0
                GPU = ''
                OpenGL = ''
                TRAM = ''
                ARAM = ''
                TVRAM = ''
                AVRAM = ''
                file = open('analysis.txt', encoding="ISO-8859-1")
                file.readline()
                for line in file:
                    if 'Renderer: ' in line:
                        GPU += line[15:]
                    if 'OpenGL version: ' in line:
                        OpenGL += line[21:]
                    if 'Total      RAM: ' in line:
                        TRAM += line[21:]
                    if 'Available  RAM: ' in line:
                        ARAM += line[21:]
                    if 'Max. used VRAM: ' in line:
                        AVRAM += line[21:]
                    if 'Physical  VRAM: ' in line:
                        TVRAM += line[21:]
                    if '(dynamic detection: ' in line.lower():
                        AVRAM += line[21:]
                    if 'ERROR: ' in line:
                        Errorbuffer += line
                        Ecount += 1
                    if 'WARNING: ' in line:
                        Warningbuffer += line
                        Wcount += 1
                file.close()
                file1 = open('analysis.txt', encoding="ISO-8859-1")
                lines = file1.readlines()
                Build = lines[0]
                em = discord.Embed(
                    title = 'Analysis:',
                    description = '`Build:` ' + str(Build[20:]) + '\n`Renderer:` ' + str(GPU[:-9]) + '\n`OpenGL Ver:` ' +
                    str(OpenGL) + '\n`Total RAM:` ' + str(TRAM) + '\t`Available RAM:` ' + str(ARAM) + '\n`Total VRAM:` '
                    + str(TVRAM) + '\t`Available VRAM:` '
                    + str(AVRAM),
                    color=0x1e73e3
                )
                if len(Errorbuffer) == 0:
                    em.add_field(name='Errors', value='```No errors.```')
                if len(Errorbuffer) > 0 and len(Errorbuffer) <= 1000:
                    em.add_field(name='Errors', value='```' + str(Errorbuffer) + '```')
                if len(Errorbuffer) > 1000:
                    em.add_field(name='Errors', value='```' + str(Errorbuffer[:1000]) + '... ' + str(Ecount) + ' total.```')
                if len(Warningbuffer) == 0:
                    em.add_field(name='Warnings', value='```No warnings.```')
                if len(Warningbuffer) > 0 and len(Warningbuffer) <= 1000:
                    em.add_field(name='Warnings', value='```' + str(Warningbuffer) + '```')
                if len(Warningbuffer) > 1000:
                    em.add_field(name='Warnings', value='```' + str(Warningbuffer[:1000]) + '... ' + str(Wcount) + ' total.```')
                msg = await channel.send(embed=em)
                f = open('ErrorsAndWarnings.txt', 'w+')
                f.write(
                    'Analysis:\nBuild: ' + str(Build) + '\nRenderer: ' + str(GPU) + '\nOpenGL Ver: ' +
                    str(OpenGL) + '\nTotal RAM: ' + str(TRAM) + '\nAvailable RAM: ' + str(ARAM) + '\nTotal VRAM: '
                    + str(TVRAM) + '\nAvailable VRAM: '
                    + str(AVRAM) + '\n\nTotal Errors: ' + str(Ecount) + '\nTotal Warnings: ' + str(Wcount) + '\n\nErrors: \n' + str(Errorbuffer) + '\n\nWarnings:\n' + str(Warningbuffer)
                )
                f.close()
                await channel.send(file=File('/home/SE/ErrorsAndWarnings.txt'))
        except:
            for attachment in message.attachments:
                await attachment.save('/home/SE/analysis.txt')
                Errorbuffer = ''
                Warningbuffer = ''
                Ecount = 0
                Wcount = 0
                GPU = ''
                OpenGL = ''
                TRAM = ''
                ARAM = ''
                TVRAM = ''
                AVRAM = ''
                file = open('analysis.txt', encoding="ISO-8859-1")
                file.readline()
                for line in file:
                    if 'Renderer: ' in line:
                        GPU += line[15:]
                    if 'OpenGL version: ' in line:
                        OpenGL += line[21:]
                    if 'Total      RAM: ' in line:
                        TRAM += line[21:]
                    if 'Available  RAM: ' in line:
                        ARAM += line[21:]
                    if 'Max. used VRAM: ' in line:
                        AVRAM += line[21:]
                    if 'Physical  VRAM: ' in line:
                        TVRAM += line[21:]
                    if '(dynamic detection: ' in line.lower():
                        AVRAM += line[21:]
                    if 'ERROR: ' in line:
                        Errorbuffer += line
                        Ecount += 1
                    if 'WARNING: ' in line:
                        Warningbuffer += line
                        Wcount += 1
                file.close()
                file1 = open('analysis.txt', encoding="ISO-8859-1")
                lines = file1.readlines()
                Build = lines[0]
                em = discord.Embed(
                    title = 'Analysis:',
                    description = '`Build:` ' + str(Build[20:]) + '\n`Renderer:` ' + str(GPU[:-9]) + '\n`OpenGL Ver:` ' +
                    str(OpenGL) + '\n`Total RAM:` ' + str(TRAM) + '\t`Available RAM:` ' + str(ARAM) + '\n`Total VRAM:` '
                    + str(TVRAM) + '\t`Available VRAM:` '
                    + str(AVRAM),
                    color=0x1e73e3
                )
                if len(Errorbuffer) == 0:
                    em.add_field(name='Errors', value='```No errors.```')
                if len(Errorbuffer) > 0 and len(Errorbuffer) <= 1000:
                    em.add_field(name='Errors', value='```' + str(Errorbuffer) + '```')
                if len(Errorbuffer) > 1000:
                    em.add_field(name='Errors', value='```' + str(Errorbuffer[:1000]) + '... ' + str(Ecount) + ' total.```')
                if len(Warningbuffer) == 0:
                    em.add_field(name='Warnings', value='```No warnings.```')
                if len(Warningbuffer) > 0 and len(Warningbuffer) <= 1000:
                    em.add_field(name='Warnings', value='```' + str(Warningbuffer) + '```')
                if len(Warningbuffer) > 1000:
                    em.add_field(name='Warnings', value='```' + str(Warningbuffer[:1000]) + '... ' + str(Wcount) + ' total.```')
                msg = await channel.send(embed=em)
                f = open('ErrorsAndWarnings.txt', 'w+')
                f.write(
                    'Analysis:\nBuild: ' + str(Build) + '\nRenderer: ' + str(GPU) + '\nOpenGL Ver: ' +
                    str(OpenGL) + '\nTotal RAM: ' + str(TRAM) + '\nAvailable RAM: ' + str(ARAM) + '\nTotal VRAM: '
                    + str(TVRAM) + '\nAvailable VRAM: '
                    + str(AVRAM) + '\n\nTotal Errors: ' + str(Ecount) + '\nTotal Warnings: ' + str(Wcount) + '\n\nErrors: \n' + str(Errorbuffer) + '\n\nWarnings:\n' + str(Warningbuffer)
                )
                f.close()
                await channel.send(file=File('/home/SE/ErrorsAndWarnings.txt'))



def setup(client):
    client.add_cog(analysis(client))
