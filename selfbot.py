import discord, asyncio, os
from discord.ext import commands

users = []
bot = commands.Bot(command_prefix = '.', help_command = None, self_bot = True)
@bot.event
async def on_ready():
    activity = discord.Activity(name="Автоответчик включен!", status = discord.ActivityType.custom, large_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/AZERTY_keyboard_layout.JPG/1200px-AZERTY_keyboard_layout.JPG")
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
            await message.channel.send('Привет! Я автоответчик **Azerty**. \nПожалуйста, опишите вашу проблему. \nСкоро он появится в Сети...')
    
@bot.command()
async def help(ctx):
    await ctx.send('**Меню помощи МЕНЯ \nЗачем оно вам?**')
@bot.command()
async def ping(ctx):
    await ctx.send(f'**Задержка бота — ** `{round(bot.latency*1000)/1000}` **секунд**')
bot.run(os.getenv('TOKEN'))
