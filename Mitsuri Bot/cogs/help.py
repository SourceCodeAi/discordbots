import discord
from discord.ext import commands





utlity = ["command [command name]", "nick [new server nickname]", "ping", "pfp [member]", "gif [search term]", "logs"]
moderation = ["ban [member] [reason]", "kick [member] [reason]", "bug [bug report]", "clear [amount]", "userinfo [member]", "membercount"]
fun = ["hug [member]", "kiss [member]", "punch [member]", "ship [member 1] [member 2]", "wyr", "cookie", "8ball [your question]", "truthordare"]
other = ["invite", "createinvite", "support", "wannasmash (dms only)", "col [member]"]
waifu = ["waifu [member]", "waifusearch [waifu name]"]
lovecmds = ["propose [member]"]
anime = ["animesearch [anime name]"]

class help_main(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command(description = "[no arguments needed]")
    async def help(self, ctx):
        embed = discord.Embed(
        title = "Mitsuri Help Panel",
        description = f"Command Prefix: `{self.client.command_prefix}`",
        colour = discord.Colour.from_rgb(230, 138, 138)
        )

        embed.set_thumbnail(url = self.client.user.avatar_url)
        embed.set_image(url = "https://media.discordapp.net/attachments/773312837623218247/773675773776363520/mbanner.png")


        utlity_cmds = ""
        moderation_cmds = ""
        fun_cmds = ""
        other_cmds = ""
        info = f"If you need to DM the developer of Mitsuri Bot for any reason at all just DM **[**`{str(self.client.get_user(691406006277898302))}`**]**"
        waifu_cmds = ""
        love_cmds = ""
        anime_cmds = ""
        for i in anime:
            anime_cmds = anime_cmds + f"\n`{self.client.command_prefix}{i}`"


        for i in other:
            other_cmds = other_cmds + f"\n`{self.client.command_prefix}{i}`"

        for i in lovecmds:
            love_cmds = love_cmds + f"\n`{self.client.command_prefix}{i}`"


        for i in waifu:
            waifu_cmds = waifu_cmds + f"\n`{self.client.command_prefix}{i}`"

        for i in utlity:
            utlity_cmds = utlity_cmds + f"\n`{self.client.command_prefix}{i}`"

        for i in moderation:
            moderation_cmds = moderation_cmds + f"\n`{self.client.command_prefix}{i}`"

        for i in fun:
            fun_cmds = fun_cmds + f"\n`{self.client.command_prefix}{i}`"


        embed.add_field(name = "Waifu", value = waifu_cmds, inline = False)
        embed.add_field(name = "Anime", value = anime_cmds, inline = False)
        embed.add_field(name = "Love", value = love_cmds, inline = False)
        embed.add_field(name = "Utility", value = utlity_cmds, inline = False)
        embed.add_field(name = "Moderation", value = moderation_cmds, inline = False)
        embed.add_field(name = "Fun", value = fun_cmds, inline = False)
        embed.add_field(name = "Other", value = other_cmds, inline = False)
        embed.add_field(name = "Information", value = info, inline = False)

        embed.set_footer(text = f"Cuter Development™", icon_url = "https://media.discordapp.net/attachments/763421716482490398/777251618407579658/logo.png")

        await ctx.send(embed = embed)

    @commands.command(description = "[no arguments needed]")
    async def support(self, ctx):
        embed = discord.Embed(
            title = "Awww. Do you need help?",
            description = f"You can join my support server [here](https://discord.gg/WJVKQGBMfs)!",
            colour = discord.Colour.from_rgb(230, 138, 138))

        embed.set_thumbnail(url = self.client.user.avatar_url)
        await ctx.send(embed = embed)






def setup(client):
    client.add_cog(help_main(client))
