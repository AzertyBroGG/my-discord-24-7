import discum as discord
import os, asyncio
from discord.ext import commands
bot = discord.Client(token = os.getenv('TOKEN'))
bot.gateway.run(auto_reconnect = True)
