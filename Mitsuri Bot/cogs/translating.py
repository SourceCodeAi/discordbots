import discord
from discord.ext import commands
from googletrans import Translator
trans = Translator()
embedColour = discord.Colour.from_rgb(230, 138, 138)
class access_langs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def translate(self, ctx, *, text):
        new = trans.translate(text)
        embed = discord.Embed(
            title = "uwu. yes I translate. hehe. :heart:",
            colour = embedColour
        )

        embed.add_field(name = "Original Text", value = text, inline = False)
        embed.add_field(name = "Translated Text", value = new.text, inline = False)

        await ctx.send(embed = embed)






def setup(client):
    client.add_cog(access_langs(client))
