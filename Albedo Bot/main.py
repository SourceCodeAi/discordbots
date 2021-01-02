import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv() #loads env vars from .env file
token = os.getenv("CLIENT_TOKEN") #retrieves env var
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "g!", case_insensitive = True, intents = intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("Gencord is ready!")
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{client.command_prefix}help"))


for i in os.listdir("./cogs"):
    if i.endswith(".py"):
        client.load_extension(f"cogs.{i[:-3]}")


@client.command()
async def invite(ctx):
    embed = discord.Embed(
        colour = discord.Colour.blurple(),
        description = f"Thank you for Supporting {client.user.name} Bot! You can click [here](https://discord.com/api/oauth2/authorize?client_id=789975395238674463&permissions=8&scope=bot) to invite the bot to one of your servers!"
    )
    embed.set_author(name = "Bot Invite", icon_url = client.user.avatar_url)
    await ctx.send(embed = embed)

@client.command()
async def reload(ctx):
    for i in os.listdir("./cogs"):
        if i.endswith(".py"):
            client.reload_extension(f"cogs.{i[:-3]}")

    await ctx.send("Reloaded all cogs")


@client.command()
async def guilds(ctx):
    await ctx.send(f"I am in {len(client.guilds)}!")





client.run(token)