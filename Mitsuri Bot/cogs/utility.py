import discord
from discord.ext import commands
import errormsg
from googletrans import Translator
translator = Translator(service_urls = ['translate.google.com'])
from discord.ext.commands.cooldowns import BucketType

class u_main(commands.Cog):
	def __init__(self, client):
		self.client = client



	@commands.command(description = "[new nickname]")
	async def nick(self, ctx, *, nickname : str):
		await ctx.author.edit(nick = nickname)
		await ctx.send(embed = errormsg.shoot_embed(f"Changed your server nickname to `{nickname}`!"))

	@commands.command(description = "[no arguments needed]")
	async def ping(self, ctx):
		embed = errormsg.shoot_embed(f"Your ping is {round(self.client.latency * 1000)}ms!")
		await ctx.send(embed = embed)

	@commands.command(description = "[member]")
	async def pfp(self, ctx, member : discord.Member):
		embed = discord.Embed(
				title = f"{member.name}'s Profile Picture",
				colour = discord.Colour.from_rgb(230, 138, 138))
		embed.set_image(url = member.avatar_url)
		await ctx.send(embed = embed)
		return











def setup(client):
	client.add_cog(u_main(client))
