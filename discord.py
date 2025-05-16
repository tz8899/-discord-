   import discord
   from pushover import Client as PushoverClient

   # Discord Bot Token
   TOKEN = 'YOUR_BOT_TOKEN'
   # 用户ID
   USER_ID_TO_MONITOR = 某用户的dis id
   # Pushover User Key和API Token
   PUSHOVER_USER_KEY = 'YOUR_PUSHOVER_USER_KEY'
   PUSHOVER_API_TOKEN = 'YOUR_PUSHOVER_API_TOKEN'

   class MyClient(discord.Client):
       async def on_ready(self):
           print(f'Logged on as {self.user}')

       async def on_message(self, message):
           # 检查消息是否来自要监控的用户
           if message.author.id == USER_ID_TO_MONITOR:
               print(f'{message.author.name} said: {message.content}')
               # 发送推送通知
               pushover_client = PushoverClient(PUSHOVER_USER_KEY, api_token=PUSHOVER_API_TOKEN)
               pushover_client.send_message(f'{message.author.name} said: {message.content}', title='Discord Message Alert')

   client = MyClient()
   client.run(TOKEN)
