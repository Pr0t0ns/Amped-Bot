import discord
from discord.ext import commands

red = 0xFF0000
blue = 0x2E64FE
yellow = 0xF7FE2E
green = 0x2EFE2E

class Stat_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Embed = discord.Embed
    
    @commands.command()
    async def ping(self, ctx):
        embed = self.Embed(title=':ping_pong: Pong', description=f"Response Recieved in ({round(self.client.latency, 5)}s)", color=blue).set_footer(text="I'm Alive!")
        await ctx.reply(embed=embed)

    @commands.command()
    async def membercount(self, ctx):
        true_member_count = len([m for m in ctx.guild.members if not m.bot])
        embed = self.Embed(title='Member Count', description=f"I have {true_member_count} users", color=blue).set_footer(text="Help with Slotth ;)")
        await ctx.reply(embed=embed)

async def setup(client):
    await client.add_cog(Stat_commands(client))
