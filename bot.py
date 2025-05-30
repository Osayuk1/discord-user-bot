import os
import discord
from discord.ext import commands
from keep_alive import start

start()  # keep_alive for UptimeRobot

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.reply("Pong!")

token = os.getenv("TOKEN")
print("TOKEN:", token[:5] + "..." if token else "No token found")

bot.run(token)
