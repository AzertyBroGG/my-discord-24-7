import discum as discord
import os, asyncio
print('Запуск...')
bot = discord.Client(token = os.getenv('TOKEN'), log = False)
@bot.gateway.command
def main(resp):
    if resp.event.ready_supplemental:
        user = bot.gateway.session.user
        print(f"Успешно вошел как {user['username']}")
    if resp.event.message:
        message = resp.parsed.auto()
        content = message['content']
        channel = message['channel_id']
        if content.startswith('.'):
            command = content.replace('.', '')
            if command == 'ping':
                bot.sendMessage(channel, 'Pong!')
            
bot.gateway.run(auto_reconnect = True)
