import os
import asyncio
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

token = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f"Бот запущен: {bot.user}")
    print(f"Синхронизировано команд: {len(synced)}")

async def main():
    async with bot:
        await bot.load_extension("cogs.general")
        await bot.start(token)

asyncio.run(main())