import discord, asyncio, os
from discord.ext import commands
from discord_self_embed import Embed
users = []
bot = commands.Bot(command_prefix = '.', help_command = None, self_bot = True)
@bot.event
async def on_ready():
    activity = discord.Game(name="SelfBot | .help")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(bot.user.name)
    print(bot.user.id)
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author.id == bot.user.id:
        return
    if isinstance(message.channel, discord.DMChannel):
        
        if message.author.id in users:
            pass
        else:
            users.append(message.author.id)
            await message.channel.send('Привет! Я автоответчик **Azerty**...')
    
@bot.command()
async def help(ctx):
    emb = Embed(title = 'Я Азерти SelfBot')
    url = emb.generate_url()
    await ctx.send(url)
@bot.command()
async def ping(ctx):
    await ctx.send(f'Задержка бота — {round(bot.latency*1000)/1000} секунд')
bot.run(os.getenv('TOKEN'))
