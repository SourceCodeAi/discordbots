import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup as bs




class waifu_search(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def waifusearch(self, ctx, *, term):
        url_term = str(term).replace(" ", "-")
        url_term = url_term.lower()
        url = "https://mywaifulist.moe/waifu/{}".format(url_term)
        await ctx.send(f"> **Search Term:** {term}\n> **Result:** {url}")




def setup(client):
    client.add_cog(waifu_search(client))