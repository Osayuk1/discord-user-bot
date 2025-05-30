from discord.ext import commands
import os
import glob
import importlib.util
import asyncio
from keepalive_server import keep_alive  # updated import

token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

async def load_cogs():
    for filename in glob.glob("commands/*.py"):
        spec = importlib.util.spec_from_file_location("module.name", filename)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        await mod.setup(bot)

async def main():
    await load_cogs()
    keep_alive()
    await bot.start(token)

asyncio.run(main())
