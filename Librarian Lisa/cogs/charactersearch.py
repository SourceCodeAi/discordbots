import discord
from discord.ext import commands
from bs4 import BeautifulSoup as bs
import requests
import characterimages
import botsettings


base_url = "https://www.gensh.in/characters"

class csearch(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def imgsearch(self, ctx, *, name : str):
        name = name.replace(" ", "")
        name = name.lower()
        name = name.capitalize()
        embed = discord.Embed(
            colour = botsettings.embed_colour(),
            timestamp = ctx.message.created_at
        )

        embed.set_image(url = characterimages.returnlink(name))
        embed.set_footer(text = name)
        await ctx.send(embed = embed)
        if name.lower() == "lisa":
            await ctx.send("hehe, thisc cutie chose me ")



def setup(client):
    client.add_cog(csearch(client))