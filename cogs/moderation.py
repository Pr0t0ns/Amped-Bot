import discord
from discord.ext import commands
class Moderation_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
def setup(client):
	client.add_cog(Moderation_commands(client))