import discord
from discord.ext import commands
from bs4 import BeautifulSoup as bs
import requests
import json
import random
import errormsg
import extfunctions
import asyncio
import random

headers = {
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
}

class fun_main(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command(description = "[member]")
	async def hug(self, ctx, *, member : discord.Member):
		hug_gifs = [
		"https://media.discordapp.net/attachments/773312837623218247/773312872854847538/gif1.gif",
		"https://media.discordapp.net/attachments/773312837623218247/773312882280628234/gif3.gif",
		"https://media.discordapp.net/attachments/773312837623218247/773312883173490688/gif2.gif",
		"https://media.discordapp.net/attachments/773312837623218247/773312883558842428/gif4.gif",
		"https://media.discordapp.net/attachments/773312837623218247/773312886985457674/gif5.gif"
		]

		# get the top 8 GIFs for the search term


		embed = discord.Embed(
		title = f"{ctx.author.name} hugs {member.name}!",
		description = "Aww. Look at these cuties!",
		colour = discord.Colour.from_rgb(230, 138, 138)
		)

		embed.set_image(url = random.choice(hug_gifs))
		await ctx.send(embed = embed)


	@hug.error
	async def hurg_error(self, ctx, error):
		if str(error).lower() == "member is a required argument that is missing.":
			await ctx.send(embed = errormsg.shoot_embed(":broken_heart: I don't know who you want to hug!"))
			return
		await ctx.send(error)


	@commands.command(description = "[no arguments needed]")
	async def cookie(self, ctx):
		embed = discord.Embed(
		title = "Nom Nom!",
		description = "That cookie looking tasty!\nSo um. Can I have some? :point_right: :point_left:",
		colour = discord.Colour.from_rgb(230, 138, 138)
		)

		embed.set_image(url = "https://media.discordapp.net/attachments/773312837623218247/774385534717132820/cookie.gif")
		await ctx.send(embed = embed)


	@commands.command(aliases = ["8ball"], description = "[question]")
	async def _8ball(self, ctx, *, question : str):
		responses = [   "It is certain",
					    "Without a doubt",
					    "You may rely on it",
					    "Yes definitely",
					    "It is decidedly so",
					    "As I see it, yes",
					    "Most likely",
					    "Yes",
					    "Outlook good",
					    "Signs point to yes",



					    "Reply hazy try again",
					    "Better not tell you now",
					    "Ask again later",
					    "Cannot predict now",
					    "Concentrate and ask again",



					    "Don’t count on it",
					    "Outlook not so good",
					    "My sources say no",
					    "Very doubtful",
					    "My reply is no"
		]

		embed = discord.Embed(
		title = "The Magic Eight Ball!",
		description = f"**You Asked:** {question}\n**Answer:** {random.choice(responses)}",
		colour = discord.Colour.from_rgb(230, 138, 138)
		)
		await ctx.send(embed = embed)


	@commands.command(aliases = ["TorD"], description = "[no arguments needed]")
	async def truthordare(self, ctx):
		#def give_truth():

		await ctx.send(embed = errormsg.shoot_embed("Hehe. Truth or dare hmm? Go on! `Truth` or `Dare`\n*:warning: Complete at your own risk :warning:*"))
		def check(m):
			return m.author.id == ctx.author.id
		msg = await self.client.wait_for("message", check = check, timeout = 10.0)
		if str(msg.content).lower() == "truth":
			embed = discord.Embed(
				title = "You Chose Truth!",
				description = f"{extfunctions.choose_truth()}",
				colour = discord.Colour.from_rgb(230, 138, 138)
			)
			embed.set_footer(icon_url = ctx.author.avatar_url, text = f"{ctx.author}")
			await ctx.send(embed = embed)
			return

		if str(msg.content).lower() == "dare":
			embed = discord.Embed(
				title = "You Chose Dare!",
				description = f"{extfunctions.choose_dare()}",
				colour = discord.Colour.from_rgb(230, 138, 138)
			)
			embed.set_footer(icon_url = ctx.author.avatar_url, text = f"{ctx.author}")
			await ctx.send(embed = embed)
			return



	@truthordare.error
	async def truth_error(self, ctx, error):
		error = str(error).replace(" ", "")
		print("ERROR:" + " " + error)
		if str(error) == "Commandraisedanexception:TimeoutError:":
			print("TimeOutError, CODE ALERT")
			await ctx.send(embed = errormsg.shoot_embed(f":broken_heart: Timeout error, command cancelled **[**{ctx.author.mention}**]**"))






	@commands.command(description = "[member 1] [member 2]")
	async def ship(self, ctx, member1 : discord.Member, member2 : discord.Member):
		msg = await ctx.send(":three:")
		await asyncio.sleep(1.0)
		await msg.edit(content = ":two:")
		await asyncio.sleep(1.0)
		await msg.edit(content = ":one:")
		await asyncio.sleep(1.0)
		embed = discord.Embed(
			title = "Do they love each other?",
			description = f"**{member1.name}** and **{member2.name}** have a {random.randint(1, 101)}% love factor!",
			colour = discord.Colour.from_rgb(230, 138, 138))
		await msg.delete()
		bot = await self.client.fetch_user(772911474012061697)
		bot_image = bot.avatar_url
		embed.set_thumbnail(url = bot_image)
		msg = f":heart: **Matchmaking** :heart:\n:small_red_triangle_down: *`{member1.name}`*\n:small_red_triangle: *`{member2.name}`*"
		await ctx.send(msg, embed = embed)


	@commands.command(description = "[no arguments needed]")
	async def wyr(self, ctx):
		options = [
		    "Would you rather have an incredibly annoying high-pitched voice or a really deep manly voice?",
		    "Would you rather have a full-blown moustache for a year or permanently hairy legs for ten years?",
		    "Would you rather give up your phone or only wear Crocs for the rest of your life?",
		    "Would you rather clog the toilet on a first date or first day at a new job?",
		    "Would you rather have an abnormally big toe or an abnormally big ear?",
		    "Would you rather be three feet tall or eight feet tall?",
		    "Would you rather have to be naked at work for an hour or be dropped off two miles from your house whilst you're naked and you have to try and get home?",
		    "Would you rather smell like cheese (which has been left in the sun) or a hamster cage (which hasn't been cleaned for a fortnight)?",
		    "Would you rather be a mad genius or popular but dim?",
		    "Would you rather a nose that never stops growing or ears that never stop growing?"
		]

		embed = discord.Embed(
			title = "Would You Rather?",
			description = f"{random.choice(options)}",
			colour = discord.Colour.from_rgb(230, 138, 138))

		await ctx.send(embed = embed)



	@commands.command()
	async def e(self, ctx):
		embed = discord.Embed(
			title = "e",
			description = "e",
			colour = discord.Colour.from_rgb(230, 138, 138))
		await ctx.send("text", embed = embed)








		#if r.status_code == 200:
		    # load the GIFs using the urls for the smaller GIF sizes
		    #top_8gifs = json.loads(r.content)
		    #print top_8gifs
		#else:
		    #top_8gifs = None









def setup(client):
	client.add_cog(fun_main(client))
