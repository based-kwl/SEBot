import discord
from discord.ext import commands, tasks


class Discordbot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channelid = payload.channel_id
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        server = self.client.get_guild(148933808811409408)
        user = await server.fetch_member(payload.user_id)
        staff = discord.utils.get(server.roles, name="Staff-Moderator")
        if staff in user.roles and str(channelid) == str(391393331709476885) and str(payload.emoji) == '👌':
            await message.add_reaction(emoji='👌')
            await message.add_reaction(emoji='⚛')
            await message.add_reaction(emoji='☣')
        if str(channelid) == str(391393331709476885):
            if str(payload.emoji) == '👌':
                member = discord.utils.get(server.roles, name="Observer")
                bot = discord.utils.get(server.roles, name="Bot")
                if bot in user.roles:
                    return
                await user.add_roles(member)
            if str(payload.emoji) == '⚛':
                member = discord.utils.get(server.roles, name="STEAM")
                bot = discord.utils.get(server.roles, name="Bot")
                if bot in user.roles:
                    return
                await user.add_roles(member)
            if str(payload.emoji) == '☣':
                member = discord.utils.get(server.roles, name="OffTopic")
                bot = discord.utils.get(server.roles, name="Bot")
                if bot in user.roles:
                    return
                await user.add_roles(member)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        channelid = payload.channel_id
        server = self.client.get_guild(148933808811409408)
        user = await server.fetch_member(payload.user_id)
        if str(channelid) == str(391393331709476885):
            if str(payload.emoji) == '⚛':
                member = discord.utils.get(server.roles, name="STEAM")
                bot = discord.utils.get(server.roles, name="Bot")
                if bot in user.roles:
                    return
                await user.remove_roles(member)
            if str(payload.emoji) == '☣':
                member = discord.utils.get(server.roles, name="OffTopic")
                bot = discord.utils.get(server.roles, name="Bot")
                if bot in user.roles:
                    return
                await user.remove_roles(member)


def setup(client):
    client.add_cog(Discordbot(client))





