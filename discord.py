# Discord Bot的Token，用于验证和连接到Discord API
TOKEN = 'YOUR_BOT_TOKEN'
# 要监控的用户的Discord ID
USER_ID_TO_MONITOR = 需要监控的discord的id
# Pushover的用户密钥和API令牌，用于发送推送通知
PUSHOVER_USER_KEY = 'YOUR_PUSHOVER_USER_KEY'
PUSHOVER_API_TOKEN = 'YOUR_PUSHOVER_API_TOKEN'

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
            # 创建Pushover客户端实例
            pushover_client = PushoverClient(PUSHOVER_USER_KEY, api_token=PUSHOVER_API_TOKEN)
            # 发送推送通知，包含用户的名字和消息内容
            pushover_client.send_message(f'{message.author.name} said: {message.content}', title='Discord Message Alert')

# 创建客户端实例并运行
client = MyClient()
client.run(TOKEN)  # 使用Bot的Token连接到Discord
