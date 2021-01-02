import discord
from discord.ext import commands
import botsettings

class events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "<@!776115261085319187>":
            await msg.channel.send(f"hey cutie! my command prefix is `{self.client.command_prefix}`. u can see what i can do with my `{self.client.command_prefix}help` command!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild

        embed = discord.Embed(
            title = f"Welcome to {guild.name}!",
            colour = botsettings.embed_colour(),
            description = f"hey cutie. welcome to {guild.name}! we're a steadily growing community that luvs to have fun! we like to joke around, and most of all, talk about genshin impact. hehe, have a good time here!"

        )
        embed.set_image(url = "https://media.discordapp.net/attachments/773312837623218247/789487816756559872/iu.png?width=1352&height=676")

        server_embed = discord.Embed(
            colour = botsettings.embed_colour(),
            description = f"Welcome to **{guild.name}** {member.mention}! Have an awesome time here!"
        )
        server_embed.set_footer(text = f"Member #{len(guild.members)}", icon_url=guild.icon_url)
        server_embed.set_author(name = f"{member}", icon_url = member.avatar_url)
        server_embed.set_image(url = "https://media.discordapp.net/attachments/773312837623218247/789487816756559872/iu.png?width=1352&height=676")
        channel = await self.client.fetch_channel(763087483969208324)
        await channel.send(embed = server_embed)
        try: 
            await member.send(embed = embed)
        except:
            pass


def setup(client):
    client.add_cog(events(client))