import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import errormsg
import time
class moderation_main(commands.Cog):
	def __init__(self, client):
		self.client = client




	@commands.command(description = "[member] [reason]")
	@has_permissions(administrator = True)
	async def ban(self, ctx, member : discord.Member, *, reason = "No Reason Given"):
		if ctx.author.id == member.id:
			embed = discord.Embed(
				description = ":broken_heart: You can't ban yourself!",
				colour = discord.Colour.from_rgb(230, 138, 138))
			await ctx.send(embed = embed)
			return
		bot = await self.client.fetch_user(772911474012061697)
		bot_image = bot.avatar_url
		embed = discord.Embed(
			title = "Member Banned",
			description = f"A member has been banned by {ctx.author}",
			colour = discord.Colour.from_rgb(230, 138, 138))

		embed.add_field(name = "Banned Member", value = str(member), inline = False)
		embed.set_footer(text = f"Server - {ctx.guild.name}")
		embed.add_field(name = "Reason", value = str(reason), inline = False)

		embed.set_thumbnail(url = bot_image)
		try:
			await member.send(embed = embed)
		except:
			pass
		await member.ban(reason = reason + f"\n | Responsible Moderator: {ctx.author}")
		await ctx.send(embed = embed)


	@ban.error
	async def ban_error(self, ctx, error):
		print(error)
		if isinstance(error, commands.BadArgument):

			embed = errormsg.shoot_embed(":broken_heart: Oop! I'm confused! Please double check who you've told me to ban and why!")
			await ctx.send(embed = embed)


	@commands.command()
	async def bug(self, ctx, *, bug_report : str):
		channel = await self.client.fetch_channel(777965293284622348)
		embed = discord.Embed(
			title = "A New Bug Report Was Created!",
			description = f"```{bug_report}```",
			colour = discord.Colour.from_rgb(230, 138, 138),
			timestamp = ctx.message.created_at)

		embed.set_footer(text = str(ctx.author), icon_url = ctx.author.avatar_url)

		await ctx.send(embed = embed)
		await channel.send(embed = embed)


	@commands.command()
	async def membercount(self, ctx):
		guild = ctx.guild
		await ctx.send(embed = errormsg.shoot_noti(f"This guild has {len(guild.members)} members!"))

	@commands.command(description = "[member]")
	@has_permissions(administrator = True)
	async def userinfo(self, ctx, *, member : discord.Member):
		discrim = str(member).split("#")
		discriminator = "#" + discrim[1]
		name = str(member.name)
		roles = member.roles
		for i in roles:
			if i == ctx.guild.default_role:
				roles.remove(i)



		embed = discord.Embed(
		title = f"Information about {str(member)}",
		colour = discord.Colour.from_rgb(230, 138, 138)
		)

		roles_all = ""

		for i in roles:
			roles_all = roles_all + f" {i.mention}"

		if len(roles) == 0:
			roles_all = "No Roles"

		embed.add_field(name = "Discriminator", value = discriminator, inline = False)
		embed.add_field(name = "Name", value = name, inline = False)
		embed.add_field(name = "Roles", value = roles_all, inline = False)
		embed.set_thumbnail(url = member.avatar_url)
		await ctx.send(embed = embed)



	@commands.command()
	@has_permissions(administrator=True)
	async def clear(self, ctx, amount = 5):
		await ctx.channel.purge(limit = amount)
		msg = errormsg.shoot_embed(f":heart: Cleared {amount} Messages!")
		info = await ctx.send(embed = msg)
		time.sleep(2)
		await info.delete()



	@commands.command()
	async def botstatus(self, ctx, *, status):
		if ctx.author.id != 691406006277898302:
			return
		await self.client.change_presence(activity=discord.Game(name=status))









def setup(client):
	client.add_cog(moderation_main(client))
