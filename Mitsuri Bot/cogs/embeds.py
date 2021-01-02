import discord
from discord.ext import commands
from discord.utils import get

class embed_main(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def embed(self, ctx):
        return
        embed_title = None
        embed_description = None
        embed_thumbnail = ""
        embed_footer = None
        embed_footer_icon = None
        embed_author = None
        embed_author_icon = None
        embed_colour = None
        def check(m):
            return m.author.id == ctx.author.id
        await ctx.send("Please type an Embed title. If you don't want one, please type `skip`")
        msg = await self.client.wait_for("message", check = check, timeout = 30.0)
        if msg.content.lower() == "skip":
            embed_title = None
        else:
            embed_title = str(msg.content)

        await ctx.send("Please type an Embed Description. If you don't want one, please type `skip`")
        msg = await self.client.wait_for("message", check = check, timeout = 30.0)
        if msg.content.lower() == "skip":
            embed_description = None
        else:
            embed_description = str(msg.content)

        await ctx.send("Please give me a link to an Embed Thumbnail. If you don't want one, please type `skip`")
        msg = await self.client.wait_for("message", check = check, timeout = 30.0)
        if msg.content.lower() == "skip":
            embed_thumbnail = ""
        else:
            embed_thumbnail = str(msg.content.lower())

        await ctx.send("Please give me an `hexadecimal` value for your embed colour! Please seperate each number with a comma!")
        msg = await self.client.wait_for("message", check = check, timeout = 30.0)
        embed_colour = msg.content

        await ctx.send("Would you still like to proceed to sending the embed? Type `yes` to proceed! Anything else will be registered as a no!")
        msg = await self.client.wait_for("message", check = check, timeout = 30)
        if str(msg.content.lower()) == "yes":
            await ctx.send("Okay! Please type the name of the channel!")
            msg = await self.client.wait_for("message", check = check, timeout = 30)
            channel = get(ctx.guild.text_channels, name = str(msg.content))
            await ctx.send("Sending Now!")
            embed = discord.Embed(
                title = embed_title,
                description = embed_description,
                colour = embed_colour
                )

            try:
                embed.set_thumbnail(url = embed_thumbnail)
            except:
                pass

            await channel.send(embed = embed)
            return


            




def setup(client):
    client.add_cog(embed_main(client))