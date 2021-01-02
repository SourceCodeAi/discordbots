import discord
from discord.ext import commands
import csettings


all_links = ["[Official Genshin Impact Homepage](https://genshin.mihoyo.com/en)", "[Official Genshin Impact Twitter Account](https://twitter.com/genshinimpact)", "[Official Genshin Impact Global Facebook Account](https://www.facebook.com/Genshinimpact/)", "[Official Sub-Reddit](https://www.reddit.com/r/Genshin_Impact)", "[Official YouTube Channel](https://www.youtube.com/c/GenshinImpact)", "[Twitch Category](https://www.twitch.tv/directory/game/Genshin%20Impact)"]

class linkspy(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def links(self, ctx):
        description = ""
        for i in all_links:
            if all_links.index(i) == 0:
                description = f"• {i}"
            else:
                description = description + "\n" + f"• {i}"
        embed = discord.Embed(
            colour = csettings.embedcolour(),
            description = description,
            timestamp = ctx.message.created_at
        )
        embed.set_author(name = "Official Genshin Impact Links", icon_url = self.client.user.avatar_url)
        embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = self.client.user.avatar_url)
        await ctx.send(embed = embed)




def setup(client):
    client.add_cog(linkspy(client))