import discord
from discord.ext import commands
red = 0xFF0000
blue = 0x2E64FE
yellow = 0xF7FE2E
green = 0x2EFE2E

class exception_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Embed = discord.Embed

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = self.Embed(title=":x: Unknown Command", description=f"{error}", color=red)
            await ctx.reply(embed=embed)

async def setup(client):
    await client.add_cog(exception_commands(client))