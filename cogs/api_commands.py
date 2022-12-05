import discord
from discord.ext import commands
class api_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Embed = discord.Embed
        

async def setup(client):
    await client.add_cog(api_commands(client))