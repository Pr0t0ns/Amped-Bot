import discord
from discord.ext import commands
from .colors import blue
class Commandz(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Embed = discord.Embed

    @commands.command()
    async def funhelp(self, ctx):
        embed = self.Embed(title="Help Command for Fun Commands", description='Here is the list of fun commands\nNote: **[] = Required Paramater | () = Optional Paramater**', color=blue)
        embed = embed.add_field(name='>echo [message]', value='Echos message in same channel command was ran in', inline=False)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def help(self, ctx):
        embed = self.Embed(title="Help Command", description='Here is the list of the basic commands\nNote: **[] = Required Paramater | () = Optional Paramater**', color=blue)
        embed = embed.add_field(name=">help", value="Runs this command!", inline=True)
        embed = embed.add_field(name=">ping", value="Responds with bot's Latency", inline=True)
        embed = embed.add_field(name='>ban [@user|userid] (reason)', value='Bans user mentioned with reason if reason is provided', inline=False)
        embed = embed.add_field(name=">unban [user#9999]", value='Unbans user mentioned', inline=False)
        embed = embed.add_field(name='>kick [@user|userid] (reason)', value='Kicks mentioned user with reason if reason is provided', inline=False)
        embed = embed.add_field(name=">role [@user|userid] [@role|roleid]", value="Adds or Removes role mentioned from user mentioned depending if the user has the role or doesn't have the role already.\n\nExample: If I run **>role @Pr0t0n @Developer** and Pr0t0n has the role already it will remove it and same way vise versa", inline=False)
        embed = embed.add_field(name='>purge [amount]', value='Deletes amount of messages specified in channel command is ran in', inline=False)
        embed = embed.add_field(name='>nuke (#channel)', value='Deletes and Recreates channel with same permissions and name! (another way of purging messages)', inline=False)
        embed = embed.add_field(name='>funhelp', value='returns a bunch of fun commands you can use', inline=False)    
        await ctx.reply(embed=embed)
def setup(client):
	client.add_cog(Commandz(client))