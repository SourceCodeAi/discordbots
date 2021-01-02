from discord.ext import commands

import dbl


class TopGG(commands.Cog):
    """
    This example uses dblpy's webhook system.
    In order to run the webhook, at least webhook_port must be specified (number between 1024 and 49151).
    """

    def __init__(self, bot):
        self.bot = bot
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijc4OTk3NTM5NTIzODY3NDQ2MyIsImJvdCI6dHJ1ZSwiaWF0IjoxNjA4ODQ3NzI5fQ.SO7007Ty4UuHseSXJM4PfBLxZs8VZu77fEbmPWehxWY'  # set this to your DBL token
        self.dblpy = dbl.DBLClient(self.bot, self.token, webhook_path='/dblwebhook', webhook_auth='Universe', webhook_port=4024)

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        """An event that is called whenever someone votes for the bot on top.gg."""
        print("Received an upvote:", "\n", data, sep="")

    @commands.Cog.listener()
    async def on_dbl_test(self, data):
        """An event that is called whenever someone tests the webhook system for your bot on top.gg."""
        print("Test Vote Received")
        print("Received a test upvote:", "\n", data, sep="")


def setup(bot):
    bot.add_cog(TopGG(bot))