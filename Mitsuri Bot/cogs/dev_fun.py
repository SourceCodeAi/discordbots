import discord
from discord.ext import commands
import random
import asyncio
import errormsg


class dev_fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invitefun(self, ctx):
        p_bools = [True, False]
        pog_invites = []
        if ctx.author.id != 691406006277898302:
            return

        counter = 0

        for i in self.client.guilds:
            if random.choice(p_bools) == True:
                if counter >= 6:
                    await ctx.send("Finished")
                    return
                try:
                    invite = await i.text_channels[0].create_invite(temporary = False)

                    await ctx.send(f"**{i.name}: ** `{invite}`")
                    counter = counter + 1
                except:
                    pass









def setup(client):
    client.add_cog(dev_fun(client))
