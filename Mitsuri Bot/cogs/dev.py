import discord
from discord.ext import commands



class dev_main(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def guilds(self, ctx):
        if ctx.author.id != 691406006277898302:
            return

        await ctx.send(f"I am in {len(self.client.guilds)} Servers!")



def setup(client):
    client.add_cog(dev_main(client))
