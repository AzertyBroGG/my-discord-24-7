import discord, asyncio, os
from discord.ext import commands
bot = commands.Bot(command_prefix = '.', help_command = None, self_bot = True)
@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
@bot.command()
async def help(ctx):
    await ctx.send('Я Азерти')
@bot.command()
async def ping(ctx):
    await ctx.send(f'Задержка бота — {bot.latency}')
bot.run(os.getenv('TOKEN'))
