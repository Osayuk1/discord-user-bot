import asyncio
import os
from userbot import User

from commands import ping, hello  # Import your commands
import keep_alive

keep_alive.start()

bot = User(token=os.getenv("TOKEN"), prefix="!")

@bot.command("ping")
async def _(ctx):
    await ping.run(ctx)

@bot.command("hello")
async def _(ctx):
    await hello.run(ctx)

bot.run()
