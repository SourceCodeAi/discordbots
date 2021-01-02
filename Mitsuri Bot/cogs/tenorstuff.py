import discord
from discord.ext import commands
import requests
import json
import random


apikey = "VW6OD32OC17R"


class tenor_stuff(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description = "[member]")
    async def kiss(self, ctx, *, member : discord.Member):
        all_results = []
        search_term = "anime+kiss"
        lmt = 8
        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            top_8gifs = json.loads(r.content)
            #print(top_8gifs)
        else:
            top_8gifs = None


        for i in top_8gifs["results"]:
            all_results.append(i["media"][0]["gif"]["url"])


        embed = discord.Embed(
        title = f"{ctx.author.name} kisses {member.name}!",
        description = "Aww. Look at these cuties!",
        colour = discord.Colour.from_rgb(230, 138, 138)
        )

        embed.set_image(url = random.choice(all_results))

        await ctx.send(embed = embed)


    @commands.command(description = "[member]")
    async def punch(self, ctx, *, member : discord.Member):
        all_results = []
        search_term = "anime+punch"
        lmt = 8
        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            top_8gifs = json.loads(r.content)
            #print(top_8gifs)
        else:
            top_8gifs = None


        for i in top_8gifs["results"]:
            all_results.append(i["media"][0]["gif"]["url"])


        embed = discord.Embed(
        title = f"{ctx.author.name} punches {member.name}!",
        description = "Dang. I wonder what went on between these two!",
        colour = discord.Colour.from_rgb(230, 138, 138)
        )

        embed.set_image(url = random.choice(all_results))

        await ctx.send(embed = embed)



    @commands.command(description = "[search term]")
    async def gif(self, ctx, *, term : str):
        term = term.replace(" ", "+")
        all_results = []
        search_term = term
        lmt = 8
        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            top_8gifs = json.loads(r.content)
            #print(top_8gifs)
        else:
            top_8gifs = None


        for i in top_8gifs["results"]:
            all_results.append(i["media"][0]["gif"]["url"])

        chosen_gif = random.choice(all_results)

        embed = discord.Embed(
        title = f"Here's your gif!",
        description = f"[Click here to view the original GIF]({str(chosen_gif)})",
        colour = discord.Colour.from_rgb(230, 138, 138),
        timestamp = ctx.message.created_at
        )

        embed.set_footer(text = f"Requested by {str(ctx.author)}", icon_url = ctx.author.avatar_url)

        embed.set_image(url = chosen_gif)

        await ctx.send(embed = embed)



def setup(client):
    client.add_cog(tenor_stuff(client))
