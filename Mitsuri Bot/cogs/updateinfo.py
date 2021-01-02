import discord
from discord.ext import commands
import json
import os
cwd = os.getcwd()
os.chdir(cwd)

class updateinfo(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def updatelogs(self, ctx):
        log_name = None
        log_description = None
        log_time = ctx.message.created_at
        if ctx.author.id != 691406006277898302:
            return

        def check(m):
            return m.author.id == 691406006277898302
            
        await ctx.send("New Log Name:")
        msg = await self.client.wait_for("message", check = check)
        if msg.content.lower() == "cancel":
            await ctx.send("Cancelled")
            return
        else:
            log_name = msg.content

        await ctx.send("New Log Description:")
        msg = await self.client.wait_for("message", check = check)
        if msg.content.lower() == "cancel":
            await ctx.send("Cancelled")
            return
        else:
            log_description = msg.content


        with open("logs.json", "r") as f:
            data = json.load(f)

        data["name"] = log_name
        data["time"] = str(log_time)
        data["description"] = log_description

        with open("logs.json", "w") as e:
            json.dump(data, e, indent = 4)
            await ctx.send("Filed Log")

        
    @commands.command()
    async def logs(self, ctx):
        with open("logs.json", "r") as f:
            data = json.load(f)

        log_name = data["name"]
        log_description = data["description"]
        log_time = data["time"]

        embed = discord.Embed(
            title = log_name,
            description = log_description,
            colour = discord.Colour.from_rgb(230, 138, 138)
        )
        await ctx.send(embed = embed)

       
        






def setup(client):
    client.add_cog(updateinfo(client))