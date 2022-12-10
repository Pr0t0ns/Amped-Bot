import discord
from discord.ext import commands
from discord.utils import find
import random
from .colors import blue
class event_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Embed = discord.Embed

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        embed = self.Embed(title=f":crown: Amped is Here!", description=f"Thank you for adding me to **{guild.name}** to get a list of some of the commands run .help", color=blue).set_footer(text=":)")
        general = find(lambda x: x.name == 'general' or x.name == "chat",  guild.text_channels)
        if general and general.permissions_for(guild.me).send_messages:
            await general.send(embed=embed)
        else:
            try:
                send_here = guild.text_channels[random.randint(0, int(len(guild.text_channels)))]
                await send_here.send(embed=embed)
            except Exception:
                return
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if self.client.user.mentioned_in(message):
            embed = self.Embed(title=f":robot: Server Prefix", description='My server prefix is "**>**"', color=blue).set_footer(text='Hello :)')
            await message.channel.send(embed=embed)
def setup(client):
	client.add_cog(event_commands(client))