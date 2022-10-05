import discord, asyncio, os
from discord.ext import commands
bot = commands.Bot(command_prefix = '.', help_command = None, self_bot = True)
@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
@bot.command()
async def help(ctx):
    await ctx.send(embed = discord.Embed(title = 'Я Азерти', color = discord.Color.random()))
@bot.command()
async def ping(ctx):
    await ctx.send(f'Задержка бота — {round(bot.latency*1000):1000} секунд')
bot.run(os.getenv('TOKEN'))
