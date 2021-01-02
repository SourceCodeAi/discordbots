import discord
from discord.ext import commands


class other_main(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(description = "[no arguments needed]")
    async def invite(self, ctx):
        embed = discord.Embed(
        title = "You're adding me to your server! UwU. Ty!",
        description = f"[Click me to add me to your server!](https://discord.com/api/oauth2/authorize?client_id=772911474012061697&permissions=8&scope=bot)",
        colour = discord.Colour.from_rgb(230, 138, 138)
        )
        embed.set_footer(text = "Ty! UwU. Ty! Ty! Ty!", icon_url = self.client.user.avatar_url)
        await ctx.send(embed = embed)

    @commands.command()
    async def createinvite(self, ctx):
        channel = ctx.message.channel
        invite = await channel.create_invite(reason = f"Mitsuri Bot Server Invite Create Command Run By {ctx.author}", temporary = False)
        await ctx.send(invite)

    @commands.command("[member]")
    async def col(self, ctx, *, member : discord.Member):
        member_color = member.colour
        member_color = member_color
        embed = discord.Embed(
        color = member_color,
        timestamp = ctx.message.created_at
        )
        embed.set_image(url = member.avatar_url)
        embed.set_footer("This returns the colour of the member's highest role!")
        await ctx.send(embed = embed)



def setup(client):
    client.add_cog(other_main(client))
