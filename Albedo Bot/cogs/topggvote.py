import dbl
import discord
from discord.ext import commands


class TopGG(commands.Cog):
    """Handles interactions with the top.gg API"""

    def __init__(self, bot):
        self.bot = bot
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijc4OTk3NTM5NTIzODY3NDQ2MyIsImJvdCI6dHJ1ZSwiaWF0IjoxNjA4ODQ3NzI5fQ.SO7007Ty4UuHseSXJM4PfBLxZs8VZu77fEbmPWehxWY' # set this to your DBL token
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True) # Autopost will post your guild count every 30 minutes

    @commands.Cog.listener()
    async def on_guild_post(self):
        print("Server count posted successfully")


def setup(bot):
    bot.add_cog(TopGG(bot))