import discord
from discord.ext import commands
class Economy_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
    


def setup(client):
	client.add_cog(Economy_commands(client))