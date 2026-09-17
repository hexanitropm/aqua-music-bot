import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="/",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Бот запущен: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "Яруги":
        await message.channel.send("пидорасы!")

    await bot.process_commands(message)

token = os.getenv("DISCORD_TOKEN")
bot.run(token)