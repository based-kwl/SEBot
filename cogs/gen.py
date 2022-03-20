import discord
from discord.ext import commands, tasks
from discord import File
import time
import asyncio
from itertools import cycle
from itertools import islice
import itertools
import random

class generator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gen(self, ctx):
        em1 = discord.Embed(
            description='Preset 1 - Diffuse Nebula (Emission Madness)\nPreset 2 - Diffuse Nebula (Dusty Cave)\nPreset 3 - Diffuse Nebula (Balanced, as all things should be.)\nPreset 4 - Planetary (Spherical)\nPreset 5 - Planetary (Lobed) --DOES NOT EXIST YET--\nPreset 6 - SNR (Spherical) --DOES NOT EXIST YET--\nPreset 7 - SNR (Lobed) --DOES NOT EXIST YET--\nPreset 8 - All',
            title='Type the preset (1-4 or 8) you wish to use. Type "cancel" to cancel. Presets 5-7 do not exist yet.',
            color=0x1e73e3
        )
        em1.set_footer(text='Generator made by Phunnie.')
        em2 = discord.Embed(
            title='Action cancelled. Type ".gen" to try again.',
            color=0x1e73e3
        )
        em3 = discord.Embed(
            title='Not a valid preset. Type ".gen" to try again.',
            color=0x1e73e3
        )
        em4 = discord.Embed(
            title='Error, not a number. Type ".gen" to try again.',
            color=0x1e73e3
        )
        em5 = discord.Embed(
            title='How many do you want to generate (must be at least 2 and below 1000)?',
            color=0x1e73e3
        )
        em8 = discord.Embed(
            title='Which color palette do you want?',
            description='Color palette 1 - random\nColor palette 2 - Hydrogen(reddish)\nColor palette 3 - SHO(orangeish and blue)\nColor palette 4 - HOO (red/blue)\nColor palette 5 - Realistic\n6 - Use all except random\n7 - Use Custom Palette',
            color=0x1e73e3
        )
        em7 = discord.Embed(
            title='Must be under 1000. Type ".gen" to try again.',
            color=0x1e73e3
        )
        em6 = discord.Embed(
            title='Must be at least 2. Type ".gen" to try again.',
            color=0x1e73e3
        )
        em9 = discord.Embed(
            title='Not a valid color preset. Type ".gen" to try again.',
            color=0x1e73e3
        )
        em10 = discord.Embed(
            title='Do you want with dust? (y/n)',
            color=0x1e73e3
        )
        em99 = discord.Embed(
            title='Request timed out. Type ".gen" to try again.',
            color=0x1e73e3
        )

        message = ctx.message
        msgm = ctx.channel
        user = ctx.message.author
        channel = ctx.channel
        channel1 = 'bots-and-voice'
        channel1get = self.client.get_channel(217142893440270346)
        if ctx.message.content.startswith('.gen'):
            try:
                await message.delete()
            except:
                print("ok")
            f = open("nebula-raymarch.cfg", "w+")
            preset = ''
            totalA = 1
            totalB = 1
            totalC = 1
            totalD = 1
            totalE = 1
            totalF = 1
            totalG = 1
            # thickA = ['-1.5', '-1', '-0.5', '0', '0.5']
            # thickB = ['-3', '-2.5', '-2', '-1.5', '-1', '-0.5', '0']
            tf = ['true', 'false']
            msg = await channel.send(embed=em1)
            def check(message):
                return message.author == ctx.author and message.channel == msgm
            try:
                ansp = await self.client.wait_for('message', check=check, timeout=30)
            except:
                await msg.edit(embed=em99)
                return
            preset = ansp.content
            await asyncio.sleep(0.5)
            try:
                await ansp.delete()
            except:
                print('ok')
            try:
                if preset == 'cancel':
                    await msg.edit(embed=em2)
                    return
                int(preset)
                if int(preset) < 1 or int(preset) > 8:
                    await msg.edit(embed=em3)
                    return
                if int(preset) >= 5 and int(preset) <= 7:
                    await msg.edit(embed=em3)
                    return
            except:
                await msg.edit(embed=em4)
                return
            count = 0
            await msg.edit(embed=em5)
            def check(message):
                return message.author == ctx.author and message.channel == msgm
            try:
                ansb = await self.client.wait_for('message', check=check, timeout=30)
            except:
                await msg.edit(embed=em99)
                return
            count = ansb.content
            await asyncio.sleep(0.5)
            try:
                await ansb.delete()
            except:
                print("ok")
            try:
                int(count)
                if int(count) < 2:
                    await msg.edit(embed=em6)
                    return
                if int(count) > 1000:
                    await msg.edit(embed=em7)
                    return
            except ValueError:
                await msg.edit(embed=em4)
                return
            if int(preset) >= 1 and int(preset) <= 8:
                bufferA = ''
                bufferB = ''
                bufferC = ''
                bufferD = ''
                bufferE = ''
                bufferF = ''
                bufferG = ''
                await msg.edit(embed=em8)
                def check(message):
                    return message.author == ctx.author and message.channel == msgm

                try:
                    ansc = await self.client.wait_for('message', check=check, timeout=30)
                except:
                    await msg.edit(embed=em99)
                    return
                color = ansc.content
                await asyncio.sleep(0.5)
                try:
                    await ansc.delete()
                except:
                    print('ok')
                try:
                    int(color)
                    if int(color) < 1 or int(color) > 7:
                        await msg.edit(embed=em9)
                        return
                except:
                    await msg.edit(embed=em2)
                    return
                if int(color) == 7:
                    em12 = discord.Embed(
                        title='Enter the number (1 or 2)',
                        description="1 - Saved palettes\n2 - Create new palette",
                        color=0x1e73e3
                    )
                    await msg.edit(embed=em12)
                    def check(message):
                        return message.author == ctx.author and message.channel == msgm

                    try:
                        anse = await self.client.wait_for('message', check=check, timeout=30)
                    except:
                        await msg.edit(embed=em99)
                        return
                    customc = anse.content
                    await asyncio.sleep(0.5)
                    try:
                        await anse.delete()
                    except:
                        print('ok')
                    if int(customc) == 2:
                        em999 = discord.Embed(
                            title='Enter a name for your new preset.',
                            color=0x1e73e3
                        )
                        await msg.edit(embed=em999)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            anse = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        presetname = anse.content
                        await asyncio.sleep(0.5)
                        try:
                            await anse.delete()
                        except:
                            print('ok')
                        em13 = discord.Embed(
                            title="Enter the R values for the first color.",
                            color=0x1e73e3
                        )
                        await msg.edit(embed=em13)
                        def check(message):
                            return message.author == ctx.author and message.channel == msgm
                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        R1 = ansf.content
                        if R1 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        em14 = discord.Embed(
                            title="Enter how much the value varies up and down. Note: The total (R,G,B) ± variation cannot exceed 1 or go below 0.",
                            color=0x1e73e3
                        )
                        await msg.edit(embed=em14)
                        def check(message):
                            return message.author == ctx.author and message.channel == msgm
                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        VR1 = ansf.content
                        if VR1 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        em15 = discord.Embed(
                            title="Enter the G values for the first color.",
                            color=0x1e73e3
                        )
                        await msg.edit(embed=em15)
                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        G1 = ansf.content
                        if G1 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        await msg.edit(embed=em14)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        VG1 = ansf.content
                        if VG1 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        em16 = discord.Embed(
                            title="Enter the B values for the first color.",
                            color=0x1e73e3
                        )
                        await msg.edit(embed=em16)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        B1 = ansf.content
                        if B1 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        await msg.edit(embed=em14)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        VB1 = ansf.content
                        if VB1 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        em17 = discord.Embed(
                            title="Enter the R values for the second color.",
                            color=0x1e73e3
                        )
                        await msg.edit(embed=em17)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        R2 = ansf.content
                        if R2 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        await msg.edit(embed=em14)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        VR2 = ansf.content
                        if VR2 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        em18 = discord.Embed(
                            title="Enter the G values for the second color.",
                            color=0x1e73e3
                        )
                        await msg.edit(embed=em18)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        G2 = ansf.content
                        if G2 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        await msg.edit(embed=em14)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        VG2 = ansf.content
                        if VG2 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        em19 = discord.Embed(
                            title="Enter the B values for the second color.",
                            color=0x1e73e3
                        )
                        await msg.edit(embed=em19)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        B2 = ansf.content
                        if B2 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        await msg.edit(embed=em14)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        VB2 = ansf.content
                        if VB2 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        em20 = discord.Embed(
                            title="Enter the R values for the third color.",
                            color=0x1e73e3
                        )
                        await msg.edit(embed=em20)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        R3 = ansf.content
                        if R3 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        await msg.edit(embed=em14)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        VR3 = ansf.content
                        if VR3 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        em21 = discord.Embed(
                            title="Enter the G values for the third color.",
                            color=0x1e73e3
                        )
                        await msg.edit(embed=em21)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        G3 = ansf.content
                        if G3 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        await msg.edit(embed=em14)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        VG3 = ansf.content
                        if VG3 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        em22 = discord.Embed(
                            title="Enter the B values for the third color.",
                            color=0x1e73e3
                        )
                        await msg.edit(embed=em22)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        B3 = ansf.content
                        if B3 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        await msg.edit(embed=em14)

                        def check(message):
                            return message.author == ctx.author and message.channel == msgm

                        try:
                            ansf = await self.client.wait_for('message', check=check, timeout=30)
                        except:
                            await msg.edit(embed=em99)
                            return
                        VB3 = ansf.content
                        if VB3 == 'cancel':
                            await msg.edit(embed=em2)
                            return
                        await asyncio.sleep(0.5)
                        try:
                            await ansf.delete()
                        except:
                            print('ok')
                        em23 = discord.Embed(
                            title='Palette saved.',
                            color=0x1e73e3
                        )
                        await msg.edit(embed=em23)
                        f1 = open(str(user) + ".txt", "a+")
                        f1.write(str(presetname) + "\n" +
                                 str(R1) + "\n" +
                                 str(VR1) + "\n" +
                                 str(G1) + "\n" +
                                 str(VG1) + '\n' +
                                 str(B1) + '\n' +
                                 str(VB1) + '\n' +
                                 str(R2) + '\n' +
                                 str(VR2) + '\n' +
                                 str(G2) + '\n' +
                                 str(VG2) + '\n' +
                                 str(B2) + '\n' +
                                 str(VB2) + '\n' +
                                 str(R3) + '\n' +
                                 str(VR3) + '\n' +
                                 str(G3) + '\n' +
                                 str(VG3) + '\n' +
                                 str(B3) + '\n' +
                                 str(VB3) + '\n'
                                            '-\n')
                        f1.close()
                    if int(customc) == 1:
                        buffercolor = ''
                        try:
                            f1 = open(str(user) + ".txt", 'r')
                            i = 1
                            for line in islice(f1, 0, None, 20):
                                buffercolor += str(i) + " - " + str(line)
                                i += 1
                            em22 = discord.Embed(
                                title='Choose:',
                                description=str(buffercolor),
                                color=0x1e73e3
                            )
                            await msg.edit(embed=em22)

                            def check(message):
                                return message.author == ctx.author and message.channel == msgm

                            try:
                                ansf = await self.client.wait_for('message', check=check, timeout=30)
                            except:
                                await msg.edit(embed=em99)
                                return
                            chosenp = ansf.content
                            try:
                                int(chosenp)
                                if int(chosenp) > i:
                                    await msg.edit(embed=em3)
                                    return
                            except:
                                await msg.edit(embed=em4)
                            await asyncio.sleep(0.5)
                            try:
                                await ansf.delete()
                            except:
                                print('ok')

                            f1.close()
                        except:
                            em23 = discord.Embed(
                                title='You have not made a preset yet. Type .gen to try again.',
                                color=0x1e73e3
                            )
                            await msg.edit(embed=em23)

                        f2 = open(str(user) + ".txt", 'r')
                        x = int(chosenp) + 19 * (int(chosenp) - 1)
                        lines = f2.readlines()
                        R1 = lines[int(x)]
                        VR1 = lines[int(x) + 1]
                        G1 = lines[int(x) + 2]
                        VG1 = lines[int(x) + 3]
                        B1 = lines[int(x) + 4]
                        VB1 = lines[int(x) + 5]
                        R2 = lines[int(x) + 6]
                        VR2 = lines[int(x) + 7]
                        G2 = lines[int(x) + 8]
                        VG2 = lines[int(x) + 9]
                        B2 = lines[int(x) + 10]
                        VB2 = lines[int(x) + 11]
                        R3 = lines[int(x) + 12]
                        VR3 = lines[int(x) + 13]
                        G3 = lines[int(x) + 14]
                        VG3 = lines[int(x) + 15]
                        B3 = lines[int(x) + 16]
                        VB3 = lines[int(x) + 17]
                        f2.close()
                await msg.edit(embed=em10)
                def check(message):
                    return message.author == ctx.author and message.channel == msgm

                try:
                    ansd = await self.client.wait_for('message', check=check, timeout=30)
                except:
                    await msg.edit(embed=em99)
                    return
                dust = ansd.content
                await asyncio.sleep(0.5)
                try:
                    await ansd.delete()
                except:
                    print('ok')
                print(dust)
                if dust == "y" or dust == "n":
                    if int(preset) == 1 or int(preset) == 8:  # Preset 1
                        for i in range(totalA, totalA + int(count)):
                            bufferA += (
                                    'CustomModel "Phunnie Diff A' + str(i) + '"\n'
                                                                             "{\n"
                                                                             "\tUseForType\t\t\"Nebula/Diffuse\"\n"
                                                                             "\n"
                                                                             "\tEnableImpostors  true\n"
                                                                             "\tEnableDepthTest  false\n"
                                                                             "\tEnableDepthWrite false\n"
                                                                             "\tEnableBlend      true\n"
                                                                             "\n"
                                                                             "\tShader           \"nebula_raymarch.glsl\"\n"
                                                                             "\tShaderUniforms   \"nebula_raymarch_uniforms.cfg\"\n"
                                                                             "\n"
                                                                             "\tBaseShape      \"box\"\n"
                                                                             "\tBaseShapeDims  (18 18 18)\n"
                                                                             "\tScale          (1 1 1)\n"
                                                                             "\tRandomize      (" + str(
                                random.uniform(-1, 1)) + " " + str(random.uniform(-1, 1)) + " " + str(
                                random.uniform(-1, 1)) + ")\n"
                                                         "\tBright          2\n"
                                                         "\tParticleColor  (0.952393 0.390625 1)\n"
                                                         "\n"
                                                         "\t//Dust volume parametrization\n"
                                                         "\tDust_enabled true\n")
                            if dust == "y":
                                bufferA += ("\tDust_volume_height " + str(random.uniform(1, 10)) + "\n")
                            if dust == 'n':
                                bufferA += ("\tDust_volume_height 1\n")
                            bufferA += (
                                "\tdust_absorption_factor 0.4\n"
                                "\tdust_scattering_factor 0.6\n")
                            if dust == 'y':
                                bufferA += ("\tDust_volume_density_factor " + str(random.uniform(0.5, 5)) + "\n")
                            if dust == 'n':
                                bufferA += ("\tDust_volume_density_factor 0.01\n")
                            bufferA += (
                                    "\tAlbedo 0.6\n"
                                    "\n"
                                    "\t//Scale\n"
                                    "\tInternal_scale 18\n"
                                    "\t//Raymarcher\n"
                                    "\tRaymarch_step_count 256\n"
                                    "\ttd_break_value 2.5\n"
                                    "\tsum_transparency_break (0.01 0.01 0.01)\n"
                                    "\t//Lights & Stars\n"
                                    "\tLight_intensivity 0\n"
                                    "\tLight_Color_11 (0.97 0.97 1)\n"
                                    "\tLight_radius_single_star 18.5\n"
                                    "\tAmbient_Light_intensivity " + str(random.uniform(0.2, 0.5)) + "\n"
                                                                                                     "\tAmbient_Light_Color_11 (0.97 0.97 1)\n"
                                                                                                     "\n"
                                                                                                     "\tSingle_star false\n"
                                                                                                     "\tStar_position (0 0 0)\n"
                                                                                                     "\tstar_empty_sphere_radius 1.5\n"
                                                                                                     "\tStar_field_scale 0.5\n"
                                                                                                     "\n"
                                                                                                     "\tRender_star false\n"
                                                                                                     "\tStar_light_coef_1 3.1405\n"
                                                                                                     "\tStar_light_coef_2 500\n"
                                                                                                     "\tRender_star_bloom false\n"
                                                                                                     "\tBloom_light_coef_1 0.075\n"
                                                                                                     "\tBloom_light_coef_2 500\n"
                                                                                                     "\n"
                                                                                                     "\t//HG phase function\n"
                                                                                                     "\tForward_scattering_g 0.6\n"
                                                                                                     "\tBackward_scattering_g -0.05\n"
                                                                                                     "\tHG_mix_coef 0.75\n"
                                                                                                     "\n"
                                                                                                     "\t//Emission\n"
                                                                                                     "\tGas_emission_enabled true\n"
                                                                                                     "\tGas_volume_height 1\n"
                                                                                                     "\tgas_scattering_factor 0.025\n"
                                                                                                     "\tgas_density_factor 0.1\n"
                                                                                                     "\tEmission_gas_1 true\n"
                                                                                                     "\t//Emission_gas_1_external true\n")
                            if int(color) == 1:  # random
                                bufferA += ("\tNebula_emission_color_1 (" + str(random.uniform(0, 1)) + " " + str(
                                    random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                            if int(color) == 2:  # Ha
                                bufferA += ("\tNebula_emission_color_1 (0.811 " + str(
                                    random.uniform(0.25, 0.55)) + " 0.236)\n")
                            if int(color) == 3:  # SHO
                                bufferA += ("\tNebula_emission_color_1 (0.926 " + str(
                                    random.uniform(0.400, 0.600)) + " 0.137)\n")
                            if int(color) == 4:  # HOO
                                bufferA += ("\tNebula_emission_color_1 (0.938 " + str(
                                    random.uniform(0, 0.2)) + " 0.100)\n")
                            if int(color) == 7:  # custom
                                bufferA += ("\tNebula_emission_color_1 (" + str(
                                    random.uniform(float(R1) - float(VR1), float(R1) + float(VR1))) + " " + str(
                                    random.uniform(float(G1) - float(VG1), float(G1) + float(VG1))) + " " + str(
                                    random.uniform(float(B1) - float(VB1), float(B1) + float(VB1))) + ")\n")
                            if int(color) == 5:  # realistic
                                dict = {
                                    1: "\tNebula_emission_color_1 (0.953 " + str(
                                        random.uniform(0.3, 0.55)) + " 0.328)\n",
                                    2: "\tNebula_emission_color_1 (0.883 " + str(
                                        random.uniform(0.49, 0.55)) + " 0.490)\n",
                                    3: "\tNebula_emission_color_1 (0.585 0.232 " + str(random.uniform(0.4, 0.6)) + ")\n"
                                }
                                r = random.randint(1, 3)
                                bufferA += dict[r]
                            if int(color) == 6:  # all except random
                                dicte = {
                                    1: "\tNebula_emission_color_1 (0.811 " + str(
                                        random.uniform(0.25, 0.55)) + " 0.236)\n",
                                    2: "\tNebula_emission_color_1 (0.926 " + str(
                                        random.uniform(0.400, 0.600)) + " 0.137)\n",
                                    3: "\tNebula_emission_color_1 (0.938 " + str(random.uniform(0, 0.2)) + " 0.100)\n"
                                }
                                e = random.randint(1, 4)
                                if e == 4:
                                    dict = {
                                        1: "\tNebula_emission_color_1 (0.953 " + str(
                                            random.uniform(0.3, 0.55)) + " 0.328)\n",
                                        2: "\tNebula_emission_color_1 (0.883 " + str(
                                            random.uniform(0.49, 0.55)) + " 0.490)\n",
                                        3: "\tNebula_emission_color_1 (0.585 0.232 " + str(
                                            random.uniform(0.4, 0.6)) + ")\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferA += dict[r]
                                else:
                                    bufferA += dicte[e]
                            bufferA += ("\tEmission_gas_1_direction (0 0 1)\n"
                                        "\tEmission_gas_1_coef_0 (0 0 0)\n"
                                        "\tEmission_gas_1_coef_1 0.140496\n"
                                        "\tEmission_gas_1_coef_2 3.96694\n"
                                        "\tEmission_gas_1_coef_3 0.75\n"
                                        "\tEmission_gas_2 true\n"
                                        "\t//Emission_gas_2_external false\n")
                            if int(color) == 1:
                                bufferA += ("\tNebula_emission_color_2 (" + str(random.uniform(0, 1)) + " " + str(
                                    random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                            if int(color) == 2:
                                bufferA += ("\tNebula_emission_color_2 (0.917969 0.179291 " + str(
                                    random.uniform(0.25, 0.55)) + ")\n")
                            if int(color) == 3:
                                bufferA += ("\tNebula_emission_color_2 (0.898 " + str(
                                    random.uniform(0.5, 0.7)) + " 0.467)\n")
                            if int(color) == 4:
                                bufferA += ("\tNebula_emission_color_2 (0.844 " + str(
                                    random.uniform(0.450, 0.650)) + " 0.488)\n")
                            if int(color) == 7:
                                bufferA += ("\tNebula_emission_color_2 (" + str(
                                    random.uniform(float(R2) - float(VR2), float(R2) + float(VR2))) + " " + str(
                                    random.uniform(float(G2) - float(VG2), float(G2) + float(VG2))) + " " + str(
                                    random.uniform(float(B2) - float(VB2), float(B2) + float(VB2))) + ")\n")
                            if int(color) == 5:
                                dict = {
                                    1: "\tNebula_emission_color_2 (" + str(
                                        random.uniform(0.55, 0.7)) + " 0.424 0.738)\n",
                                    2: "\tNebula_emission_color_2 (0.746 0.280 " + str(
                                        random.uniform(0.35, 0.65)) + ")\n",
                                    3: "\tNebula_emission_color_2 (0.746 " + str(
                                        random.uniform(0.28, 0.4)) + " 0.280)\n"
                                }
                                r = random.randint(1, 3)
                                bufferA += dict[r]
                            if int(color) == 6:
                                dicte = {
                                    1: "\tNebula_emission_color_2 (0.917969 0.179291 " + str(
                                        random.uniform(0.25, 0.55)) + ")\n",
                                    2: "\tNebula_emission_color_2 (0.898 " + str(
                                        random.uniform(0.5, 0.7)) + " 0.467)\n",
                                    3: "\tNebula_emission_color_2 (0.844 " + str(
                                        random.uniform(0.450, 0.650)) + " 0.488)\n"
                                }
                                e = random.randint(1, 4)
                                if e == 4:
                                    dict = {
                                        1: "\tNebula_emission_color_2 (" + str(
                                            random.uniform(0.55, 0.7)) + " 0.424 0.738)\n",
                                        2: "\tNebula_emission_color_2 (0.785 0.347 " + str(
                                            random.uniform(0.35, 0.65)) + ")\n",
                                        3: "\tNebula_emission_color_2 (0.746 " + str(
                                            random.uniform(0.28, 0.4)) + " 0.280)\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferA += dict[r]
                                else:
                                    bufferA += dicte[e]
                            bufferA += (
                                    "\tEmission_gas_2_direction (0 1 0)\n"
                                    "\tEmission_gas_2_coef_0 (0 1 0)\n"
                                    "\tEmission_gas_2_coef_1 0.446281\n"
                                    "\tEmission_gas_2_coef_2 " + str(random.uniform(1.2, 1.8)) + "\n"
                                                                                                 "\tEmission_gas_2_coef_3 1.364\n"
                                                                                                 "\tEmission_gas_3 true\n"
                                                                                                 "\t//Emission_gas_3_external false\n")
                            if int(color) == 1:
                                bufferA += ("\tNebula_emission_color_3 (" + str(random.uniform(0, 1)) + " " + str(
                                    random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                            if int(color) == 2:
                                bufferA += ("\tNebula_emission_color_3 (" + str(random.uniform(0.7, 0.9)) + " " + str(
                                    random.uniform(0.75, 0.9)) + " 0.533)\n")
                            if int(color) == 3:
                                bufferA += ("\tNebula_emission_color_3 (0.276 " + str(
                                    random.uniform(0.600, 0.800)) + " 0.906)\n")
                            if int(color) == 4:
                                bufferA += ("\tNebula_emission_color_3 (0.088 " + str(
                                    random.uniform(0.55, 0.7)) + " 0.863)\n")
                            if int(color) == 7:
                                bufferA += ("\tNebula_emission_color_3 (" + str(
                                    random.uniform(float(R3) - float(VR3), float(R3) + float(VR3))) + " " + str(
                                    random.uniform(float(G3) - float(VG3), float(G3) + float(VG3))) + " " + str(
                                    random.uniform(float(B3) - float(VB3), float(B3) + float(VB3))) + ")\n")
                            if int(color) == 5:
                                dict = {
                                    1: "\tNebula_emission_color_3 (0.358 " + str(
                                        random.uniform(0.6, 0.9)) + " 0.926)\n",
                                    2: "\tNebula_emission_color_3 (0.125 " + str(
                                        random.uniform(0.3, 0.45)) + " 0.46)\n",
                                    3: "\tNebula_emission_color_3 (0.67 0.297 " + str(random.uniform(0.3, 0.45)) + ")\n"
                                }
                                r = random.randint(1, 3)
                                bufferA += dict[r]
                            if int(color) == 6:
                                dicte = {
                                    1: "\tNebula_emission_color_3 (" + str(random.uniform(0.7, 0.9)) + " " + str(
                                        random.uniform(0.75, 0.9)) + " 0.533)\n",
                                    2: "\tNebula_emission_color_3 (0.276 " + str(
                                        random.uniform(0.600, 0.800)) + " 0.906)\n",
                                    3: "\tNebula_emission_color_3 (0.088 " + str(
                                        random.uniform(0.55, 0.7)) + " 0.863)\n"
                                }
                                e = random.randint(1, 4)
                                if e == 4:
                                    dict = {
                                        1: "\tNebula_emission_color_3 (0.358 " + str(
                                            random.uniform(0.6, 0.9)) + " 0.926)\n",
                                        2: "\tNebula_emission_color_3 (0.125 " + str(
                                            random.uniform(0.3, 0.45)) + " 0.46)\n",
                                        3: "\tNebula_emission_color_3 (0.67 0.297 " + str(
                                            random.uniform(0.3, 0.45)) + ")\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferA += dict[r]
                                else:
                                    bufferA += dicte[e]
                            bufferA += ("\tEmission_gas_3_direction (0 1 0)\n"
                                        "\tEmission_gas_3_coef_0 (0 0 0.5)\n"
                                        "\tEmission_gas_3_coef_1 0.35\n"
                                        "\tEmission_gas_3_coef_2 " + str(random.uniform(0.8, 1.1)) + "\n"
                                                                                                     "\tEmission_gas_3_coef_3 " + str(
                                random.uniform(1.3, 1.5)) + "\n"
                                                            "\n"
                                                            "\tEmission_intensivity_coef 80\n"
                                                            "\n"
                                                            "\tNebulaCentPos (0 0 0)\n"
                                                            "\n"
                                                            "\t// SCALE\n"
                                                            "\tNebScaleAbsBoth false\n"
                                                            "\tNebScaleAbsX true\n"
                                                            "\tNebScaleAbsY false\n"
                                                            "\tNebScale 1\n"
                                                            "\tNebScaleCoef (2 2)\n"
                                                            "\n"
                                                            "\t// Spiral noise\n"
                                                            "\tSpirNoiseNudge (" + str(
                                random.uniform(0, 10)) + " " + str(random.uniform(0, 10)) + ")\n"
                                                                                            "\tSpirNoiseAmount (-1 -1)\n")
                            noiseiter = random.uniform(1.5, 2.2)
                            bufferA += (
                                    "\tSpirNoiseIter (" + str(noiseiter) + " " + str(noiseiter) + ")\n")
                            noisecoef = random.uniform(1.4, 2.3)
                            bufferA += (
                                    "\tSpirNoiseCoef (" + str(noisecoef) + " " + str(noisecoef) + ")\n"
                                                                                                  "\t//Spiral Noise 3D\n"
                                                                                                  "\tNudge_3D_2 (0.739513 0.739513)\n"
                                                                                                  "\tNoise_amount_3D_2 (0 0)\n"
                                                                                                  "\tFrequency_iteration_count_3D_2 (1 1)\n"
                                                                                                  "\tSpirNoise3DCoef_2 (1.53373 1.53373)\n"
                                                                                                  "\n"
                                                                                                  "\t// FORM\n"
                                                                                                  "\tNebulaFormPlane false\n"
                                                                                                  "\tNebulaFormPlaneSign (1 1)\n"
                                                                                                  "\tNebulaFormPlaneXYZ (0 1 0)\n"
                                                                                                  "\tNebulaFormPlaneHeight 7\n"
                                                                                                  "\n"
                                                                                                  "\tNebulaFormDsk true\n"
                                                                                                  "\tNebulaFormDskSign (-0.1 -0.1)\n"
                                                                                                  "\tNebulaFormDskParam (" + str(
                                random.uniform(0, 10)) + " " + str(random.uniform(0, 10)) + " " + str(
                                random.uniform(0, 10)) + ")\n"
                                                         "\n"
                                                         "\tNebulaFormCyl false\n"
                                                         "\tNebulaFormCylSign (-1 -1)\n"
                                                         "\tNebulaFormCylParam (3 5)\n"
                                                         "\n"
                                                         "\tNebulaFormSph true\n"
                                                         "\tNebulaFormSphSign (1.1157 1.1157)\n"
                                                         "\tNebulaFormSphRad " + str(random.uniform(2, 5)) + "\n"
                                                                                                             "\n"
                                                                                                             "\tNebulaFormCapsule false\n"  # + str(random.choice(tf)) + "\n"
                                                                                                             "\tNebulaFormCapsuleSign (2 2)\n"
                                                                                                             "\tNebulaFormCapsulePos_1 (" + str(
                                random.uniform(-10, 10)) + " " + str(random.uniform(-10, 10)) + " " + str(
                                random.uniform(-10, 10)) + ")\n"
                                                           "\tNebulaFormCapsulePos_2 (" + str(
                                random.uniform(-10, 10)) + " " + str(random.uniform(-10, 10)) + " " + str(
                                random.uniform(-10, 10)) + ")\n"
                                                           "\tNebulaFormCapsuleRadius 8\n"
                                                           "\n"
                                                           "\tNebulaFormTorus " + str(random.choice(tf)) + "\n")
                            TorusSign = random.uniform(-0.5, 0)
                            bufferA += ("\tNebulaFormTorusSign (" + str(TorusSign) + " " + str(TorusSign) + ")\n"
                                                                                                            "\tNebulaFormTorusRadius_1 " + str(
                                random.uniform(0, 10)) + "\n"
                                                         "\tNebulaFormTorusRadius_2 10\n"
                                                         "\n"
                                                         "\tNebulaFormSpir " + str(random.choice(tf)) + "\n"
                                                                                                        "\tNebulaFormSpirSign (0.1 0.1)\n"
                                                                                                        "\tNebulaFormSpirParam (" + str(
                                random.uniform(0, 5)) + " " + str(random.uniform(0.5, 2)) + " " + str(
                                random.uniform(1, 3)) + " " + str(random.uniform(0, 1)) + ")\n"
                                                                                          "\n"
                                                                                          "\tNebulaFormNoise " + str(
                                random.choice(tf)) + "\n"
                                                     "\tNebulaFormNoiseSign (0.2066 0.2066)\n"
                                                     "\tNebulaFormNoiseCoef1 " + str(random.uniform(0, 3)) + "\n"
                                                                                                             "\tNebulaFormNoiseCoef2 " + str(
                                random.uniform(0, 5)) + "\n"
                                                        "\n"
                                                        "\tNebulaFormFBMNoise " + str(random.choice(tf)) + "\n")
                            FBMNoise = random.uniform(-1.5, 1.5)
                            bufferA += ("\tNebulaFormFBMNoiseSign (" + str(FBMNoise) + " " + str(FBMNoise) + ")\n"
                                                                                                             "\tNebulaFormFBMNoiseCoef 40\n"
                                                                                                             "\n"
                                                                                                             "\tNebulaFormSpirNoise false\n"
                                                                                                             "\tNebulaFormSpirNoiseSign (-0.5 -0.5)\n"
                                                                                                             "\tNebulaFormSpirNoiseCoef1 0.3123\n"
                                                                                                             "\tNebulaFormSpirNoiseCoef2 100\n"
                                                                                                             "\tNebulaFormSpirNoiseCoef3 2\n"
                                                                                                             "\n"
                                                                                                             "\tNebulaFormSpirIQNoise true\n"
                                                                                                             "\tNebulaFormSpirIQNoiseSign (1.25 1.25)\n"
                                                                                                             "\tNebulaFormSpirIQNoiseCoef1 0.4123\n"
                                                                                                             "\tNebulaFormSpirIQNoiseCoef2 " + str(
                                random.uniform(0, 1000)) + "\n"
                                                           "\tNebulaFormSpirIQNoiseCoef3 4.5\n"
                                                           "\tNebulaFormSpirIQNoiseCoef4 " + str(
                                random.uniform(2, 5)) + "\n"
                                                        "\n"
                                                        "\tNebulaFormSpirNoise3D false\n"
                                                        "\tNebulaFormSpirNoise3DSign (1 1)\n"
                                                        "\tNebulaFormSpirNoise3DCoef 1\n"
                                                        "\n"
                                                        "\t// Map\n"
                                                        "\tNebulaMapTwist false\n"
                                                        "\tNebulaMapTwistCoef1 0.25\n"
                                                        "\tNebulaMapTwistCoef2 0.15\n"
                                                        "\n"
                                                        "\tNebulaMapThickCoef (" + str(
                                random.uniform(-0.5, 1)) + " 0.2)\n"
                                                           "\tExpansionBegin\t2.451545000000000e+06\n"
                                                           "\tExpansionDuration\t0.000000000000000e+00\n"
                                                           "}\n")
                        f.write(bufferA)
                        totalA += int(count)

                    if int(preset) == 2 or int(preset) == 8:  # Preset 2
                        for i in range(totalB, totalB + int(count)):
                            rand = random.randint(0, 1)
                            if rand == 1:
                                bufferB += ("\n"
                                            'CustomModel  "Phunnie Diff B' + str(i) + '"\n'
                                                                                      "{\n"
                                                                                      "\tUseForType\t\t\"Nebula/Diffuse\"\n"
                                                                                      "\n"
                                                                                      "\tEnableImpostors  true\n"
                                                                                      "\tEnableDepthTest  false\n"
                                                                                      "\tEnableDepthWrite false\n"
                                                                                      "\tEnableBlend      true\n"
                                                                                      "\n"
                                                                                      "\tShader           \"nebula_raymarch.glsl\"\n"
                                                                                      "\tShaderUniforms   \"nebula_raymarch_uniforms.cfg\"\n"
                                                                                      "\n"
                                                                                      "\n"
                                                                                      "\tBaseShape      \"box\"\n"
                                                                                      "\tBaseShapeDims  (30 30 30)\n"
                                                                                      "\tScale          (1 1 1)\n"
                                                                                      "\tBright          2\n"
                                                                                      "\n"
                                                                                      "\t//Dust volume parametrization\n"
                                                                                      "\tDust_enabled true\n")
                                if dust == "y":
                                    bufferB += ("\tDust_volume_height " + str(random.uniform(1, 10)) + "\n")
                                if dust == 'n':
                                    bufferB += ("\tDust_volume_height 1\n")
                                bufferB += (
                                    "\tdust_absorption_factor 0.4\n"
                                    "\tdust_scattering_factor 0.6\n")
                                if dust == 'y':
                                    bufferB += ("\tDust_volume_density_factor " + str(random.uniform(0.5, 10)) + "\n")
                                if dust == 'n':
                                    bufferB += ("\tDust_volume_density_factor 0.01\n")
                                bufferB += (
                                    "\tAlbedo 0.6\n"
                                    "\n"
                                    "\t//Scale\n"
                                    "\tInternal_scale 30\n"
                                    "\t//Raymarcher\n"
                                    "\tRaymarch_step_count 256\n"
                                    "\ttd_break_value 2.5\n"
                                    "\tsum_transparency_break (0 0.01 0.01)\n"
                                    "\t//Lights & Stars\n"
                                    "\tLight_intensivity 0\n"
                                    "\tLight_Color_11 (0.66449 0.711667 0.746094)\n"
                                    "\tLight_radius_single_star 12.0661\n"
                                    "\tAmbient_Light_intensivity " + str(random.uniform(0.2, 1.5)) + "\n"
                                    "\tAmbient_Light_Color_11 (0.717285 0.836258 0.882813)\n"
                                    "\n"
                                    "\tSingle_star false\n"
                                    "\tStar_position (2.47934 0 6.61157)\n"
                                    "\tstar_empty_sphere_radius 0\n"
                                    "\tStar_field_scale 1\n"
                                    "\n"
                                    "\tRender_star false\n"
                                    "\tStar_light_coef_1 1.65289\n"
                                    "\tStar_light_coef_2 578.512\n"
                                    "\tRender_star_bloom false\n"
                                    "\tBloom_light_coef_1 0.0165289\n"
                                    "\tBloom_light_coef_2 413.223\n"
                                    "\n"
                                    "\t//HG phase function\n"
                                    "\tForward_scattering_g 0.6\n"
                                    "\tBackward_scattering_g -0.05\n"
                                    "\tHG_mix_coef 0.75\n"
                                    "\n"
                                    "\t//Emission\n"
                                    "\tGas_emission_enabled true\n"
                                    "\tGas_volume_height 5\n"
                                    "\tgas_scattering_factor 0.025\n"
                                    "\tgas_density_factor 0.1\n"
                                    "\tEmission_gas_1 true\n"
                                    "\t//Emission_gas_1_external true\n")
                                if int(color) == 1:
                                    bufferB += ("\tNebula_emission_color_1 (" + str(random.uniform(0, 1)) + " " + str(
                                        random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                                if int(color) == 2:
                                    bufferB += ("\tNebula_emission_color_1 (0.811 " + str(
                                        random.uniform(0.25, 0.55)) + " 0.236)\n")
                                if int(color) == 3:
                                    bufferB += ("\tNebula_emission_color_1 (0.926 " + str(
                                        random.uniform(0.400, 0.600)) + " 0.137)\n")
                                if int(color) == 4:
                                    bufferB += ("\tNebula_emission_color_1 (0.938 " + str(
                                        random.uniform(0, 0.2)) + " 0.100)\n")
                                if int(color) == 7:
                                    bufferB += ("\tNebula_emission_color_1 (" + str(
                                        random.uniform(float(R1) - float(VR1), float(R1) + float(VR1))) + " " + str(
                                        random.uniform(float(G1) - float(VG1), float(G1) + float(VG1))) + " " + str(
                                        random.uniform(float(B1) - float(VB1), float(B1) + float(VB1))) + ")\n")
                                if int(color) == 5:  # realistic
                                    dict = {
                                        1: "\tNebula_emission_color_1 (0.953 " + str(
                                            random.uniform(0.3, 0.55)) + " 0.328)\n",
                                        2: "\tNebula_emission_color_1 (0.883 " + str(
                                            random.uniform(0.49, 0.55)) + " 0.490)\n",
                                        3: "\tNebula_emission_color_1 (0.585 0.232 " + str(random.uniform(0.4, 0.6)) + ")\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferB += dict[r]
                                if int(color) == 6:  # all except random
                                    dicte = {
                                        1: "\tNebula_emission_color_1 (0.811 " + str(
                                            random.uniform(0.25, 0.55)) + " 0.236)\n",
                                        2: "\tNebula_emission_color_1 (0.926 " + str(
                                            random.uniform(0.400, 0.600)) + " 0.137)\n",
                                        3: "\tNebula_emission_color_1 (0.938 " + str(random.uniform(0, 0.2)) + " 0.100)\n"
                                    }
                                    e = random.randint(1, 4)
                                    if e == 4:
                                        dict = {
                                            1: "\tNebula_emission_color_1 (0.953 " + str(
                                                random.uniform(0.3, 0.55)) + " 0.328)\n",
                                            2: "\tNebula_emission_color_1 (0.883 " + str(
                                                random.uniform(0.49, 0.55)) + " 0.490)\n",
                                            3: "\tNebula_emission_color_1 (0.585 0.232 " + str(
                                                random.uniform(0.4, 0.6)) + ")\n"
                                        }
                                        r = random.randint(1, 3)
                                        bufferB += dict[r]
                                    else:
                                        bufferB += dicte[e]
                                bufferB += (
                                    "\tEmission_gas_1_direction (0.14876 0.247934 0)\n"
                                    "\tEmission_gas_1_coef_0 (4.2562 0.53719 0.867769)\n"
                                    "\tEmission_gas_1_coef_1 0.0909091\n"
                                    "\tEmission_gas_1_coef_2 1.28099\n"
                                    "\tEmission_gas_1_coef_3 2.19008\n"
                                    "\tEmission_gas_2 true\n"
                                    "\t//Emission_gas_2_external false\n")
                                if int(color) == 1:
                                    bufferB += ("\tNebula_emission_color_2 (" + str(random.uniform(0, 1)) + " " + str(
                                        random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                                if int(color) == 2:
                                    bufferB += ("\tNebula_emission_color_2 (0.917969 0.179291 " + str(
                                        random.uniform(0.25, 0.55)) + ")\n")
                                if int(color) == 3:
                                    bufferB += ("\tNebula_emission_color_2 (0.844 " + str(
                                        random.uniform(0.600, 0.800)) + " 0.488)\n")
                                if int(color) == 4:
                                    bufferB += ("\tNebula_emission_color_2 (0.938 " + str(
                                        random.uniform(0, 0.2)) + " 0.100)\n")
                                if int(color) == 7:
                                    bufferB += ("\tNebula_emission_color_2 (" + str(
                                        random.uniform(float(R2) - float(VR2), float(R2) + float(VR2))) + " " + str(
                                        random.uniform(float(G2) - float(VG2), float(G2) + float(VG2))) + " " + str(
                                        random.uniform(float(B2) - float(VB2), float(B2) + float(VB2))) + ")\n")
                                if int(color) == 5:
                                    dict = {
                                        1: "\tNebula_emission_color_2 (" + str(
                                            random.uniform(0.55, 0.7)) + " 0.424 0.738)\n",
                                        2: "\tNebula_emission_color_2 (0.746 0.280 " + str(
                                            random.uniform(0.35, 0.65)) + ")\n",
                                        3: "\tNebula_emission_color_2 (0.746 " + str(
                                            random.uniform(0.28, 0.4)) + " 0.280)\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferB += dict[r]
                                if int(color) == 6:
                                    dicte = {
                                        1: "\tNebula_emission_color_2 (0.917969 0.179291 " + str(
                                            random.uniform(0.25, 0.55)) + ")\n",
                                        2: "\tNebula_emission_color_2 (0.898 " + str(
                                            random.uniform(0.5, 0.7)) + " 0.467)\n",
                                        3: "\tNebula_emission_color_2 (0.844 " + str(
                                            random.uniform(0.450, 0.650)) + " 0.488)\n"
                                    }
                                    e = random.randint(1, 4)
                                    if e == 4:
                                        dict = {
                                            1: "\tNebula_emission_color_2 (" + str(
                                                random.uniform(0.55, 0.7)) + " 0.424 0.738)\n",
                                            2: "\tNebula_emission_color_2 (0.785 0.347 " + str(
                                                random.uniform(0.35, 0.65)) + ")\n",
                                            3: "\tNebula_emission_color_2 (0.746 " + str(
                                                random.uniform(0.28, 0.4)) + " 0.280)\n"
                                        }
                                        r = random.randint(1, 3)
                                        bufferB += dict[r]
                                    else:
                                        bufferB += dicte[e]
                                bufferB += (
                                    "\tEmission_gas_2_direction (0.77686 0 0)\n"
                                    "\tEmission_gas_2_coef_0 (4.58678 -0.619835 -0.702479)\n"
                                    "\tEmission_gas_2_coef_1 0.0909091\n"
                                    "\tEmission_gas_2_coef_2 1.1157\n"
                                    "\tEmission_gas_2_coef_3 0.867769\n"
                                    "\tEmission_gas_3 true\n"
                                    "\t//Emission_gas_3_external false\n")
                                if int(color) == 1:
                                    bufferB += ("\tNebula_emission_color_3 (" + str(random.uniform(0, 1)) + " " + str(
                                        random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                                if int(color) == 2:
                                    bufferB += ("\tNebula_emission_color_3 (0.793 " + str(
                                        random.uniform(0.5, 0.8)) + " 0.533)\n")
                                if int(color) == 3:
                                    bufferB += ("\tNebula_emission_color_3 (0.276 " + str(
                                        random.uniform(0.600, 0.800)) + " 0.906)\n")
                                if int(color) == 4:
                                    bufferB += ("\tNebula_emission_color_3 (0.276 " + str(
                                        random.uniform(0.600, 0.800)) + " 0.906)\n")
                                if int(color) == 7:
                                    bufferB += ("\tNebula_emission_color_3 (" + str(
                                        random.uniform(float(R3) - float(VR3), float(R3) + float(VR3))) + " " + str(
                                        random.uniform(float(G3) - float(VG3), float(G3) + float(VG3))) + " " + str(
                                        random.uniform(float(B3) - float(VB3), float(B3) + float(VB3))) + ")\n")
                                if int(color) == 5:
                                    dict = {
                                        1: "\tNebula_emission_color_3 (0.358 " + str(
                                            random.uniform(0.6, 0.9)) + " 0.926)\n",
                                        2: "\tNebula_emission_color_3 (0.125 " + str(
                                            random.uniform(0.3, 0.45)) + " 0.46)\n",
                                        3: "\tNebula_emission_color_3 (0.67 0.297 " + str(random.uniform(0.3, 0.45)) + ")\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferB += dict[r]
                                if int(color) == 6:
                                    dicte = {
                                        1: "\tNebula_emission_color_3 (" + str(random.uniform(0.7, 0.9)) + " " + str(
                                            random.uniform(0.75, 0.9)) + " 0.533)\n",
                                        2: "\tNebula_emission_color_3 (0.276 " + str(
                                            random.uniform(0.600, 0.800)) + " 0.906)\n",
                                        3: "\tNebula_emission_color_3 (0.088 " + str(
                                            random.uniform(0.55, 0.7)) + " 0.863)\n"
                                    }
                                    e = random.randint(1, 4)
                                    if e == 4:
                                        dict = {
                                            1: "\tNebula_emission_color_3 (0.358 " + str(
                                                random.uniform(0.6, 0.9)) + " 0.926)\n",
                                            2: "\tNebula_emission_color_3 (0.125 " + str(
                                                random.uniform(0.3, 0.45)) + " 0.46)\n",
                                            3: "\tNebula_emission_color_3 (0.67 0.297 " + str(
                                                random.uniform(0.3, 0.45)) + ")\n"
                                        }
                                        r = random.randint(1, 3)
                                        bufferB += dict[r]
                                    else:
                                        bufferB += dicte[e]
                                bufferB += (
                                        "\tEmission_gas_3_direction (0 0 0.479339)\n"
                                        "\tEmission_gas_3_coef_0 (5 3.34711 5)\n"
                                        "\tEmission_gas_3_coef_1 0.00826446\n"
                                        "\tEmission_gas_3_coef_2 0.578512\n"
                                        "\tEmission_gas_3_coef_3 0.826446\n"
                                        "\n"
                                        "\tEmission_intensivity_coef 100\n"
                                        "\n"
                                        "\tNebulaCentPos (0 1 0)\n"
                                        "\n"
                                        "\t// SCALE\n"
                                        "\tNebScaleAbsBoth false\n"
                                        "\tNebScaleAbsX true\n"
                                        "\tNebScaleAbsY false\n"
                                        "\tNebScale 2.31405\n"
                                        "\tNebScaleCoef (-20.1653 -20.8264)\n"
                                        "\n"
                                        "\t// Spiral noise\n"
                                        "\tSpirNoiseNudge (" + str(
                                random.uniform(0, 10)) + " " + str(random.uniform(0, 10)) + ")\n"
                                                                                            "\tSpirNoiseAmount (-1 -1)\n")
                            noiseiter = random.uniform(1.5, 2.2)
                            bufferB += (
                                    "\tSpirNoiseIter (" + str(noiseiter) + " " + str(noiseiter) + ")\n")
                            noisecoef = random.uniform(1.4, 2.3)
                            bufferB += (
                                    "\tSpirNoiseCoef (" + str(noisecoef) + " " + str(noisecoef) + ")\n"
                                                            "\t//Spiral Noise 3D\n"
                                                            "\tNudge_3D_2 (0.739513 0.739513)\n"
                                                            "\tNoise_amount_3D_2 (0 0)\n"
                                                            "\tFrequency_iteration_count_3D_2 (1 1)\n"
                                                            "\tSpirNoise3DCoef_2 (1.53373 1.53373)\n"
                                                            "\n"
                                                            "\t// FORM\n"
                                                            "\tNebulaFormPlane false\n"
                                                            "\tNebulaFormPlaneSign (-0.0413222 -0.0413222)\n"
                                                            "\tNebulaFormPlaneXYZ (0 0.743802 0.578512)\n"
                                                            "\tNebulaFormPlaneHeight 4.71074\n"
                                                            "\n"
                                                            "\tNebulaFormDsk true\n"
                                                            "\tNebulaFormDskSign (1.03306 1.03306)\n"
                                                            "\tNebulaFormDskParam (" + str(
                                    random.uniform(0, 2)) + " " + str(random.uniform(0, 2)) + " " + str(
                                    random.uniform(0, 2)) + ")\n"
                                                            "\n"
                                                            "\tNebulaFormCyl false\n"
                                                            "\tNebulaFormCylSign (-1.03306 -2.43802)\n"
                                                            "\tNebulaFormCylParam (3 5)\n"
                                                            "\n"
                                                            "\tNebulaFormSph false\n"
                                                            "\tNebulaFormSphSign (-1.69421 -1.69421)\n"
                                                            "\tNebulaFormSphRad 5.3719\n"
                                                            "\n"
                                                            "\tNebulaFormCapsule false\n"
                                                            "\tNebulaFormCapsuleSign (0.0413222 0.0413222)\n"
                                                            "\tNebulaFormCapsulePos_1 (3.1405 -3.47108 -1.81818)\n"
                                                            "\tNebulaFormCapsulePos_2 (-7.10744 2.14876 5.78512)\n"
                                                            "\tNebulaFormCapsuleRadius 23.1405\n"
                                                            "\n"
                                                            "\tNebulaFormTorus true\n"
                                                            "\tNebulaFormTorusSign (-0.123967 -0.123967)\n"
                                                            "\tNebulaFormTorusRadius_1 37.6033\n"
                                                            "\tNebulaFormTorusRadius_2 26.0331\n"
                                                            "\n"
                                                            "\tNebulaFormSpir false\n"
                                                            "\tNebulaFormSpirSign (0.785124 0.785124)\n"
                                                            "\tNebulaFormSpirParam (3.6 3 0.5 0.7)\n"
                                                            "\n"
                                                            "\tNebulaFormNoise true\n"
                                                            "\tNebulaFormNoiseSign (0.0413222 0.0413222)\n"
                                                            "\tNebulaFormNoiseCoef1 " + str(random.uniform(0, 3)) + "\n"
                                                                                                                    "\tNebulaFormNoiseCoef2 " + str(
                                    random.uniform(0, 5)) + "\n"
                                                            "\n"
                                                            "\tNebulaFormFBMNoise true\n"
                                                            "\tNebulaFormFBMNoiseSign (" + str(
                                    random.uniform(-4, -1)) + " " + str(random.uniform(-5, -0.5)) + ")\n"
                                                                                                    "\tNebulaFormFBMNoiseCoef " + str(
                                    random.uniform(0, 30)) + "\n"
                                                               "\n"
                                                               "\tNebulaFormSpirNoise true\n"
                                                               "\tNebulaFormSpirNoiseSign (-0.5 -0.5)\n"
                                                               "\tNebulaFormSpirNoiseCoef1 0.15\n"
                                                               "\tNebulaFormSpirNoiseCoef2 (" + str(
                                    random.uniform(0, 1000)) + ")\n"
                                                               "\tNebulaFormSpirNoiseCoef3 6.19835\n"
                                                               "\n"
                                                               "\tNebulaFormSpirIQNoise false\n"
                                                               "\tNebulaFormSpirIQNoiseSign (-1 -1)\n"
                                                               "\tNebulaFormSpirIQNoiseCoef1 0.3123\n"
                                                               "\tNebulaFormSpirIQNoiseCoef2 100\n"
                                                               "\tNebulaFormSpirIQNoiseCoef3 3\n"
                                                               "\tNebulaFormSpirIQNoiseCoef4 2.5\n"
                                                               "\n"
                                                               "\tNebulaFormSpirNoise3D false\n"
                                                               "\tNebulaFormSpirNoise3DSign (-1.1157 -0.53719)\n"
                                                               "\tNebulaFormSpirNoise3DCoef 1\n"
                                                               "\n"
                                                               "\t// Map\n"
                                                               "\tNebulaMapTwist true\n"
                                                               "\tNebulaMapTwistCoef1 0\n"
                                                               "\tNebulaMapTwistCoef2 0\n"
                                                               "\n"
                                                               "\tNebulaMapThickCoef (" + str(
                                    random.uniform(-4, 1)) + " -1.19835)\n"
                                                             "\n"
                                                             "\tRandomize      (" + str(random.uniform(-1, 1)) + " " + str(
                                    random.uniform(-1, 1)) + " " + str(random.uniform(-1, 1)) + ")\n"
                                                                                                "\tParticleColor\t(0.535156, 0.0648041, 0.0648041)\n"
                                                                                                "\tExpansionBegin\t2.451545000000000e+06\n"
                                                                                                "\tExpansionDuration\t0.000000000000000e+00\n"
                                                                                                "}")
                            if rand == 0:
                                bufferB += ("\n"'CustomModel  "PhunnieL Diff B' + str(i) +'"\n'
                                          "{\n"
                                          "\tUseForType\t\t\"Nebula/Diffuse\"\n"
                                          "\n"
                                          "\tEnableImpostors  true\n"
                                          "\tEnableDepthTest  false\n"
                                          "\tEnableDepthWrite false\n"
                                          "\tEnableBlend      true\n"
                                          "\n"
                                          "\tShader           \"nebula_raymarch.glsl\"\n"
                                          "\tShaderUniforms   \"nebula_raymarch_uniforms.cfg\"\n"
                                          "\n"
                                          "\tBaseShape      \"box\"\n"
                                          "\tBaseShapeDims  (20 " + str(random.uniform(12, 20)) + " 20)\n"
                                          "\tScale          (1 1 1)\n"
                                          "\tRandomize      (0 0 0)\n"
                                          "\tBright          2\n"
                                          "\tParticleColor  (1 0.617188 0.724853)\n"
                                          "\n"
                                          "\t//Dust volume parametrization\n"
                                          "\tDust_enabled true\n")
                                if dust == "y":
                                    bufferB += ("\tDust_volume_height " + str(random.uniform(4, 10)) + "\n")
                                if dust == 'n':
                                    bufferB += ("\tDust_volume_height 1\n")
                                bufferB += (
                                    "\tdust_absorption_factor 0.4\n"
                                    "\tdust_scattering_factor 0.6\n")
                                if dust == 'y':
                                    bufferB += ("\tDust_volume_density_factor " + str(random.uniform(0.5, 10)) + "\n")
                                if dust == 'n':
                                    bufferB += ("\tDust_volume_density_factor 0.01\n")
                                bufferB += (
                                          "\tAlbedo 0.6\n"
                                          "\n"
                                          "\t//Scale\n"
                                          "\tInternal_scale 20\n"
                                          "\t//Raymarcher\n"
                                          "\tRaymarch_step_count 256\n"
                                          "\ttd_break_value 2.5\n"
                                          "\tsum_transparency_break (0.01 0.01 0.01)\n"
                                          "\t//Lights & Stars\n"
                                          "\tLight_intensivity 0.330579\n"
                                          "\tLight_Color_11 (0.97 0.97 1)\n"
                                          "\tLight_radius_single_star 18.5\n"
                                          "\tAmbient_Light_intensivity 0.289256\n"
                                          "\tAmbient_Light_Color_11 (0.97 0.97 1)\n"
                                          "\n"
                                          "\tSingle_star false\n"
                                          "\tStar_position (0 0 0)\n"
                                          "\tstar_empty_sphere_radius 1.5\n"
                                          "\tStar_field_scale 0.5\n"
                                          "\n"
                                          "\tRender_star false\n"
                                          "\tStar_light_coef_1 3.1405\n"
                                          "\tStar_light_coef_2 500\n"
                                          "\tRender_star_bloom true\n"
                                          "\tBloom_light_coef_1 0.00826446\n"
                                          "\tBloom_light_coef_2 330.579\n"
                                          "\n"
                                          "\t//HG phase function\n"
                                          "\tForward_scattering_g 0.6\n"
                                          "\tBackward_scattering_g -0.05\n"
                                          "\tHG_mix_coef 0.75\n"
                                          "\n"
                                          "\t//Emission\n"
                                        "\tGas_emission_enabled true\n"
                                        "\tGas_volume_height 1\n"
                                        "\tgas_scattering_factor 0.025\n"
                                        "\tgas_density_factor 0.1\n"
                                        "\tEmission_gas_1 true\n"
                                        "\t//Emission_gas_1_external true\n")
                                if int(color) == 1:  # random
                                    bufferB += ("\tNebula_emission_color_1 (" + str(random.uniform(0, 1)) + " " + str(
                                        random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                                if int(color) == 2:  # Ha
                                    bufferB += ("\tNebula_emission_color_1 (0.811 " + str(
                                        random.uniform(0.25, 0.55)) + " 0.236)\n")
                                if int(color) == 3:  # SHO
                                    bufferB += ("\tNebula_emission_color_1 (0.926 " + str(
                                        random.uniform(0.400, 0.600)) + " 0.137)\n")
                                if int(color) == 4:  # HOO
                                    bufferB += ("\tNebula_emission_color_1 (0.938 " + str(
                                        random.uniform(0, 0.2)) + " 0.100)\n")
                                if int(color) == 7:  # custom
                                    bufferB += ("\tNebula_emission_color_1 (" + str(
                                        random.uniform(float(R1) - float(VR1), float(R1) + float(VR1))) + " " + str(
                                        random.uniform(float(G1) - float(VG1), float(G1) + float(VG1))) + " " + str(
                                        random.uniform(float(B1) - float(VB1), float(B1) + float(VB1))) + ")\n")
                                if int(color) == 5:  # realistic
                                    dict = {
                                        1: "\tNebula_emission_color_1 (0.953 " + str(
                                            random.uniform(0.3, 0.55)) + " 0.328)\n",
                                        2: "\tNebula_emission_color_1 (0.883 " + str(
                                            random.uniform(0.49, 0.55)) + " 0.490)\n",
                                        3: "\tNebula_emission_color_1 (0.585 0.232 " + str(random.uniform(0.4, 0.6)) + ")\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferB += dict[r]
                                if int(color) == 6:  # all except random
                                    dicte = {
                                        1: "\tNebula_emission_color_1 (0.811 " + str(
                                            random.uniform(0.25, 0.55)) + " 0.236)\n",
                                        2: "\tNebula_emission_color_1 (0.926 " + str(
                                            random.uniform(0.400, 0.600)) + " 0.137)\n",
                                        3: "\tNebula_emission_color_1 (0.938 " + str(random.uniform(0, 0.2)) + " 0.100)\n"
                                    }
                                    e = random.randint(1, 4)
                                    if e == 4:
                                        dict = {
                                            1: "\tNebula_emission_color_1 (0.953 " + str(
                                                random.uniform(0.3, 0.55)) + " 0.328)\n",
                                            2: "\tNebula_emission_color_1 (0.883 " + str(
                                                random.uniform(0.49, 0.55)) + " 0.490)\n",
                                            3: "\tNebula_emission_color_1 (0.585 0.232 " + str(
                                                random.uniform(0.4, 0.6)) + ")\n"
                                        }
                                        r = random.randint(1, 3)
                                        bufferB += dict[r]
                                    else:
                                        bufferB += dicte[e]
                                bufferB += (
                                        "\tEmission_gas_1_direction (0 0 1)\n"
                                        "\tEmission_gas_1_coef_0 (0 0 0)\n"
                                        "\tEmission_gas_1_coef_1 0.124\n"
                                        "\tEmission_gas_1_coef_2 3.306\n"
                                        "\tEmission_gas_1_coef_3 0.2893\n"
                                        "\tEmission_gas_2 true\n"
                                        "\t//Emission_gas_2_external false\n")
                                if int(color) == 1:
                                    bufferB += ("\tNebula_emission_color_2 (" + str(random.uniform(0, 1)) + " " + str(
                                        random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                                if int(color) == 2:
                                    bufferB += ("\tNebula_emission_color_2 (0.917969 0.179291 " + str(
                                        random.uniform(0.25, 0.55)) + ")\n")
                                if int(color) == 3:
                                    bufferB += ("\tNebula_emission_color_2 (0.844 " + str(
                                        random.uniform(0.600, 0.800)) + " 0.488)\n")
                                if int(color) == 4:
                                    bufferB += ("\tNebula_emission_color_2 (0.938 " + str(
                                        random.uniform(0, 0.2)) + " 0.100)\n")
                                if int(color) == 7:
                                    bufferB += ("\tNebula_emission_color_2 (" + str(
                                        random.uniform(float(R2) - float(VR2), float(R2) + float(VR2))) + " " + str(
                                        random.uniform(float(G2) - float(VG2), float(G2) + float(VG2))) + " " + str(
                                        random.uniform(float(B2) - float(VB2), float(B2) + float(VB2))) + ")\n")
                                if int(color) == 5:
                                    dict = {
                                        1: "\tNebula_emission_color_2 (" + str(
                                            random.uniform(0.55, 0.7)) + " 0.424 0.738)\n",
                                        2: "\tNebula_emission_color_2 (0.746 0.280 " + str(
                                            random.uniform(0.35, 0.65)) + ")\n",
                                        3: "\tNebula_emission_color_2 (0.746 " + str(
                                            random.uniform(0.28, 0.4)) + " 0.280)\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferB += dict[r]
                                if int(color) == 6:
                                    dicte = {
                                        1: "\tNebula_emission_color_2 (0.917969 0.179291 " + str(
                                            random.uniform(0.25, 0.55)) + ")\n",
                                        2: "\tNebula_emission_color_2 (0.898 " + str(
                                            random.uniform(0.5, 0.7)) + " 0.467)\n",
                                        3: "\tNebula_emission_color_2 (0.844 " + str(
                                            random.uniform(0.450, 0.650)) + " 0.488)\n"
                                    }
                                    e = random.randint(1, 4)
                                    if e == 4:
                                        dict = {
                                            1: "\tNebula_emission_color_2 (" + str(
                                                random.uniform(0.55, 0.7)) + " 0.424 0.738)\n",
                                            2: "\tNebula_emission_color_2 (0.785 0.347 " + str(
                                                random.uniform(0.35, 0.65)) + ")\n",
                                            3: "\tNebula_emission_color_2 (0.746 " + str(
                                                random.uniform(0.28, 0.4)) + " 0.280)\n"
                                        }
                                        r = random.randint(1, 3)
                                        bufferB += dict[r]
                                    else:
                                        bufferB += dicte[e]
                                bufferB += (
                                        "\tEmission_gas_2_direction (0 1 0)\n"
                                        "\tEmission_gas_2_coef_0 (0 1 0)\n"
                                        "\tEmission_gas_2_coef_1 0.2645\n"
                                        "\tEmission_gas_2_coef_2 0.6612\n"
                                        "\tEmission_gas_2_coef_3 1.57\n"
                                        "\tEmission_gas_3 true\n"
                                        "\t//Emission_gas_3_external false\n")
                                if int(color) == 1:
                                    bufferB += ("\tNebula_emission_color_3 (" + str(random.uniform(0, 1)) + " " + str(
                                        random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                                if int(color) == 2:
                                    bufferB += ("\tNebula_emission_color_3 (0.793 " + str(
                                        random.uniform(0.5, 0.8)) + " 0.533)\n")
                                if int(color) == 3:
                                    bufferB += ("\tNebula_emission_color_3 (0.276 " + str(
                                        random.uniform(0.600, 0.800)) + " 0.906)\n")
                                if int(color) == 4:
                                    bufferB += ("\tNebula_emission_color_3 (0.276 " + str(
                                        random.uniform(0.600, 0.800)) + " 0.906)\n")
                                if int(color) == 7:
                                    bufferB += ("\tNebula_emission_color_3 (" + str(
                                        random.uniform(float(R3) - float(VR3), float(R3) + float(VR3))) + " " + str(
                                        random.uniform(float(G3) - float(VG3), float(G3) + float(VG3))) + " " + str(
                                        random.uniform(float(B3) - float(VB3), float(B3) + float(VB3))) + ")\n")
                                if int(color) == 5:
                                    dict = {
                                        1: "\tNebula_emission_color_3 (0.358 " + str(
                                            random.uniform(0.6, 0.9)) + " 0.926)\n",
                                        2: "\tNebula_emission_color_3 (0.125 " + str(
                                            random.uniform(0.3, 0.45)) + " 0.46)\n",
                                        3: "\tNebula_emission_color_3 (0.67 0.297 " + str(random.uniform(0.3, 0.45)) + ")\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferB += dict[r]
                                if int(color) == 6:
                                    dicte = {
                                        1: "\tNebula_emission_color_3 (" + str(random.uniform(0.7, 0.9)) + " " + str(
                                            random.uniform(0.75, 0.9)) + " 0.533)\n",
                                        2: "\tNebula_emission_color_3 (0.276 " + str(
                                            random.uniform(0.600, 0.800)) + " 0.906)\n",
                                        3: "\tNebula_emission_color_3 (0.088 " + str(
                                            random.uniform(0.55, 0.7)) + " 0.863)\n"
                                    }
                                    e = random.randint(1, 4)
                                    if e == 4:
                                        dict = {
                                            1: "\tNebula_emission_color_3 (0.358 " + str(
                                                random.uniform(0.6, 0.9)) + " 0.926)\n",
                                            2: "\tNebula_emission_color_3 (0.125 " + str(
                                                random.uniform(0.3, 0.45)) + " 0.46)\n",
                                            3: "\tNebula_emission_color_3 (0.67 0.297 " + str(
                                                random.uniform(0.3, 0.45)) + ")\n"
                                        }
                                        r = random.randint(1, 3)
                                        bufferB += dict[r]
                                    else:
                                        bufferB += dicte[e]
                                bufferB += (
                                        "\tEmission_gas_3_direction (0 1 0)\n"
                                        "\tEmission_gas_3_coef_0 (0 0 0.5)\n"
                                        "\tEmission_gas_3_coef_1 0.0413223\n"
                                        "\tEmission_gas_3_coef_2 0.53719\n"
                                        "\tEmission_gas_3_coef_3 0.950413\n"
                                          "\n"
                                          "\tEmission_intensivity_coef 80\n"
                                          "\n"
                                          "\tNebulaCentPos (0 0 0)\n"
                                          "\n"
                                          "\t// SCALE\n"
                                          "\tNebScaleAbsBoth false\n"
                                          "\tNebScaleAbsX true\n"
                                          "\tNebScaleAbsY false\n"
                                          "\tNebScale 1\n"
                                          "\tNebScaleCoef (2 2)\n"
                                          "\n"
                                          "\t// Spiral noise\n"
                                          "\tSpirNoiseNudge (" + str(random.uniform(2, 8)) + " " + str(random.uniform(2, 8)) + ")\n")
                            noiseamt = random.uniform(-1.7, -1)
                            noiseamtB = noiseamt/2 - random.uniform(0, 0.5)
                            bufferB += (
                                    "\tSpirNoiseAmount (" + str(noiseamt) + " " + str(noiseamtB) + ")\n")
                            noisecoef = random.uniform(1.4, 2.3)
                            bufferB += (
                                    "\tSpirNoiseIter (1.69 1.69)\n"
                                    "\tSpirNoiseCoef (" + str(noisecoef) + " " + str(noisecoef) + ")\n"
                                                            "\t//Spiral Noise 3D\n"
                                          "\tNudge_3D_2 (0.739513 0.739513)\n"
                                          "\tNoise_amount_3D_2 (0 0)\n"
                                          "\tFrequency_iteration_count_3D_2 (1 1)\n"
                                          "\tSpirNoise3DCoef_2 (1.53373 1.53373)\n"
                                          "\n"
                                          "\t// FORM\n"
                                          "\tNebulaFormPlane false\n"
                                          "\tNebulaFormPlaneSign (1 1)\n"
                                          "\tNebulaFormPlaneXYZ (0 1 0)\n"
                                          "\tNebulaFormPlaneHeight 7\n"
                                          "\n"
                                          "\tNebulaFormDsk true\n"
                                          "\tNebulaFormDskSign (-0.1 -0.1)\n"
                                          "\tNebulaFormDskParam (" + str(random.uniform(0, 10)) + " " + str(random.uniform(0, 10)) + " " + str(random.uniform(0, 10)) + ")\n"
                                          "\n"
                                          "\tNebulaFormCyl false\n"
                                          "\tNebulaFormCylSign (-1 -1)\n"
                                          "\tNebulaFormCylParam (3 5)\n"
                                          "\n"
                                          "\tNebulaFormSph true\n"
                                          "\tNebulaFormSphSign (1.116 1.116)\n"
                                          "\tNebulaFormSphRad 2.89256\n"
                                          "\n"
                                          "\tNebulaFormCapsule false\n"
                                          "\tNebulaFormCapsuleSign (2 1.85)\n"
                                          "\tNebulaFormCapsulePos_1 (0 8 0)\n"
                                          "\tNebulaFormCapsulePos_2 (0 -12 0)\n"
                                          "\tNebulaFormCapsuleRadius 8\n"
                                          "\n"
                                          "\tNebulaFormTorus true\n"
                                          "\tNebulaFormTorusSign (-0.371901 -0.371901)\n"
                                          "\tNebulaFormTorusRadius_1 " + str(random.uniform(0, 10)) + "\n"
                                          "\tNebulaFormTorusRadius_2 " + str(random.uniform(3, 10)) + "\n"
                                          "\n"
                                          "\tNebulaFormSpir false\n"
                                          "\tNebulaFormSpirSign (1.25 1.25)\n"
                                          "\tNebulaFormSpirParam (3 2.1206 1.5 1)\n"
                                          "\n"
                                          "\tNebulaFormNoise true\n"
                                          "\tNebulaFormNoiseSign (0.289256 " + str(random.uniform(-0.5, 1)) + ")\n"
                                          "\tNebulaFormNoiseCoef1 5.61983\n"
                                          "\tNebulaFormNoiseCoef2 0.578512\n"
                                          "\n"
                                          "\tNebulaFormFBMNoise false\n"
                                          "\tNebulaFormFBMNoiseSign (1.1157 0.867769)\n"
                                          "\tNebulaFormFBMNoiseCoef 10\n"
                                          "\n"
                                          "\tNebulaFormSpirNoise false\n"
                                          "\tNebulaFormSpirNoiseSign (-0.5 -0.5)\n"
                                          "\tNebulaFormSpirNoiseCoef1 0.3123\n"
                                          "\tNebulaFormSpirNoiseCoef2 100\n"
                                          "\tNebulaFormSpirNoiseCoef3 2\n"
                                          "\n"
                                          "\tNebulaFormSpirIQNoise true\n"
                                          "\tNebulaFormSpirIQNoiseSign (1.25 1.25)\n"
                                          "\tNebulaFormSpirIQNoiseCoef1 0.4123\n"
                                          "\tNebulaFormSpirIQNoiseCoef2 " + str(random.uniform(0, 1000)) + "\n"
                                          "\tNebulaFormSpirIQNoiseCoef3 3.8\n"
                                          "\tNebulaFormSpirIQNoiseCoef4 " + str(random.uniform(2.5, 5)) + "\n"
                                          "\n"
                                          "\tNebulaFormSpirNoise3D false\n"
                                          "\tNebulaFormSpirNoise3DSign (0.123967 -0.123967)\n"
                                          "\tNebulaFormSpirNoise3DCoef 1.40496\n"
                                          "\n"
                                          "\t// Map\n"
                                          "\tNebulaMapTwist " + str(random.choice(tf)) + "\n"
                                          "\tNebulaMapTwistCoef1 0\n"
                                          "\tNebulaMapTwistCoef2 0.04dd\n"
                                          "\n"
                                          "\tNebulaMapThickCoef (" + str(random.uniform(-1.5, 0.2)) + " 0.2)\n"
                                          "\tExpansionBegin\t2.451545000000000e+06\n"
                                          "\tExpansionDuration\t0.000000000000000e+00\n"
                                          "}")
                        f.write(bufferB)
                        totalB += int(count)

                    if int(preset) == 3 or int(preset) == 8:  # Preset 3
                        for i in range(totalC, totalC + int(count)):
                            bufferC += ("\n"
                                        'CustomModel  "Phunnie Diff C' + str(i) + '"\n'
                                                                                  "{\n"
                                                                                  "\tUseForType\t\t\"Nebula/Diffuse\"\n"
                                                                                  "\n"
                                                                                  "\tEnableImpostors  true\n"
                                                                                  "\tEnableDepthTest  false\n"
                                                                                  "\tEnableDepthWrite false\n"
                                                                                  "\tEnableBlend      true\n"
                                                                                  "\n"
                                                                                  "\tShader           \"nebula_raymarch.glsl\"\n"
                                                                                  "\tShaderUniforms   \"nebula_raymarch_uniforms.cfg\"\n"
                                                                                  "\n"
                                                                                  "\tBaseShape      \"box\"\n"
                                                                                  "\tBaseShapeDims  (30 32 32)\n"
                                                                                  "\tScale          (1 1 1)\n"
                                                                                  "\tRandomize      (-0.305785 -0.38843 -0.140496)\n"
                                                                                  "\tBright          2\n"
                                                                                  "\tParticleColor  (1 0.47525 0.292969)\n"
                                                                                  "\n"
                                                                                  "\t//Dust volume parametrization\n"
                                                                                  "\tDust_enabled true\n")
                            if dust == "y":
                                bufferC += ("\tDust_volume_height " + str(random.uniform(2, 10)) + "\n")
                            if dust == 'n':
                                bufferC += ("\tDust_volume_height 1\n")
                            bufferC += (
                                "\tdust_absorption_factor 0.4\n"
                                "\tdust_scattering_factor 0.6\n")
                            if dust == 'y':
                                bufferC += ("\tDust_volume_density_factor " + str(random.uniform(0.5, 6)) + "\n")
                            if dust == 'n':
                                bufferC += ("\tDust_volume_density_factor 0.01\n")
                            bufferC += (
                                    "\tAlbedo 0.6\n"
                                    "\n"
                                    "\t//Scale\n"
                                    "\tInternal_scale 32\n"
                                    "\t//Raymarcher\n"
                                    "\tRaymarch_step_count 128\n"
                                    "\ttd_break_value 2.5\n"
                                    "\tsum_transparency_break (0.01 0.01 0.01)\n"
                                    "\t//Lights & Stars\n"
                                    "\tLight_intensivity 0\n"
                                    "\tLight_Color_11 (1 0.894531 0.894531)\n"
                                    "\tLight_radius_single_star 20\n"
                                    "\tAmbient_Light_intensivity " + str(random.uniform(0.2, 0.5)) + "\n"
                                                                                                     "\tAmbient_Light_Color_11 (0.836 0.536 0.536)\n"
                                                                                                     "\n"
                                                                                                     "\tSingle_star false\n"
                                                                                                     "\tStar_position (4.95868 0 0)\n"
                                                                                                     "\tstar_empty_sphere_radius 0\n"
                                                                                                     "\tStar_field_scale 0.550413\n"
                                                                                                     "\n"
                                                                                                     "\tRender_star false\n"
                                                                                                     "\tStar_light_coef_1 13.3884\n"
                                                                                                     "\tStar_light_coef_2 330.579\n"
                                                                                                     "\tRender_star_bloom false\n"
                                                                                                     "\tBloom_light_coef_1 0.0578512\n"
                                                                                                     "\tBloom_light_coef_2 578.512\n"
                                                                                                     "\n"
                                                                                                     "\t//HG phase function\n"
                                                                                                     "\tForward_scattering_g 0.6\n"
                                                                                                     "\tBackward_scattering_g -0.05\n"
                                                                                                     "\tHG_mix_coef 0.75\n"
                                                                                                     "\n"
                                                                                                     "\t//Emission\n"
                                                                                                     "\tGas_emission_enabled true\n"
                                                                                                     "\tGas_volume_height 1\n"
                                                                                                     "\tgas_scattering_factor 0.025\n"
                                                                                                     "\tgas_density_factor 0.1\n"
                                                                                                     "\tEmission_gas_1 true\n"
                                                                                                     "\t//Emission_gas_1_external true\n")
                            if int(color) == 1:
                                bufferC += ("\tNebula_emission_color_1 (" + str(random.uniform(0, 1)) + " " + str(
                                    random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                            if int(color) == 2:
                                bufferC += ("\tNebula_emission_color_1 (0.391 " + str(
                                    random.uniform(0.15, 0.3)) + " 0.124)\n")
                            if int(color) == 3:
                                bufferC += ("\tNebula_emission_color_1 (0.844 " + str(
                                    random.uniform(0.25, 0.4)) + " 0.099)\n")
                            if int(color) == 4:
                                bufferC += ("\tNebula_emission_color_1 (0.852 " + str(
                                    random.uniform(0.05, 0.3)) + " 0.06)\n")
                            if int(color) == 7:
                                bufferC += ("\tNebula_emission_color_1 (" + str(
                                    random.uniform(float(R1) - float(VR1), float(R1) + float(VR1))) + " " + str(
                                    random.uniform(float(G1) - float(VG1), float(G1) + float(VG1))) + " " + str(
                                    random.uniform(float(B1) - float(VB1), float(B1) + float(VB1))) + ")\n")
                            if int(color) == 5:  # realistic
                                dict = {
                                    1: "\tNebula_emission_color_1 (0.953 " + str(
                                        random.uniform(0.3, 0.55)) + " 0.328)\n",
                                    2: "\tNebula_emission_color_1 (0.883 " + str(
                                        random.uniform(0.49, 0.55)) + " 0.490)\n",
                                    3: "\tNebula_emission_color_1 (0.585 0.232 " + str(random.uniform(0.4, 0.6)) + ")\n"
                                }
                                r = random.randint(1, 3)
                                bufferC += dict[r]
                            if int(color) == 6:  # all except random
                                dicte = {
                                    1: "\tNebula_emission_color_1 (0.391 " + str(
                                        random.uniform(0.15, 0.3)) + " 0.124)\n",
                                    2: "\tNebula_emission_color_1 (0.844 " + str(
                                        random.uniform(0.25, 0.4)) + " 0.099)\n",
                                    3: "\tNebula_emission_color_1 (0.852 " + str(random.uniform(0.05, 0.3)) + " 0.06)\n"
                                }
                                e = random.randint(1, 4)
                                if e == 4:
                                    dict = {
                                        1: "\tNebula_emission_color_1 (0.953 " + str(
                                            random.uniform(0.3, 0.55)) + " 0.328)\n",
                                        2: "\tNebula_emission_color_1 (0.883 " + str(
                                            random.uniform(0.49, 0.55)) + " 0.490)\n",
                                        3: "\tNebula_emission_color_1 (0.585 0.232 " + str(
                                            random.uniform(0.4, 0.6)) + ")\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferC += dict[r]
                                else:
                                    bufferC += dicte[e]
                            bufferC += (
                                "\tEmission_gas_1_direction (0 0 1)\n"
                                "\tEmission_gas_1_coef_0 (0 0 0)\n"
                                "\tEmission_gas_1_coef_1 0.371901\n"
                                "\tEmission_gas_1_coef_2 3.058\n"
                                "\tEmission_gas_1_coef_3 1.23967\n"
                                "\tEmission_gas_2 true\n"
                                "\t//Emission_gas_2_external false\n")
                            if int(color) == 1:
                                bufferC += ("\tNebula_emission_color_2 (" + str(random.uniform(0, 1)) + " " + str(
                                    random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                            if int(color) == 2:
                                bufferC += ("\tNebula_emission_color_2 (0.917969 0.179291 " + str(
                                    random.uniform(0.25, 0.55)) + ")\n")
                            if int(color) == 3:
                                bufferC += ("\tNebula_emission_color_2 (" + str(
                                    random.uniform(0.550, 0.715)) + " " + str(random.uniform(0.45, 0.7)) + " 0.290)\n")
                            if int(color) == 4:
                                bufferC += ("\tNebula_emission_color_2 (0.625 " + str(
                                    random.uniform(0.180, 0.3)) + " 0.186)\n")
                            if int(color) == 7:
                                bufferC += ("\tNebula_emission_color_2 (" + str(
                                    random.uniform(float(R2) - float(VR2), float(R2) + float(VR2))) + " " + str(
                                    random.uniform(float(G2) - float(VG2), float(G2) + float(VG2))) + " " + str(
                                    random.uniform(float(B2) - float(VB2), float(B2) + float(VB2))) + ")\n")
                            if int(color) == 5:
                                dict = {
                                    1: "\tNebula_emission_color_2 (" + str(
                                        random.uniform(0.55, 0.7)) + " 0.424 0.738)\n",
                                    2: "\tNebula_emission_color_2 (0.746 0.280 " + str(
                                        random.uniform(0.35, 0.65)) + ")\n",
                                    3: "\tNebula_emission_color_2 (0.746 " + str(
                                        random.uniform(0.28, 0.4)) + " 0.280)\n"
                                }
                                r = random.randint(1, 3)
                                bufferC += dict[r]
                            if int(color) == 6:
                                dicte = {
                                    1: "\tNebula_emission_color_2 (0.917969 0.179291 " + str(
                                        random.uniform(0.25, 0.55)) + ")\n",
                                    2: "\tNebula_emission_color_2 (" + str(random.uniform(0.550, 0.715)) + " " + str(
                                        random.uniform(0.45, 0.7)) + " 0.290)\n",
                                    3: "\tNebula_emission_color_2 (0.625 " + str(
                                        random.uniform(0.180, 0.3)) + " 0.186)\n"
                                }
                                e = random.randint(1, 4)
                                if e == 4:
                                    dict = {
                                        1: "\tNebula_emission_color_2 (" + str(
                                            random.uniform(0.55, 0.7)) + " 0.424 0.738)\n",
                                        2: "\tNebula_emission_color_2 (0.785 0.347 " + str(
                                            random.uniform(0.35, 0.65)) + ")\n",
                                        3: "\tNebula_emission_color_2 (0.746 " + str(
                                            random.uniform(0.28, 0.4)) + " 0.280)\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferC += dict[r]
                                else:
                                    bufferC += dicte[e]
                            bufferC += (
                                "\tEmission_gas_2_direction (0 1 0)\n"
                                "\tEmission_gas_2_coef_0 (0 1.03306 0)\n"
                                "\tEmission_gas_2_coef_1 0.5868\n"
                                "\tEmission_gas_2_coef_2 1.074\n"
                                "\tEmission_gas_2_coef_3 1.57\n"
                                "\tEmission_gas_3 true\n"
                                "\t//Emission_gas_3_external false\n")
                            if int(color) == 1:
                                bufferC += ("\tNebula_emission_color_3 (" + str(random.uniform(0, 1)) + " " + str(
                                    random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                            if int(color) == 2:
                                bufferC += ("\tNebula_emission_color_3 (0.254 " + str(
                                    random.uniform(0.07, 0.175)) + " " + str(random.uniform(0.07, 0.175)) + ")\n")
                            if int(color) == 3:
                                bufferC += ("\tNebula_emission_color_3 (0 " + str(
                                    random.uniform(0.250, 0.450)) + " 0.600)\n")
                            if int(color) == 4:
                                bufferC += ("\tNebula_emission_color_3 (0.067 " + str(
                                    random.uniform(0.250, 0.450)) + " 0.613)\n")
                            if int(color) == 7:
                                bufferC += ("\tNebula_emission_color_3 (" + str(
                                    random.uniform(float(R3) - float(VR3), float(R3) + float(VR3))) + " " + str(
                                    random.uniform(float(G3) - float(VG3), float(G3) + float(VG3))) + " " + str(
                                    random.uniform(float(B3) - float(VB3), float(B3) + float(VB3))) + ")\n")
                            if int(color) == 5:
                                dict = {
                                    1: "\tNebula_emission_color_3 (0.358 " + str(
                                        random.uniform(0.6, 0.9)) + " 0.926)\n",
                                    2: "\tNebula_emission_color_3 (0.125 " + str(
                                        random.uniform(0.3, 0.45)) + " 0.46)\n",
                                    3: "\tNebula_emission_color_3 (0.67 0.297 " + str(random.uniform(0.3, 0.45)) + ")\n"
                                }
                                r = random.randint(1, 3)
                                bufferC += dict[r]
                            if int(color) == 6:
                                dicte = {
                                    1: "\tNebula_emission_color_3 (0.254 " + str(
                                        random.uniform(0.07, 0.175)) + " " + str(random.uniform(0.07, 0.175)) + ")\n",
                                    2: "\tNebula_emission_color_3 (0 " + str(
                                        random.uniform(0.250, 0.450)) + " 0.600)\n",
                                    3: "\tNebula_emission_color_3 (0.067 " + str(
                                        random.uniform(0.250, 0.450)) + " 0.613)\n"
                                }
                                e = random.randint(1, 4)
                                if e == 4:
                                    dict = {
                                        1: "\tNebula_emission_color_3 (0.358 " + str(
                                            random.uniform(0.6, 0.9)) + " 0.926)\n",
                                        2: "\tNebula_emission_color_3 (0.125 " + str(
                                            random.uniform(0.3, 0.45)) + " 0.46)\n",
                                        3: "\tNebula_emission_color_3 (0.67 0.297 " + str(
                                            random.uniform(0.3, 0.45)) + ")\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferC += dict[r]
                                else:
                                    bufferC += dicte[e]
                            bufferC += (
                                    "\tEmission_gas_3_direction (0 1 0)\n"
                                    "\tEmission_gas_3_coef_0 (0 0 0.5)\n"
                                    "\tEmission_gas_3_coef_1 0.380165\n"
                                    "\tEmission_gas_3_coef_2 " + str(random.uniform(0.8, 1)) + "\n"
                                                                                               "\tEmission_gas_3_coef_3 " + str(
                                random.uniform(1.25, 1.5)) + "\n"
                                                             "\n"
                                                             "\tEmission_intensivity_coef 80\n"
                                                             "\n"
                                                             "\tNebulaCentPos (0 0 0)\n"
                                                             "\n"
                                                             "\t// SCALE\n"
                                                             "\tNebScaleAbsBoth false\n"
                                                             "\tNebScaleAbsX true\n"
                                                             "\tNebScaleAbsY false\n"
                                                             "\tNebScale 1.32231\n"
                                                             "\tNebScaleCoef (0.991737 0.991737)\n"
                                                             "\n"
                                                             "\t// Spiral noise\n"
                                                             "\tSpirNoiseNudge (" + str(
                                random.uniform(3, 7)) + " " + str(random.uniform(3, 7)) + ")\n"
                                                                                          "\tSpirNoiseAmount (-1 -1)\n"
                                                                                          "\tSpirNoiseIter (2 2)\n"
                                                                                          "\tSpirNoiseCoef (1.73373 1.73373)\n"
                                                                                          "\t//Spiral Noise 3D\n"
                                                                                          "\tNudge_3D_2 (1.90083 1.90083)\n"
                                                                                          "\tNoise_amount_3D_2 (-1.90083 -3.22314)\n"
                                                                                          "\tFrequency_iteration_count_3D_2 (0.702479 2.56198)\n"
                                                                                          "\tSpirNoise3DCoef_2 (6.28099 6.19835)\n"
                                                                                          "\n"
                                                                                          "\t// FORM\n"
                                                                                          "\tNebulaFormPlane false\n"
                                                                                          "\tNebulaFormPlaneSign (1.03306 0.206612)\n"
                                                                                          "\tNebulaFormPlaneXYZ (0.909091 1 -0.413223)\n"
                                                                                          "\tNebulaFormPlaneHeight 0.0826445\n"
                                                                                          "\n")
                            DskSign = random.uniform(-0.2, 0.05)
                            bufferC += (
                                    "\tNebulaFormDsk " + str(random.choice(tf)) + "\n"
                                                                                  "\tNebulaFormDskSign (" + str(
                                DskSign) + " " + str(DskSign) + ")\n"
                                                                "\tNebulaFormDskParam (" + str(
                                random.uniform(0, 5)) + " " + str(random.uniform(0, 5)) + " " + str(
                                random.uniform(0, 5)) + ")\n"
                                                        "\n"
                                                        "\tNebulaFormCyl " + str(random.choice(tf)) + "\n"
                                                                                                      "\tNebulaFormCylSign (-0.785124 -0.785124)\n"
                                                                                                      "\tNebulaFormCylParam (" + str(
                                random.uniform(4, 8)) + " " + str(random.uniform(4, 15)) + ")\n"
                                                                                           "\n"
                                                                                           "\tNebulaFormSph true\n"
                                                                                           "\tNebulaFormSphSign (1.19835 1.19835)\n"
                                                                                           "\tNebulaFormSphRad " + str(
                                random.uniform(0, 0.5)) + "\n"
                                                          "\n"
                                                          "\tNebulaFormCapsule " + str(random.choice(tf)) + "\n"
                                                                                                            "\tNebulaFormCapsuleSign (0.206612 0.206612)\n"
                                                                                                            "\tNebulaFormCapsulePos_1 (-19.6694 -20 10.0826)\n"
                                                                                                            "\tNebulaFormCapsulePos_2 (20 -9.09091 5.45455)\n"
                                                                                                            "\tNebulaFormCapsuleRadius 22.4793\n"
                                                                                                            "\n"
                                                                                                            "\tNebulaFormTorus true\n"
                                                                                                            "\tNebulaFormTorusSign (-0.206612 -0.289256)\n"
                                                                                                            "\tNebulaFormTorusRadius_1 21.0744\n"
                                                                                                            "\tNebulaFormTorusRadius_2 " + str(
                                random.uniform(21, 28)) + "\n"
                                                          "\n"
                                                          "\tNebulaFormSpir false\n"
                                                          "\tNebulaFormSpirSign (0.0413223 -0.0413223)\n"
                                                          "\tNebulaFormSpirParam (1.98347 3.01653 1.07438 1)\n"
                                                          "\n"
                                                          "\tNebulaFormNoise true\n"
                                                          "\tNebulaFormNoiseSign (-0.2 -0.2)\n"
                                                          "\tNebulaFormNoiseCoef1 11.9008\n"
                                                          "\tNebulaFormNoiseCoef2 0.785124\n"
                                                          "\n")
                            FBMNoiseC = random.uniform(-3, 1)
                            bufferC += (
                                    "\tNebulaFormFBMNoise true\n"
                                    "\tNebulaFormFBMNoiseSign (" + str(FBMNoiseC) + " " + str(
                                FBMNoiseC + random.uniform(1, 3)) + ")\n"
                                                                    "\tNebulaFormFBMNoiseCoef " + str(
                                random.uniform(0, 20)) + "\n"
                                                         "\n"
                                                         "\tNebulaFormSpirNoise true\n"
                                                         "\tNebulaFormSpirNoiseSign (0.785124 0.785124)\n"
                                                         "\tNebulaFormSpirNoiseCoef1 " + str(
                                random.uniform(0, 0.5)) + "\n"
                                                          "\tNebulaFormSpirNoiseCoef2 " + str(
                                random.uniform(0, 1000)) + "\n"
                                                           "\tNebulaFormSpirNoiseCoef3 " + str(
                                random.uniform(0.4, 0.7)) + "\n"
                                                            "\n"
                                                            "\tNebulaFormSpirIQNoise true\n"
                                                            "\tNebulaFormSpirIQNoiseSign (1.1157 1.1157)\n"
                                                            "\tNebulaFormSpirIQNoiseCoef1 " + str(
                                random.uniform(0.4, 0.55)) + "\n"
                                                             "\tNebulaFormSpirIQNoiseCoef2 " + str(
                                random.uniform(0, 1000)) + "\n"
                                                           "\tNebulaFormSpirIQNoiseCoef3 4.46281\n"
                                                           "\tNebulaFormSpirIQNoiseCoef4 " + str(
                                random.uniform(1, 2.5)) + "\n"
                                                          "\n"
                                                          "\tNebulaFormSpirNoise3D false\n"
                                                          "\tNebulaFormSpirNoise3DSign (1 1)\n"
                                                          "\tNebulaFormSpirNoise3DCoef 1\n"
                                                          "\n"
                                                          "\t// Map\n"
                                                          "\tNebulaMapTwist false\n"
                                                          "\tNebulaMapTwistCoef1 0\n"
                                                          "\tNebulaMapTwistCoef2 0.0247934\n"
                                                          "\n"
                                                          "\tNebulaMapThickCoef (-0.5 -1.1157)\n"
                                                          "\tExpansionBegin\t2.451545000000000e+06\n"
                                                          "\tExpansionDuration\t0.000000000000000e+00\n"
                                                          "}\n")

                        f.write(bufferC)
                        totalC += int(count)

                    if int(preset) == 4 or int(preset) == 8:  # Preset 3
                        for i in range(totalD, totalD + int(count)):
                            bufferD += ("\n"
                                        'CustomModel  "Phunnie Plan A' + str(i) + '"\n'
                                                                                  "{\n"
                                                                                  "\tUseForType\t\t\"Nebula/Planetary\"\n"
                                                                                  "\n"
                                                                                  "\tEnableImpostors  true\n"
                                                                                  "\tEnableDepthTest  false\n"
                                                                                  "\tEnableDepthWrite false\n"
                                                                                  "\tEnableBlend      true\n"
                                                                                  "\n"
                                                                                  "\tShader           \"nebula_raymarch.glsl\"\n"
                                                                                  "\tShaderUniforms   \"nebula_raymarch_uniforms.cfg\"\n"
                                                                                  "\n"
                                                                                  "\tBaseShape      \"box\"\n"
                                                                                  "\tBaseShapeDims  (16 16 16)\n"
                                                                                  "\tScale          (1 1 1)\n"
                                                                                  "\tRandomize      (0 0 0)\n"
                                                                                  "\tBright          1\n"
                                                                                  "\tParticleColor  (1 0.9 0.8)\n"
                                                                                  "\t\n"
                                                                                  "\t//Dust volume parametrization\n"
                                                                                  "\tDust_enabled true\n")
                            if dust == "y":
                                bufferD += ("\tDust_volume_height " + str(random.uniform(0, 10)) + "\n")
                            if dust == 'n':
                                bufferD += ("\tDust_volume_height 1\n")
                            bufferD += (
                                "\tdust_absorption_factor 0.4\n"
                                "\tdust_scattering_factor 0.6\n")
                            if dust == 'y':
                                bufferD += ("\tDust_volume_density_factor " + str(random.uniform(0, 10)) + "\n")
                            if dust == 'n':
                                bufferD += ("\tDust_volume_density_factor 0.01\n")
                            bufferD += (
                                    "\tAlbedo 0.6\n"
                                    "\n"
                                    "\t//Scale\n"
                                    "\tInternal_scale 16\n"
                                    "\t//Raymarcher\n"
                                    "\tRaymarch_step_count 128\t\n"
                                    "\ttd_break_value 2.5\n"
                                    "\tsum_transparency_break (0.01 0.01 0.01)\n"
                                    "\t//Lights & Stars\n"
                                    "\tLight_intensivity 4\n"
                                    "\tLight_Color_11 (0.97 0.97 1)\n"
                                    "\tLight_radius_single_star 4.5\n"
                                    "\tAmbient_Light_intensivity 1\n"
                                    "\tAmbient_Light_Color_11 (0.97 0.97 1)\n"
                                    "\n"
                                    "\tSingle_star true\n"
                                    "\tStar_position (0 0 0)\n"
                                    "\tstar_empty_sphere_radius 1.5\n"
                                    "\tStar_field_scale 0.25\n"
                                    "\t\n"
                                    "\tRender_star false\n"
                                    "\tStar_light_coef_1 2\n"
                                    "\tStar_light_coef_2 100\n"
                                    "\tRender_star_bloom true\n"
                                    "\tBloom_light_coef_1 0.075\n"
                                    "\tBloom_light_coef_2 1000\n"
                                    "\n"
                                    "\t//HG phase function\n"
                                    "\tForward_scattering_g 0.6\n"
                                    "\tBackward_scattering_g -0.05\n"
                                    "\tHG_mix_coef 0.75\n"
                                    "\t\n"
                                    "\t//Emission\n"
                                    "\tGas_emission_enabled true\n"
                                    "\tGas_volume_height 0.5\n"
                                    "\tgas_scattering_factor 0.025\n"
                                    "\tgas_density_factor 0.1\n"
                                    "\tEmission_gas_1 " + str(random.choice(tf)) + "\n"
                                                                                   "\t//Emission_gas_1_external true\n")
                            if int(color) == 1:
                                bufferD += ("\tNebula_emission_color_1 (" + str(random.uniform(0, 1)) + " " + str(
                                    random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                            if int(color) == 2:
                                bufferD += ("\tNebula_emission_color_1 (0.811 " + str(
                                    random.uniform(0.25, 0.55)) + " 0.236)\n")
                            if int(color) == 3:
                                bufferD += ("\tNebula_emission_color_1 (0.926 " + str(
                                    random.uniform(0.400, 0.600)) + " 0.137)\n")
                            if int(color) == 4:
                                bufferD += ("\tNebula_emission_color_1 (0.938 " + str(
                                    random.uniform(0, 0.2)) + " 0.100)\n")
                            if int(color) == 7:
                                bufferD += ("\tNebula_emission_color_1 (" + str(
                                    random.uniform(float(R1) - float(VR1), float(R1) + float(VR1))) + " " + str(
                                    random.uniform(float(G1) - float(VG1), float(G1) + float(VG1))) + " " + str(
                                    random.uniform(float(B1) - float(VB1), float(B1) + float(VB1))) + ")\n")
                            if int(color) == 5:  # realistic
                                dict = {
                                    1: "\tNebula_emission_color_1 (0.953 " + str(
                                        random.uniform(0.3, 0.55)) + " 0.328)\n",
                                    2: "\tNebula_emission_color_1 (0.883 " + str(
                                        random.uniform(0.49, 0.55)) + " 0.490)\n",
                                    3: "\tNebula_emission_color_1 (0.585 0.232 " + str(random.uniform(0.4, 0.6)) + ")\n"
                                }
                                r = random.randint(1, 3)
                                bufferD += dict[r]
                            if int(color) == 6:  # all except random
                                dicte = {
                                    1: "\tNebula_emission_color_1 (0.811 " + str(
                                        random.uniform(0.25, 0.55)) + " 0.236)\n",
                                    2: "\tNebula_emission_color_1 (0.926 " + str(
                                        random.uniform(0.400, 0.600)) + " 0.137)\n",
                                    3: "\tNebula_emission_color_1 (0.938 " + str(random.uniform(0, 0.2)) + " 0.100)\n"
                                }
                                e = random.randint(1, 4)
                                if e == 4:
                                    dict = {
                                        1: "\tNebula_emission_color_1 (0.953 " + str(
                                            random.uniform(0.3, 0.55)) + " 0.328)\n",
                                        2: "\tNebula_emission_color_1 (0.883 " + str(
                                            random.uniform(0.49, 0.55)) + " 0.490)\n",
                                        3: "\tNebula_emission_color_1 (0.585 0.232 " + str(
                                            random.uniform(0.4, 0.6)) + ")\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferD += dict[r]
                                else:
                                    bufferD += dicte[e]
                            bufferD += (
                                "\tEmission_gas_1_direction (0 0.338843 0)\n"
                                "\tEmission_gas_1_coef_0 (0 0 5)\n"
                                "\tEmission_gas_1_coef_1 0.125\n"
                                "\tEmission_gas_1_coef_2 3.05785\n"
                                "\tEmission_gas_1_coef_3 1.57025\n"
                                "\tEmission_gas_2 true\n"
                                "\t//Emission_gas_2_external false\n")
                            if int(color) == 1:
                                bufferD += ("\tNebula_emission_color_2 (" + str(random.uniform(0, 1)) + " " + str(
                                    random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                            if int(color) == 2:
                                bufferD += ("\tNebula_emission_color_2 (0.917969 0.179291 " + str(
                                    random.uniform(0.25, 0.55)) + ")\n")
                            if int(color) == 3:
                                bufferD += ("\tNebula_emission_color_2 (" + str(
                                    random.uniform(0.550, 0.715)) + " " + str(random.uniform(0.45, 0.7)) + " 0.290)\n")
                            if int(color) == 4:
                                bufferD += ("\tNebula_emission_color_2 (0.625 " + str(
                                    random.uniform(0.180, 0.3)) + " 0.186)\n")
                            if int(color) == 7:
                                bufferD += ("\tNebula_emission_color_2 (" + str(
                                    random.uniform(float(R2) - float(VR2), float(R2) + float(VR2))) + " " + str(
                                    random.uniform(float(G2) - float(VG2), float(G2) + float(VG2))) + " " + str(
                                    random.uniform(float(B2) - float(VB2), float(B2) + float(VB2))) + ")\n")
                            if int(color) == 5:
                                dict = {
                                    1: "\tNebula_emission_color_2 (" + str(
                                        random.uniform(0.55, 0.7)) + " 0.424 0.738)\n",
                                    2: "\tNebula_emission_color_2 (0.746 0.280 " + str(
                                        random.uniform(0.35, 0.65)) + ")\n",
                                    3: "\tNebula_emission_color_2 (0.746 " + str(
                                        random.uniform(0.28, 0.4)) + " 0.280)\n"
                                }
                                r = random.randint(1, 3)
                                bufferD += dict[r]
                            if int(color) == 6:
                                dicte = {
                                    1: "\tNebula_emission_color_2 (0.917969 0.179291 " + str(
                                        random.uniform(0.25, 0.55)) + ")\n",
                                    2: "\tNebula_emission_color_2 (" + str(random.uniform(0.550, 0.715)) + " " + str(
                                        random.uniform(0.45, 0.7)) + " 0.290)\n",
                                    3: "\tNebula_emission_color_2 (0.625 " + str(
                                        random.uniform(0.180, 0.3)) + " 0.186)\n"
                                }
                                e = random.randint(1, 4)
                                if e == 4:
                                    dict = {
                                        1: "\tNebula_emission_color_2 (" + str(
                                            random.uniform(0.55, 0.7)) + " 0.424 0.738)\n",
                                        2: "\tNebula_emission_color_2 (0.785 0.347 " + str(
                                            random.uniform(0.35, 0.65)) + ")\n",
                                        3: "\tNebula_emission_color_2 (0.746 " + str(
                                            random.uniform(0.28, 0.4)) + " 0.280)\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferD += dict[r]
                                else:
                                    bufferD += dicte[e]
                            bufferD += (
                                    "\tEmission_gas_2_direction (0 1 0)\n"
                                    "\tEmission_gas_2_coef_0 (0 3 0)\n"
                                    "\tEmission_gas_2_coef_1 0.25\n"
                                    "\tEmission_gas_2_coef_2 0.5\n"
                                    "\tEmission_gas_2_coef_3 2.125\n"
                                    "\tEmission_gas_3 " + str(random.choice(tf)) + "\n"
                                                                                   "\t//Emission_gas_3_external false\n")
                            if int(color) == 1:
                                bufferD += ("\tNebula_emission_color_3 (" + str(random.uniform(0, 1)) + " " + str(
                                    random.uniform(0, 1)) + " " + str(random.uniform(0, 1)) + ")\n")
                            if int(color) == 2:
                                bufferD += ("\tNebula_emission_color_3 (0.254 " + str(
                                    random.uniform(0.07, 0.175)) + " " + str(random.uniform(0.07, 0.175)) + ")\n")
                            if int(color) == 3:
                                bufferD += ("\tNebula_emission_color_3 (0 " + str(
                                    random.uniform(0.250, 0.450)) + " 0.600)\n")
                            if int(color) == 4:
                                bufferD += ("\tNebula_emission_color_3 (0.067 " + str(
                                    random.uniform(0.250, 0.450)) + " 0.613)\n")
                            if int(color) == 7:
                                bufferD += ("\tNebula_emission_color_3 (" + str(
                                    random.uniform(float(R3) - float(VR3), float(R3) + float(VR3))) + " " + str(
                                    random.uniform(float(G3) - float(VG3), float(G3) + float(VG3))) + " " + str(
                                    random.uniform(float(B3) - float(VB3), float(B3) + float(VB3))) + ")\n")
                            if int(color) == 5:
                                dict = {
                                    1: "\tNebula_emission_color_3 (0.358 " + str(
                                        random.uniform(0.6, 0.9)) + " 0.926)\n",
                                    2: "\tNebula_emission_color_3 (0.125 " + str(
                                        random.uniform(0.3, 0.45)) + " 0.46)\n",
                                    3: "\tNebula_emission_color_3 (0.67 0.297 " + str(random.uniform(0.3, 0.45)) + ")\n"
                                }
                                r = random.randint(1, 3)
                                bufferD += dict[r]
                            if int(color) == 6:
                                dicte = {
                                    1: "\tNebula_emission_color_3 (0.254 " + str(
                                        random.uniform(0.07, 0.175)) + " " + str(random.uniform(0.07, 0.175)) + ")\n",
                                    2: "\tNebula_emission_color_3 (0 " + str(
                                        random.uniform(0.250, 0.450)) + " 0.600)\n",
                                    3: "\tNebula_emission_color_3 (0.067 " + str(
                                        random.uniform(0.250, 0.450)) + " 0.613)\n"
                                }
                                e = random.randint(1, 4)
                                if e == 4:
                                    dict = {
                                        1: "\tNebula_emission_color_3 (0.358 " + str(
                                            random.uniform(0.6, 0.9)) + " 0.926)\n",
                                        2: "\tNebula_emission_color_3 (0.125 " + str(
                                            random.uniform(0.3, 0.45)) + " 0.46)\n",
                                        3: "\tNebula_emission_color_3 (0.67 0.297 " + str(
                                            random.uniform(0.3, 0.45)) + ")\n"
                                    }
                                    r = random.randint(1, 3)
                                    bufferD += dict[r]
                                else:
                                    bufferD += dicte[e]
                            bufferD += (
                                    "\tEmission_gas_3_direction (0 0.0413223 0)\t\n"
                                    "\tEmission_gas_3_coef_0 (0 0 0)\n"
                                    "\tEmission_gas_3_coef_1 0.0909091\n"
                                    "\tEmission_gas_3_coef_2 2.19008\n"
                                    "\tEmission_gas_3_coef_3 0.578512\n"
                                    "\n"
                                    "\tEmission_intensivity_coef 330\n"
                                    "\t\n"
                                    "\tNebulaCentPos (0 -0.8 0.8)\n"
                                    "\t\n"
                                    "\t// SCALE\n"
                                    "\tNebScaleAbsBoth false\n"
                                    "\tNebScaleAbsX true\n"
                                    "\tNebScaleAbsY false\n"
                                    "\tNebScale 0.5\n"
                                    "\tNebScaleCoef (-3 -3)\t\n"
                                    "\t\n"
                                    "\t// Spiral noise\n"
                                    "\tSpirNoiseNudge (" + str(random.uniform(3, 7)) + " " + str(
                                random.uniform(3, 7)) + ")\n")
                            SpirNoiseIter = random.uniform(0.2, 3)
                            bufferD += (
                                    "\tSpirNoiseAmount (-0.0826446 -0.0826446)\n"
                                    "\tSpirNoiseIter (" + str(SpirNoiseIter) + " " + str(SpirNoiseIter) + ")\n"
                                                                                                          "\tSpirNoiseCoef (1.5 1.5)\n"
                                                                                                          "\t//Spiral Noise 3D\n"
                                                                                                          "\tNudge_3D_2 (5.53719 4.04959)\n"
                                                                                                          "\tNoise_amount_3D_2 (0 0)\n"
                                                                                                          "\tFrequency_iteration_count_3D_2 (2.68595 2.10744)\n"
                                                                                                          "\tSpirNoise3DCoef_2 (1.53373 1.53373)\n"
                                                                                                          "\n"
                                                                                                          "\t// FORM\n"
                                                                                                          "\tNebulaFormPlane false\n"
                                                                                                          "\tNebulaFormPlaneSign (1 1)\n"
                                                                                                          "\tNebulaFormPlaneXYZ (0 1 0) \n"
                                                                                                          "\tNebulaFormPlaneHeight 7\t\n"
                                                                                                          "\t\n"
                                                                                                          "\tNebulaFormDsk false\n"
                                                                                                          "\tNebulaFormDskSign (-1 -1)\n"
                                                                                                          "\tNebulaFormDskParam (2 0.8 0.25)\n"
                                                                                                          "\n"
                                                                                                          "\tNebulaFormCyl false\n"
                                                                                                          "\tNebulaFormCylSign (-1 -1)\n"
                                                                                                          "\tNebulaFormCylParam (3 5)\n"
                                                                                                          "\n"
                                                                                                          "\tNebulaFormSph " + str(
                                random.choice(tf)) + "\n"
                                                     "\tNebulaFormSphSign (0.53719 0.53719)\n"
                                                     "\tNebulaFormSphRad " + str(random.uniform(4, 10)) + "\n"
                                                                                                          "\t\n"
                                                                                                          "\tNebulaFormCapsule true\n"
                                                                                                          "\tNebulaFormCapsuleSign (1.85 1.85)\n"
                                                                                                          "\tNebulaFormCapsulePos_1 (" + str(
                                random.uniform(-2, 2)) + " " + str(random.uniform(-2, 8)) + " " + str(
                                random.uniform(-2, 2)) + ")\n"
                                                         "\tNebulaFormCapsulePos_2 (" + str(
                                random.uniform(-2, 2)) + " " + str(random.uniform(-2, 2)) + " " + str(
                                random.uniform(-12, 2)) + ")\n"
                                                          "\tNebulaFormCapsuleRadius " + str(
                                random.uniform(4, 10)) + "\n"
                                                         "\n"
                                                         "\tNebulaFormTorus false\n"
                                                         "\tNebulaFormTorusSign (-0.206612 0.123967)\n"
                                                         "\tNebulaFormTorusRadius_1 15\n"
                                                         "\tNebulaFormTorusRadius_2 1\n"
                                                         "\n"
                                                         "\tNebulaFormSpir false\n"
                                                         "\tNebulaFormSpirSign (-0.702479 -0.702479)\n"
                                                         "\tNebulaFormSpirParam (0.454545 0.330579 0.413223 0.206612)\n"
                                                         "\n"
                                                         "\tNebulaFormNoise true\n"
                                                         "\tNebulaFormNoiseSign (-1.28099 -1.28099)\n"
                                                         "\tNebulaFormNoiseCoef1 " + str(random.uniform(0, 10)) + "\n"
                                                                                                                  "\tNebulaFormNoiseCoef2 " + str(
                                random.uniform(0, 0.5)) + "\t\n"
                                                          "\t\n"
                                                          "\tNebulaFormFBMNoise true\n"
                                                          "\tNebulaFormFBMNoiseSign (-2.10744 -2.10744)\n"
                                                          "\tNebulaFormFBMNoiseCoef " + str(
                                random.uniform(0, 20)) + "\n"
                                                         "\n"
                                                         "\tNebulaFormSpirNoise true\n"
                                                         "\tNebulaFormSpirNoiseSign (-0.5 -0.5)\n"
                                                         "\tNebulaFormSpirNoiseCoef1 " + str(
                                random.uniform(0, 0.4)) + "\n"
                                                          "\tNebulaFormSpirNoiseCoef2 " + str(
                                random.uniform(0, 1000)) + "\n"
                                                           "\tNebulaFormSpirNoiseCoef3 " + str(
                                random.uniform(1, 2)) + "\n"
                                                        "\n"
                                                        "\tNebulaFormSpirIQNoise true\n"
                                                        "\tNebulaFormSpirIQNoiseSign (0.5 0.5)\n"
                                                        "\tNebulaFormSpirIQNoiseCoef1 " + str(
                                random.uniform(0.2, 0.5)) + "\n"
                                                            "\tNebulaFormSpirIQNoiseCoef2 " + str(
                                random.uniform(0, 1000)) + "\n"
                                                           "\tNebulaFormSpirIQNoiseCoef3 4\n"
                                                           "\tNebulaFormSpirIQNoiseCoef4 " + str(
                                random.uniform(2, 5)) + "\n"
                                                        "\n"
                                                        "\tNebulaFormSpirNoise3D false\n"
                                                        "\tNebulaFormSpirNoise3DSign (1 1)\n"
                                                        "\tNebulaFormSpirNoise3DCoef 1\n"
                                                        "\n"
                                                        "\t// Map\n"
                                                        "\tNebulaMapTwist " + str(random.choice(tf)) + "\n"
                                                                                                       "\tNebulaMapTwistCoef1 " + str(
                                random.uniform(0, 0.05)) + "\n"
                                                           "\tNebulaMapTwistCoef2 " + str(
                                random.uniform(0, 0.05)) + "\n"
                                                           "\n"
                                                           "\tNebulaMapThickCoef (0.2 -1)\n"
                                                           "\tExpansionBegin\t2.451545000000000e+06\n"
                                                           "\tExpansionDuration\t0.000000000000000e+00\n"
                                                           "}\n"
                                                           "\n")
                        f.write(bufferD)
                        totalD += int(count)

                    total = totalA - 1 + totalB - 1 + totalC - 1 + totalD - 1
                    em11 = discord.Embed(
                        title='Generated ' + str(total) + ' nebulae using preset ' + str(preset) + ' and color palette ' + str(color) + '.\nTo use, place the .cfg in SpaceEngine/addons/models/custom.\nType .gen to generate more.',
                        color=0x1e73e3
                    )
                    em11.set_footer(text='Generator made by Phunnie.')
                    await msg.edit(embed=em11)
                    await channel.send(file=File('/home/SE/nebula-raymarch.cfg'))

                else:
                    em111 = discord.Embed(
                        title='Error. Please write "y" or "n". Type ".gen" to try again.',
                        color=0x1e73e3
                    )
                    await msg.edit(embed=em111)
                    return





def setup(client):
    client.add_cog(generator(client))
