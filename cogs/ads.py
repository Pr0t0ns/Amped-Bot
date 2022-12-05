import discord
from discord.ext import commands
class Bot_advertisments(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ads_test(self, ctx):
        pass

def setup(client):
	client.add_cog(Bot_advertisments(client))