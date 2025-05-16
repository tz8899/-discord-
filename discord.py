import discord
import requests

# Discord Bot的Token，用于验证和连接到Discord API
TOKEN = '你的dc token'
# 要监控的用户的Discord ID
USER_ID_TO_MONITOR = 被监控的dc id
# Pushover的用户密钥和API令牌，用于发送推送通知
PUSHOVER_USER_KEY = '你的key'
PUSHOVER_API_TOKEN = '你的api'

# 自定义客户端类，继承自discord.Client
class MyClient(discord.Client):
    # 当Bot成功登录时调用
    async def on_ready(self):
        print(f'Logged on as {self.user}')  # 打印Bot的用户名

    # 当有新消息时调用
    async def on_message(self, message):
        # 检查消息是否来自要监控的用户
        if message.author.id == USER_ID_TO_MONITOR:
            # 打印用户的名字和消息内容
            print(f'{message.author.name} said: {message.content}')
            # 发送推送通知
            self.send_pushover_message(f'{message.author.name} said: {message.content}')

    def send_pushover_message(self, message, title="Discord Message Alert"):
        url = "https://api.pushover.net/1/messages.json"
        data = {
            "token": PUSHOVER_API_TOKEN,
            "user": PUSHOVER_USER_KEY,
            "message": message,
            "title": title
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Notification sent successfully.")
        else:
            print("Failed to send notification.")

# 创建客户端实例并运行
client = MyClient()
client.run(TOKEN)  # 使用Bot的Token连接到Discord
