import discord
from discord.ext import commands
class Fun_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Embed = discord.Embed
    
    @commands.command()
    async def echo(self, ctx, *, message): return await ctx.send(message)
    
def setup(client):
	client.add_cog(Fun_commands(client))