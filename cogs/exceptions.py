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
        elif isinstance(error, commands.MissingPermissions):
            embed = self.Embed(title=':x: Insufficent Permissions', description="Sorry, you don't have permissions to run this command", color=red)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = self.Embed(title=":x: Missing Argument/Paramater", description="It looks like your missing required data! You can run >help to figure out how to use the command", color=red)
        elif isinstance(error, commands.CommandError):
            embed = self.Embed(title=":x: Invalid Data", description="It looks like the data you might have provided is not the data needed or it is invalid!\n\n**You can run >help to figure out the correct Syntax for this command**", color=red)
        elif isinstance(error, commands.CommandOnCooldown):
            embed = self.Embed(title=":x: Command on Cooldown", description=f"{error}", color=red)
        await ctx.reply(embed=embed)
def setup(client):
    client.add_cog(exception_commands(client))