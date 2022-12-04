import discord, asyncio, datetime, time, random, string
from discord.ext import commands

cog_files = ['cogs.api_commands', 'cogs.moderation', 'cogs.stat_commands', 'cogs.economy', 'cogs.fun_commands', 'cogs.ads']

TOKEN = "MTA0OTA4NTgzMTk3MDgyMDI0Ng.GAXGpY.92ssOSCUUmCAfnrgrogGqHEMW-smiHPKr8AaMU"
client = commands.Bot(command_prefix='')