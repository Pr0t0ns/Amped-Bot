import discord
from discord.ext import commands
from .colors import red
class exception_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Embed = discord.Embed

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = self.Embed(title=":x: Unknown Command", description=f"{error}", color=red)
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(exception_commands(client))