import discord
from discord.ext import commands


def shoot_embed(msg):
	embed = discord.Embed(
		description = msg,
		colour = discord.Colour.from_rgb(230, 138, 138))

	return embed


def shoot_noti(msg):
	embed = discord.Embed(
		description = msg,
		colour = discord.Colour.from_rgb(230, 138, 138))

	return embed



class errors(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		print(str(error))




def setup(client):
	client.add_cog(errors(client))
