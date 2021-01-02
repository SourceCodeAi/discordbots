import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO
import os
import errormsg

class waifu(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(description = "[member]")
    async def waifu(self, ctx, member : discord.Member):
        image = Image.open("waifu.png")
        a = Image.open(BytesIO(await member.avatar_url.read()))
        area = (150, 50)
        box = (100,100,100,100)
        a.save(f"{member.id}-og.jpg")
        og = Image.open(f"{member.id}-og.jpg")
        og.thumbnail((214, 214))
        #a.save("test.png")
        image.paste(og, area)
        image.save(f"{member.id}-waifu.jpg")
        filepath = f"{member.id}-waifu.jpg"


        await ctx.send(f"> **[**Waifu {member.name}**]**", file = discord.File(filepath))
        os.remove(filepath)
        os.remove(f"{member.id}-og.jpg")


    @waifu.error
    async def waifu_error(self, ctx, error):
        await ctx.send(embed = errormsg.shoot_embed(":broken_heart: I can't turn that person into a waifu unfortunately!"))




def setup(client):
    client.add_cog(waifu(client))
