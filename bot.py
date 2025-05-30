import os
import random
import datetime
from discord.ext import commands
import discord
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
        pass  # Ignore unknown commands
    else:
        await ctx.reply("An error occurred.")
        print(f"Error: {error}")

@bot.command()
async def info(ctx):
    user = ctx.author
    await ctx.reply(f"**User Info**\nName: {user.name}\nID: {user.id}\nCreated: {user.created_at}")

@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    await ctx.reply(f"**Server Info**\nName: {guild.name}\nID: {guild.id}\nMembers: {guild.member_count}")

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.reply(member.avatar.url)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Deleted {amount} messages", delete_after=5)

@bot.command()
async def roll(ctx, dice: str = "1d6"):
    try:
        rolls, limit = map(int, dice.lower().split('d'))
        result = [random.randint(1, limit) for _ in range(rolls)]
        await ctx.reply(f"🎲 Rolls: {result} Total: {sum(result)}")
    except:
        await ctx.reply("Use format NdN (example: `2d6`)")

@bot.command(name="commands")
async def custom_help(ctx):
    cmds = ["info", "serverinfo", "avatar", "clear", "roll", "commands", "stats", "quote"]
    await ctx.reply("Commands: " + ", ".join(cmds))

@bot.command()
async def stats(ctx):
    uptime = datetime.datetime.now() - bot.launch_time
    await ctx.reply(f"Uptime: {str(uptime).split('.')[0]}")

@bot.command()
async def quote(ctx):
    quotes = [
        "Stay hungry, stay foolish. — Steve Jobs",
        "Be yourself; everyone else is already taken. — Oscar Wilde",
        "Simplicity is the ultimate sophistication. — Leonardo da Vinci",
        "The only limit to our realization of tomorrow is our doubts of today. — FDR"
    ]
    await ctx.reply(random.choice(quotes))

token = os.getenv("TOKEN")
if not token:
    print("TOKEN not found in environment variables")
else:
    bot.run(token)
