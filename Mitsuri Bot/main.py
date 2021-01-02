import discord
from discord.ext import commands
import os
intents = discord.Intents.default()
import errormsg
import sqlite3
client = commands.Bot(command_prefix = "m-", intents = intents)

client.remove_command("help")

#https://stackoverflow.com/questions/59126137/how-to-change-discord-py-bot-activity



@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name=f"being cute! ❤️ | {client.command_prefix}help"))
	print("The bot is ready!")
	db = sqlite3.connect("currencydata.sqlite")
	db2 = sqlite3.connect("waifus.sqlite")
	db3 = sqlite3.connect("userwaifus.sqlite")
	c3 = db3.cursor()
	c2 = db2.cursor()
	c = db.cursor()
	c.execute("""CREATE TABLE IF NOT EXISTS usercurrency(
		user_id INTEGER,
		balance INTEGER
	)""")

	c2.execute("""CREATE TABLE IF NOT EXISTS allwaifus(
		name STRING,
		image STRING
	)""")

	c3.execute("""CREATE TABLE IF NOT EXISTS uwd(
		user_id INTEGER,
		waifuone STRING,
		waifutwo STRING,
		waifuthree STRING
	)""")
	db3.commit()
	db3.close()
	db2.commit()
	db2.close()
	db.commit()
	db.close()
	print("SQL finished")




for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")
		print(f"Loaded {filename}")



@client.command()
async def reload(ctx):
	if ctx.author.id != 691406006277898302:
		return
	for filename in os.listdir("./cogs"):
		if filename.endswith(".py"):
			client.reload_extension(f"cogs.{filename[:-3]}")
			print(f"Loaded {filename}")

	await ctx.send(embed = errormsg.shoot_noti("Reloaded all cogs"))



@client.command()
async def servericon(ctx):
	guild = ctx.guild
	embed = discord.Embed(
		colour = discord.Colour.from_rgb(230, 138, 138)
	)

	embed.set_image(url = guild.icon_url)
	await ctx.send(embed = embed)





client.run("NzcyOTExNDc0MDEyMDYxNjk3.X6Bj5w.h9b0zX8mGJvHKWSxVCwHQPNDp0Y")
