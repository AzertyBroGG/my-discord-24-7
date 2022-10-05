import discum as discord
import os, asyncio

bot = discord.Client(token = os.getenv('TOKEN'), log = False)
bot.gateway.run(auto_reconnect = True)
