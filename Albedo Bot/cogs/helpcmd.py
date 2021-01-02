import discord
from discord.ext import commands
import csettings

class helpcmd(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def help(self, ctx):
        prefix = self.client.command_prefix
        prefix = str(prefix)
        embed = discord.Embed(
            colour = csettings.embedcolour(),
            description = f"Command Prefix: `{self.client.command_prefix}`\n[] = Required Arguments | <> = Optional Arguments\nRun the `{prefix}about` to learn more about the bot!"
        )
        embed.set_author(name = f"{self.client.user.name} Help Panel", icon_url = self.client.user.avatar_url)
        embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = self.client.user.avatar_url)
        embed.set_thumbnail(url = self.client.user.avatar_url)
        embed.set_image(url = "https://media.discordapp.net/attachments/773312837623218247/790258676715225178/iu.png")
        embed.add_field(name = "Character Search", value = f"You can search up characters by using the `{prefix}character [character name]` command! Some pieces of information may not be available for new characters or characters who do not confirmed information to their name!", inline = False)
        embed.add_field(name = "Enemy Search", value = f"You can search up enemies by using the `{prefix}enemy [enemy name]` command! Some pieces of information may not be available for new enemies or enemies who do not confirmed information to their name!", inline = False)
        embed.add_field(name = "Artifact Set Search", value = f"You can search up artifact sets by using the `{prefix}artifactset [set name]` command!", inline = False)
        embed.add_field(name = "Fan Art", value = f"You can view some awesome Genshin Impact Fan Art by using the `{prefix}fanart` command!", inline = False)
        embed.add_field(name = "Links", value = f"You can check out some Official Genshin Impact links by running the `{prefix}links` command!")
        embed.add_field(name = "Wishing System", value = f"Register a Gencord Wishing Account by running the `{prefix}register` command! You can do some cool wishes with the `{prefix}wish [banner code] [amount]` command. To check the banner codes, you can just run the `{prefix}wish` command as it is. You can do either a single wish `[1]` or a ten wish `[10]`! To earn primogems and mora, you can use the `{prefix}daily` command and the `{prefix}quest` command! You can gift primogems to your friends by running the `{prefix}giftprimos [member] [amount]` command!", inline = False)
        embed.add_field(name = "Genshin Imapct Fan DB", value = "All of our information comes from the **Genshin Impact Fan DB** which you can check out by clicking [here](https://www.gensh.in/)", inline = False)
        await ctx.send(embed = embed)
        





def setup(client):
    client.add_cog(helpcmd(client))