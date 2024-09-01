import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from commands import join, leave, listen, help_command

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents, application_id=os.getenv('DISCORD_APP_ID'))

    async def on_ready(self):
        await self.tree.sync()
        print(f'{self.user} olarak giriş yapıldı.')

bot = MyBot()

# Komutları bot'a ekle
bot.tree.add_command(join)
bot.tree.add_command(leave)
bot.tree.add_command(listen)
bot.tree.add_command(help_command)

bot.run(DISCORD_TOKEN)
