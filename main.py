import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="/",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Бот запущен: {bot.user}")


token = os.getenv("DISCORD_TOKEN")
bot.run(token)