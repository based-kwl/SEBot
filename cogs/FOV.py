import discord
from discord.ext import commands, tasks
import asyncio
import math


class FOV(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fov(self, ctx, arg1: str = None, arg2: str = None, arg3: str = None, arg4: str = None):
        em69 = discord.Embed(
            title='''You monster. You're trying to divide by 0!''',
            description='Type ".fov [arguments]" to try again.',
            color=0x1e73e3
        )
        em68 = discord.Embed(
            title='''A 0 width sensor... really?''',
            description='Type ".fov [arguments]" to try again.',
            color=0x1e73e3
        )
        em67 = discord.Embed(
            title='''Don't use negative values.''',
            description='Type ".fov [arguments]" to try again.',
            color=0x1e73e3
        )
        em4 = discord.Embed(
            title='Error, not a number. Type ".fov [arguments]" to try again.',
            color=0x1e73e3
        )
        em0 = discord.Embed(
            title='Do you wish to calculate the FOV for camera or eyepiece?',
            color=0x1e73e3
        )
        em1 = discord.Embed(
            title='Enter the sensor width in mm.',
            color=0x1e73e3
        )
        em6 = discord.Embed(
            title='Enter eyepiece FOV.',
            color=0x1e73e3
        )
        em7 = discord.Embed(
            title='Enter eyepiece focal length.',
            color=0x1e73e3
        )
        em8 = discord.Embed(
            title='Enter telescope focal length.',
            color=0x1e73e3
        )
        em2 = discord.Embed(
            title='Enter the focal length of the lens/telescope in mm.',
            color=0x1e73e3
        )

        em99 = discord.Embed(
            title='Request timed out.',
            description='Type ".fov [arguments]" to try again.',
            color=0x1e73e3
        )
        em100 = discord.Embed(
            title='Invalid argument',
            description='Type ".fov [arguments]" to try again.',
            color=0x1e73e3
        )
        emhelp = discord.Embed(
            title='Valid usage of the .fov command:',
            color=0x1e73e3
        )
        emhelp.add_field(name='.fov', value='Brings up the "interactive" menu.')
        emhelp.add_field(name='.fov camera [camera sensor width in mm] [telescope focal length in mm]', value='Gives the FOV for the entered values for a camera')
        emhelp.add_field(name='.fov eyepiece [eyepiece field of view] [eyepiece focal length] [telescope focal length]', value='Gives the FOV for the entered values for an eyepiece')
        channel = ctx.channel
        message = ctx.message
        content = ctx.message.content
        author = ctx.message.author
        if str(arg1).lower() == 'help':
            await channel.send(embed=emhelp)
            return
        if str(arg1).lower() == 'camera' and arg2 is not None and arg3 is not None:
            arg2f = arg2.replace('^', '**')
            arg3f = arg3.replace('^', '**')
            earg3 = eval(arg3f)
            earg2 = eval(arg2f)
            if float(earg3) == 0:
                await channel.send(embed=em69)
                return
            if float(earg3) < 0:
                await channel.send(embed=em67)
                return
            if float(earg2) == 0:
                await channel.send(embed=em68)
                return
            if float(earg2) < 0:
                await channel.send(embed=em67)
                return
            fov = 2 * math.atan(float(earg2) / 2 / float(earg3)) * 180 / math.pi
            em3 = discord.Embed(
                title='FOV= **' + str(fov) + '** °.\nEnter "fov ' + str(fov) + '" in the SE console to simulate the field of view.',
                description='Type ".fov [arguments]" to try again.',
                color=0x1e73e3
            )
            try:
                await channel.send(embed=em3)
                return
            except:
                await channel.send(embed=em99)
                return
        if str(arg1).lower() == 'eyepiece' and arg2 is not None and arg3 is not None and arg4 is not None:
            arg2f = arg2.replace('^', '**')
            arg4f = arg4.replace('^', '**')
            arg3f = arg3.replace('^', '**')
            earg3 = eval(arg3f)
            earg2 = eval(arg2f)
            earg4 = eval(arg4f)
            if float(earg3) == 0:
                await channel.send(embed=em69)
                return
            if float(earg3) < 0:
                await channel.send(embed=em67)
                return
            if float(earg4) == 0:
                await channel.send(embed=em69)
                return
            if float(earg4) < 0:
                await channel.send(embed=em67)
                return
            if float(earg2) == 0:
                await channel.send(embed=em68)
                return
            if float(earg2) < 0:
                await channel.send(embed=em67)
                return
            fov = float(earg2) / (float(earg4) / float(earg3))
            em3 = discord.Embed(
                title='FOV= **' + str(fov) + '** °.\nEnter "fov ' + str(fov) + '" in the SE console to simulate the field of view.',
                description='Type ".fov [arguments]" to try again.',
                color=0x1e73e3
            )
            try:
                await channel.send(embed=em3)
                return
            except:
                await channel.send(embed=em99)
                return
        msg = await channel.send(embed=em0)
        try:
            def check(message):
                return message.author == author and message.channel == channel
            cameraornot = await self.client.wait_for('message', check=check, timeout=30)
            if str(cameraornot.content).lower() == 'camera':
                await msg.edit(embed=em1)
                asyncio.sleep(0.3)
                await cameraornot.delete()
                try:
                    def check(message):
                        return message.author == author and message.channel == channel
                    ans = await self.client.wait_for('message', check=check, timeout=30)
                    ansf = ans.content.replace('^', '**')
                    eans = eval(ansf)
                    await msg.edit(embed=em2)
                    asyncio.sleep(0.3)
                    await ans.delete()
                    try:
                        if float(eans) == 0:
                            await msg.edit(embed=em68)
                            return
                        if float(eans) < 0:
                            await msg.edit(embed=em67)
                            return
                        try:
                            def check(message):
                                return message.author == author and message.channel == channel
                            ans2 = await self.client.wait_for('message', check=check, timeout=30)
                            asyncio.sleep(0.3)
                            await ans2.delete()
                            try:
                                ansf = ans2.content.replace('^', '**')
                                eans2 = eval(ansf)
                                if float(eans2) == 0:
                                    await msg.edit(embed=em69)
                                    return
                                if float(eans2) < 0:
                                    await msg.edit(embed=em67)
                                    return
                                fov = 2 * math.atan(float(eans) / 2 / float(eans2)) * 180 / math.pi
                                em5 = discord.Embed(
                                    title='FOV= **' + str(fov) + '** °.\nEnter "fov ' + str(fov) + '" in the SE console to simulate the field of view.',
                                    description='Type ".fov [arguments]" to try again.',
                                    color=0x1e73e3
                                )
                                await msg.edit(embed=em5)
                                return
                            except:
                                await msg.edit(embed=em4)
                                return
                        except:
                            await msg.edit(embed=em99)
                            return
                    except:
                        await msg.edit(embed=em4)
                        return
                except:
                    await msg.edit(embed=em99)
                    return
            if str(cameraornot.content).lower() == 'eyepiece':
                await msg.edit(embed=em6)
                asyncio.sleep(0.3)
                await cameraornot.delete()
                try:
                    def check(message):
                        return message.author == author and message.channel == channel
                    ans = await self.client.wait_for('message', check=check, timeout=30)
                    await msg.edit(embed=em7)
                    asyncio.sleep(0.3)
                    await ans.delete()
                    try:
                        ansf = ans.content.replace('^', '**')
                        eans = eval(ansf)
                        if float(eans) == 0:
                            await msg.edit(embed=em68)
                            return
                        if float(eans) < 0:
                            await msg.edit(embed=em67)
                            return
                        try:
                            def check(message):
                                return message.author == author and message.channel == channel
                            ans2 = await self.client.wait_for('message', check=check, timeout=30)
                            await msg.edit(embed=em8)
                            asyncio.sleep(0.3)
                            await ans2.delete()
                            try:
                                ansf = ans2.content.replace('^', '**')
                                eans2 = eval(ansf)
                                if float(eans2) == 0:
                                    await msg.edit(embed=em69)
                                    return
                                if float(eans2) < 0:
                                    await msg.edit(embed=em67)
                                    return
                                try:
                                    def check(message):
                                        return message.author == author and message.channel == channel

                                    ans3 = await self.client.wait_for('message', check=check, timeout=30)

                                    try:
                                        ansf = ans3.content.replace('^', '**')
                                        eans3 = eval(ansf)
                                        if float(eans3) == 0:
                                            await msg.edit(embed=em69)
                                            return
                                        if float(eans3) < 0:
                                            await msg.edit(embed=em67)
                                            return
                                        fov = float(eans) / (float(eans3) / float(eans2))
                                        em5 = discord.Embed(
                                            title='FOV= **' + str(fov) + '** °.\nEnter "fov ' + str(fov) + '" in the SE console to simulate the field of view.',
                                            description='Type ".fov [arguments]" to try again.',
                                            color=0x1e73e3
                                        )
                                        asyncio.sleep(0.3)
                                        await ans3.delete()
                                        await msg.edit(embed=em5)
                                        return
                                    except:
                                        await msg.edit(embed=em4)
                                        return
                                except:
                                    await msg.edit(embed=em99)
                                    return
                            except:
                                await msg.edit(embed=em4)
                                return
                        except:
                            await msg.edit(embed=em99)
                            return
                    except:
                        await msg.edit(embed=em4)
                        return
                except:
                    await msg.edit(embed=em99)
                    return

            else:
                await msg.edit(embed=em100)
        except:
            await msg.edit(embed=em99)
            return

    @commands.command()
    async def afov(self, ctx, arg1: str = None, arg2: str = None, arg3: str = None, arg4: str = None):
        em69 = discord.Embed(
            title='''You monster. You're trying to divide by 0!''',
            description='Type ".afov [arguments]" to try again.',
            color=0x1e73e3
        )
        em68 = discord.Embed(
            title='''A 0 width sensor... really?''',
            description='Type ".afov [arguments]" to try again.',
            color=0x1e73e3
        )
        em67 = discord.Embed(
            title='''Don't use negative values.''',
            description='Type ".afov [arguments]" to try again.',
            color=0x1e73e3
        )
        em4 = discord.Embed(
            title='Error, not a number. Type ".afov [arguments]" to try again.',
            color=0x1e73e3
        )
        em0 = discord.Embed(
            title='Do you wish to calculate the FOV for camera or eyepiece?',
            color=0x1e73e3
        )
        em1 = discord.Embed(
            title='Enter the sensor width in mm.',
            color=0x1e73e3
        )
        em6 = discord.Embed(
            title='Enter eyepiece FOV.',
            color=0x1e73e3
        )
        em7 = discord.Embed(
            title='Enter eyepiece focal length.',
            color=0x1e73e3
        )
        em8 = discord.Embed(
            title='Enter telescope focal length.',
            color=0x1e73e3
        )
        em2 = discord.Embed(
            title='Enter the focal length of the lens/telescope in mm.',
            color=0x1e73e3
        )

        em99 = discord.Embed(
            title='Request timed out.',
            description='Type ".afov [arguments]" to try again.',
            color=0x1e73e3
        )
        em100 = discord.Embed(
            title='Invalid argument',
            description='Type ".afov [arguments]" to try again.',
            color=0x1e73e3
        )
        emhelp = discord.Embed(
            title='Valid usage of the .afov command:',
            color=0x1e73e3
        )
        emhelp.add_field(name='.afov', value='Brings up the "interactive" menu.')
        emhelp.add_field(name='.afov camera [camera sensor width in mm] [telescope focal length in mm]',
                         value='Gives the FOV for the entered values for a camera')
        emhelp.add_field(name='.afov eyepiece [eyepiece field of view] [eyepiece focal length] [telescope focal length]',
                         value='Gives the FOV for the entered values for an eyepiece')
        channel = ctx.channel
        message = ctx.message
        content = ctx.message.content
        author = ctx.message.author
        if str(arg1).lower() == 'help':
            await channel.send(embed=emhelp)
            return
        if str(arg1).lower() == 'camera' and arg2 is not None and arg3 is not None:
            arg2f = arg2.replace('^', '**')
            arg3f = arg3.replace('^', '**')
            earg3 = eval(arg3f)
            earg2 = eval(arg2f)
            if float(earg3) == 0:
                await channel.send(embed=em69)
                return
            if float(earg3) < 0:
                await channel.send(embed=em67)
                return
            if float(earg2) == 0:
                await channel.send(embed=em68)
                return
            if float(earg2) < 0:
                await channel.send(embed=em67)
                return
            fov = 2 * math.atan(float(earg2) / 2 / float(earg3)) * 180 / math.pi
            em3 = discord.Embed(
                title='FOV= **' + str(fov) + '** °.',
                description='Type ".afov [arguments]" to try again.',
                color=0x1e73e3
            )
            try:
                await channel.send(embed=em3)
                return
            except:
                await channel.send(embed=em99)
                return
        if str(arg1).lower() == 'eyepiece' and arg2 is not None and arg3 is not None and arg4 is not None:
            arg2f = arg2.replace('^', '**')
            arg4f = arg4.replace('^', '**')
            arg3f = arg3.replace('^', '**')
            earg3 = eval(arg3f)
            earg2 = eval(arg2f)
            earg4 = eval(arg4f)
            if float(earg3) == 0:
                await channel.send(embed=em69)
                return
            if float(earg3) < 0:
                await channel.send(embed=em67)
                return
            if float(earg4) == 0:
                await channel.send(embed=em69)
                return
            if float(earg4) < 0:
                await channel.send(embed=em67)
                return
            if float(earg2) == 0:
                await channel.send(embed=em68)
                return
            if float(earg2) < 0:
                await channel.send(embed=em67)
                return
            fov = float(earg2) / (float(earg4) / float(earg3))
            em3 = discord.Embed(
                title='FOV= **' + str(fov) + '** °.',
                description='Type ".afov [arguments]" to try again.',
                color=0x1e73e3
            )
            try:
                await channel.send(embed=em3)
                return
            except:
                await channel.send(embed=em99)
                return
        msg = await channel.send(embed=em0)
        try:
            def check(message):
                return message.author == author and message.channel == channel

            cameraornot = await self.client.wait_for('message', check=check, timeout=30)
            if str(cameraornot.content).lower() == 'camera':
                await msg.edit(embed=em1)
                asyncio.sleep(0.3)
                await cameraornot.delete()
                try:
                    def check(message):
                        return message.author == author and message.channel == channel

                    ans = await self.client.wait_for('message', check=check, timeout=30)
                    ansf = ans.content.replace('^', '**')
                    eans = eval(ansf)
                    await msg.edit(embed=em2)
                    asyncio.sleep(0.3)
                    await ans.delete()
                    try:
                        if float(eans) == 0:
                            await msg.edit(embed=em68)
                            return
                        if float(eans) < 0:
                            await msg.edit(embed=em67)
                            return
                        try:
                            def check(message):
                                return message.author == author and message.channel == channel

                            ans2 = await self.client.wait_for('message', check=check, timeout=30)
                            asyncio.sleep(0.3)
                            await ans2.delete()
                            try:
                                ansf = ans2.content.replace('^', '**')
                                eans2 = eval(ansf)
                                if float(eans2) == 0:
                                    await msg.edit(embed=em69)
                                    return
                                if float(eans2) < 0:
                                    await msg.edit(embed=em67)
                                    return
                                fov = 2 * math.atan(float(eans) / 2 / float(eans2)) * 180 / math.pi
                                em5 = discord.Embed(
                                    title='FOV= **' + str(fov) + '** °.',
                                    description='Type ".afov [arguments]" to try again.',
                                    color=0x1e73e3
                                )
                                await msg.edit(embed=em5)
                                return
                            except:
                                await msg.edit(embed=em4)
                                return
                        except:
                            await msg.edit(embed=em99)
                            return
                    except:
                        await msg.edit(embed=em4)
                        return
                except:
                    await msg.edit(embed=em99)
                    return
            if str(cameraornot.content).lower() == 'eyepiece':
                await msg.edit(embed=em6)
                asyncio.sleep(0.3)
                await cameraornot.delete()
                try:
                    def check(message):
                        return message.author == author and message.channel == channel

                    ans = await self.client.wait_for('message', check=check, timeout=30)
                    await msg.edit(embed=em7)
                    asyncio.sleep(0.3)
                    await ans.delete()
                    try:
                        ansf = ans.content.replace('^', '**')
                        eans = eval(ansf)
                        if float(eans) == 0:
                            await msg.edit(embed=em68)
                            return
                        if float(eans) < 0:
                            await msg.edit(embed=em67)
                            return
                        try:
                            def check(message):
                                return message.author == author and message.channel == channel

                            ans2 = await self.client.wait_for('message', check=check, timeout=30)
                            await msg.edit(embed=em8)
                            asyncio.sleep(0.3)
                            await ans2.delete()
                            try:
                                ansf = ans2.content.replace('^', '**')
                                eans2 = eval(ansf)
                                if float(eans2) == 0:
                                    await msg.edit(embed=em69)
                                    return
                                if float(eans2) < 0:
                                    await msg.edit(embed=em67)
                                    return
                                try:
                                    def check(message):
                                        return message.author == author and message.channel == channel

                                    ans3 = await self.client.wait_for('message', check=check, timeout=30)

                                    try:
                                        ansf = ans3.content.replace('^', '**')
                                        eans3 = eval(ansf)
                                        if float(eans3) == 0:
                                            await msg.edit(embed=em69)
                                            return
                                        if float(eans3) < 0:
                                            await msg.edit(embed=em67)
                                            return
                                        fov = float(eans) / (float(eans3) / float(eans2))
                                        em5 = discord.Embed(
                                            title='FOV= **' + str(fov) + '** °.',
                                            description='Type ".afov [arguments]" to try again.',
                                            color=0x1e73e3
                                        )
                                        asyncio.sleep(0.3)
                                        await ans3.delete()
                                        await msg.edit(embed=em5)
                                        return
                                    except:
                                        await msg.edit(embed=em4)
                                        return
                                except:
                                    await msg.edit(embed=em99)
                                    return
                            except:
                                await msg.edit(embed=em4)
                                return
                        except:
                            await msg.edit(embed=em99)
                            return
                    except:
                        await msg.edit(embed=em4)
                        return
                except:
                    await msg.edit(embed=em99)
                    return

            else:
                await msg.edit(embed=em100)
        except:
            await msg.edit(embed=em99)
            return




def setup(client):
    client.add_cog(FOV(client))



