import discord
from discord.ext import commands
import errormsg


class love_main(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def propose(self, ctx, *, member : discord.Member):
        if member.id == ctx.author.id:
            await ctx.send(embed = errormsg.shoot_noti(f":broken_heart: You can't propose to yourself!"))
            return

        if member.id == self.client.user.id:
            await ctx.send("Oh uh. uwu")
            return
        def check(m):
            return m.author.id == ctx.author.id

        await ctx.send(embed = errormsg.shoot_noti("What would you like to say at the proposition?"))
        msg = await self.client.wait_for("message", check = check, timeout = 30.0)
        prop_msg = str(msg.content)
        embed = discord.Embed(
        title = f"You have a new proposition!",
        description = f"**{ctx.author} said:** {prop_msg}\n\n\n",
        colour = discord.Colour.from_rgb(230, 138, 138),
        timestamp = ctx.message.created_at
        )
        embed.set_footer(text = f"DM them. Hehe. I'm sure they would want you to!")
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

        try:
            await member.send(embed = embed)
            await ctx.send(embed = errormsg.shoot_noti(f"Sent your proposition cutie. I made sure that your message was correct. Here it is. Just so you don't get nervous: `{prop_msg}`"))
        except:
            await ctx.send(embed = errormsg.shoot_noti(f"Oop. I'm sorry cutie but I can't send any messages to {member.mention}. Maybe ask them to open their DMs?"))





def setup(client):
    client.add_cog(love_main(client))
