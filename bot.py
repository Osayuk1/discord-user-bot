from discord.ext import commands
from discord import Intents
import os
import importlib.util
import glob
from keep_alive import keep_alive

token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

# Load cogs from commands/
for filename in glob.glob("commands/*.py"):
    spec = importlib.util.spec_from_file_location("module.name", filename)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    foo.setup(bot)

keep_alive()
bot.run(token)
