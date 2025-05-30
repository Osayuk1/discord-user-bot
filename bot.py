
import os
import discord
from discord.ext import commands
from keepalive_server import keep_alive
import importlib.util
import pathlib

token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"ID: {bot.user.id}")

# Load all command cogs
commands_dir = pathlib.Path("commands")
for file in commands_dir.glob("*.py"):
    if file.name.startswith("_"):
        continue
    spec = importlib.util.spec_from_file_location(file.stem, file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, "setup"):
        bot.loop.create_task(mod.setup(bot))

# Keep alive
keep_alive()

# Start bot
bot.run(token)
