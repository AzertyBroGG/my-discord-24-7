import discum as discord
import os, asyncio
print('Запуск...')
@bot.gateway.command
def main(resp):
    if resp.event.ready_supplemental:
        user = bot.gateway.session.user
        print(f"Успешно вошел как {user['username']}")
bot = discord.Client(token = os.getenv('TOKEN'), log = False)
bot.gateway.run(auto_reconnect = True)
