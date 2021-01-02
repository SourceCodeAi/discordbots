import discord
from discord.ext import commands
from discord.utils import get


class events(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "<@!789975395238674463>":
            await message.channel.send(f"Hey there! I'm Albedo, the chief Alchemist of the Knights of Favonius! My command prefix is `{self.client.command_prefix}`. You can check out what I do by running my `{self.client.command_prefix}help` command!")


    


def setup(client):
    client.add_cog(events(client))