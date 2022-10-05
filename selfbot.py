import discum as discord
import os, asyncio
from discord.ext import commands
bot = discord.Client(self_bot = True)
bot.gateway.run(os.getenv('TOKEN'))
