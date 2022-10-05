import discord, os, asyncio
from discord.ext import commands
bot = commands.Bot(self_bot = True)
bot.run(os.getenv('TOKEN'))
