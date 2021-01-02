import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup as bs


blacklist = [



    "Tags",



    "Action",




    "Comedy",




    "Shounen",




    "Anthropomorphic",




    "Educational",




    "Episodic",




    "Medical",




    "Non-Human Protagonists",




    "Based on a Manga",





    "Content Warning",



    "Violence",





    "my anime:",


    "Unwatched",
    "Watched",
    "Watching",
    "Want to Watch",
    "Stalled",
    "Dropped",
    "Won't Watch",


    "Eps",
]

class anime_cmds(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def animesearch(self, ctx, *, term):
        term = str(term)
        term = term.lower()
        term = term.replace(" ", "-")
        term = term.replace("'", "")
        url = "https://www.anime-planet.com/anime/{}".format(term)
        page = requests.get(url)
        soup = bs(page.content, "html.parser")
        description = soup.find(class_ = "pure-1 md-3-5")
        title = soup.find(itemprop = "name")
        episodes = soup.find(class_ = "type")
        episodes = episodes.get_text()
        episodes = episodes.replace("TV", "")
        episodes = episodes.replace("(", "")
        episodes = episodes.replace(")", "")
        episodes = episodes.replace("eps", "")
        title = title.get_text()
        content_warning = soup.find(class_ = "tags tags--plain")
        content_warning = content_warning.ul.li.get_text()
        image = soup.find(class_ = "mainEntry")
        image_link = image.img["src"]
        content = description.div.p
        content = content.get_text()

        if len(content) >= 1997:
            content = content[:1997]
            content = content + "..."


        embed = discord.Embed(
            title = title, 
            description = f"Click [here]({url}) to view the Anime on [Anime Planet](https://www.anime-planet.com/)",
            colour = discord.Colour.from_rgb(230, 138, 138)
            
        )
        embed.set_thumbnail(url = "https://www.anime-planet.com" + image_link)
        embed.add_field(name = "Description", value = content, inline = False)
        embed.add_field(name = "Episodes", value = episodes, inline = False)
        embed.add_field(name = ":warning: Content Warning :warning:", value = content_warning, inline = False)
        
        await ctx.send(embed = embed)


    @animesearch.error
    async def animesearcherror(self, ctx, error):
        print(str(error))
        embed = discord.Embed(
            description = ":broken_heart: Oop! I'm sorry bb. I can't seem to find that Anime for you!",
            colour = discord.Colour.from_rgb(230, 138, 138)
        )
        await ctx.send(embed = embed)


    



    
        


            
        



def setup(client):
    client.add_cog(anime_cmds(client))