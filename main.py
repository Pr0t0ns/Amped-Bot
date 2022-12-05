import discord, asyncio, datetime, time, random, string, os
from discord.ext import commands
#from cogs.database import UserMySQLcommands, ServerMySQLcommands, GlobalDataMySQLcommands


TOKEN = "MTA0OTE4MDU4MzYwNTA1MTQ0Mg.Gn38qA.kgOnBsODBvrGfmfpawJBZ_Q2ELLMuZsN5TyHbw"
client = commands.Bot(command_prefix='.', intents=discord.Intents().all())

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded {filename}")


@client.event
async def on_ready():
    print("Logged in as {}".format(client.user))

async def main():
    async with client:
        await load_extensions()
        await client.start('MTA0OTE4MDU4MzYwNTA1MTQ0Mg.Gn38qA.kgOnBsODBvrGfmfpawJBZ_Q2ELLMuZsN5TyHbw')


if __name__ == "__main__":
    asyncio.run(main())
