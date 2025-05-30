import os
import discord
from discord.ext import commands
from keep_alive import start

start()  # keep_alive for UptimeRobot

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", self_bot=True, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.reply("Pong!")

bot.run(os.getenv("TOKEN"))
