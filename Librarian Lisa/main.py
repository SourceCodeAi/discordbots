import discord
from discord.ext import commands
import os
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "lisa ", case_insensitive = True, intents = intents)


@client.event
async def on_ready():
    print(f"{client.user.name} is ready!")

for x in os.listdir("./cogs"):
    if x.endswith(".py"):
        client.load_extension(f"cogs.{x[:-3]}")
        print(f"Loaded: {x}")

client.run("Nzc2MTE1MjYxMDg1MzE5MTg3.X6wLqQ.5Hu4NnrLenP-jUjPAEFhfAoXErA")