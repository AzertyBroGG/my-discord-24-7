import discord, os, asyncio
from discord.ext import commands
bot = discord.Client(self_bot = True)
bot.run(os.getenv('TOKEN'))
