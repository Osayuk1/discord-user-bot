from discord.ext import commands
import os
import glob
import importlib.util
from keep_alive import keep_alive

token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

# Load all commands from the commands folder
for filename in glob.glob("commands/*.py"):
    spec = importlib.util.spec_from_file_location("module.name", filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.setup(bot)

keep_alive()
bot.run(token)
