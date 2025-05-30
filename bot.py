import os
import datetime
from discord.ext import commands
from keep_alive import start

bot = commands.Bot(command_prefix="!", self_bot=False)
bot.launch_time = datetime.datetime.now()

start()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("You don't have permission to do that.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Missing argument.")
    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        await ctx.reply("An error occurred.")
        print(f"Error: {error}")

# Load commands from commands folder
for filename in os.listdir("./commands"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"commands.{filename[:-3]}")

token = os.getenv("TOKEN")
if not token:
    print("TOKEN not found in environment variables")
else:
    bot.run(token)
