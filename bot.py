import discord
import os

token = os.environ['TOKEN']

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith("hello"):
            await message.channel.send(f'Hi there {message.author}')


intents = discord.Intents.default()
intents.message_content = True

print(token)

client = Client(intents=intents)
client.run(token)
