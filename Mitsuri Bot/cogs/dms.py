import discord
from discord.ext import commands
import asyncio

class dms(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(description = "[no arguments needed]")
    @commands.dm_only()
    async def wannasmash(self, ctx):
        message = ctx.message
        def check(m):
            return m.author.id == message.author.id
        if message.author.bot:
            return
        if message.guild is None:
            await message.channel.send("Oh! Hello bb! Didn't see you there! :blush: Hehe. Wanna smash? Please say `yes`! I'll be fine with `no` too though but I won't be happy. You want me to be happy right?!")
            msg = await self.client.wait_for("message", check = check, timeout = 15.0)
            if str(msg.content).lower() == "yes":
                await message.channel.send("Hehe. Hold, on I'm going to prepare!")
                await asyncio.sleep(3.0)
                await message.channel.send("Hehe, I'm ready. Tell me when your ready!")
                await self.client.wait_for("message", check = check)
                embed = discord.Embed(
                    title = "oOoOoOoOh. That feels good! :heart:",
                    description = "I'm having fun!",
                    colour = discord.Colour.from_rgb(230, 138, 138))

                embed.set_image(url = "https://media.discordapp.net/attachments/763421716482490398/775459123247841300/rickroll.gif")
                await message.channel.send(embed = embed)




def setup(client):
    client.add_cog(dms(client))
