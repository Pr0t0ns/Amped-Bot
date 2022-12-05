import discord
from discord.ext import commands
class api_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Embed = discord.Embed
        

def setup(client):
	client.add_cog(api_commands(client))