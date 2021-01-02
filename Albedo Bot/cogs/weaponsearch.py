import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup as bs



class weaponsearch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def weapon(self, ctx, *, weapon_name : str):
        weapon_name = weapon_name.lower()
        weapon_name = weapon_name.replace("'", "")
        weapon_name = weapon_name.replace(" ", "-")
        weapon_description = "None Found"
        r = requests.get(f"https://www.gensh.in/database/weapon/{weapon_name}")
        soup = bs(r.content, "html.parser")
        cards = soup.findAll("div", class_ = "card")
        for i in cards:
            try:
                if i.find(class_ = "card-body").h3.get_text() == "Detailed Description":
                    weapon_description = i.find(class_ = "card-body").p.get_text()
            except:
                pass



def setup(client):
    client.add_cog(weaponsearch(client))