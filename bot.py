import os
import discord
from discord.ext import commands
import keep_alive

keep_alive.start()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", self_bot=True, intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
