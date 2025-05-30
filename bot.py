import os
import discord
from discord.ext import commands
from keep_alive import start

start()

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.reply("Pong!")

bot.run(os.getenv("TOKEN"))
