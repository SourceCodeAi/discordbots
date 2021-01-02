import discord
from discord.ext import commands
import errormsg

class help_ext(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(description = "[command name]")
    async def command(self, ctx, *, command_name : str):
        command = None
        try:
            command = self.client.get_command(command_name)
        except:
            await ctx.send(embed = errormsg.shoot_embed(":broken_heart: I can't seem to find that command! Perhaps you made a typo?"))
            return

        embed = discord.Embed(
        description = f"`{self.client.command_prefix}{command.name} {command.description}`",
        colour = discord.Colour.from_rgb(230, 138, 138)
        )

        embed.set_author(name = "Command Usage", icon_url = self.client.user.avatar_url)

        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(help_ext(client))
