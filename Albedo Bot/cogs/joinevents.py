import discord
from discord.ext import commands

class joinandleave(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        server_invite = await guild.text_channels[0].create_invite(reason = "Gencord Security Logging (To prevent Discord TOS breaking servers)")
        embed = discord.Embed(
            colour = discord.Colour.blurple(),
            timestamp = guild.me.joined_at
        )
        embed.set_author(name = f"{self.client.user.name} Join Event", icon_url = self.client.user.avatar_url)
        embed.set_footer(text = f"Server Owner: {guild.owner}", icon_url = self.client.user.avatar_url)
        embed.add_field(name = "Server Name", value = guild.name, inline = True)
        embed.add_field(name = "Member Count", value = str(len(guild.members)), inline = True)
        embed.add_field(name = "Invite Link", value = str(server_invite), inline = True)
        channel = await self.client.fetch_channel(790580152693293106)
        await channel.send(embed = embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        server_invite = "Missing Permissions"
        embed = discord.Embed(
            colour = discord.Colour.blurple()
        )
        embed.set_author(name = f"{self.client.user.name} Leave Event", icon_url = self.client.user.avatar_url)
        embed.set_footer(text = f"Server Owner: {guild.owner}", icon_url = self.client.user.avatar_url)
        embed.add_field(name = "Server Name", value = guild.name, inline = True)
        embed.add_field(name = "Member Count", value = str(len(guild.members)), inline = True)
        embed.add_field(name = "Invite Link", value = str(server_invite), inline = True)
        channel = await self.client.fetch_channel(790580152693293106)
        await channel.send(embed = embed)



def setup(client):
    client.add_cog(joinandleave(client))