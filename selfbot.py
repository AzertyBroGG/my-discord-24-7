import discord, asyncio, os
from discord.ext import commands
bot = commands.Bot(command_prefix = '.', self_bot = True)
@bot.event
async def on_ready():
    print(bot.user.name)
bot.run(os.getenv('TOKEN'))
