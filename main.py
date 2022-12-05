import discord, asyncio, datetime, time, random, string
from discord.ext import commands
from cogs.database import UserMySQLcommands, ServerMySQLcommands, GlobalDataMySQLcommands

cog_files = ['cogs.api_commands', 'cogs.moderation', 'cogs.stat_commands', 'cogs.economy', 'cogs.events', 'cogs.fun_commands', 'cogs.ads', 'cogs.exceptions']

TOKEN = ""
client = commands.Bot(command_prefix='.', intents=discord.Intents().all())

@client.event
async def on_ready():
    print("Logged in as {}".format(client.user))
    for cog in cog_files:
        try: client.load_extension(cog); print(f"Loaded Cog ({cog})")
        except Exception as err: print(f"Error Loaded cog ({cog}): {err}"); exit(69)



if __name__ == "__main__":
    client.run(TOKEN, bot=True)
