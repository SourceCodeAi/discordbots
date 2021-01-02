import os
import discord
from discord.ext import commands, tasks


class ydl_manage(commands.Cog):
	def __init__(self, client):
		self.client = client

		@tasks.loop(seconds = 30)
		async def delete_webm():
			path = "./"
			for filename in os.listdir(path):
				#print(filename)
				if filename.lower().endswith(".webm"):
					try:
						print(f"WEBM FOUND: {filename}")
						os.remove(f"{filename}")
						print("DELETED")
					except:
						pass


		delete_webm.start()





def setup(client):
	client.add_cog(ydl_manage(client))
