import discord
from discord.ext import commands
from .colors import blue
class Stat_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Embed = discord.Embed
    
    @commands.command()
    async def ping(self, ctx):
        embed = self.Embed(title=':ping_pong: Pong', description=f"Response Recieved in ({round(self.client.latency, 5)}s)", color=blue).set_footer(text="I'm Alive!")
        await ctx.reply(embed=embed)
def setup(client):
	client.add_cog(Stat_commands(client))