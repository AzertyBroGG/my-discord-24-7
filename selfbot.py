import discord, asyncio, os
from discord.ext import commands
bot = commands.Bot(command_prefix = '.', help_command = None, self_bot = True)
@bot.event
async def on_ready():
    activity = discord.Game(name="SelfBot | .help")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(bot.user.name)
    print(bot.user.id)
@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        await message.channel.send('._.')
@bot.command()
async def help(ctx):
    await ctx.send(embed = discord.Embed(title = 'Я Азерти', color = discord.Color.random()))
@bot.command()
async def ping(ctx):
    await ctx.send(f'Задержка бота — {round(bot.latency*1000)/1000} секунд')
bot.run(os.getenv('TOKEN'))
