import os
import random
import datetime
from discord.ext import commands
from keep_alive import start

bot = commands.Bot(command_prefix="!", self_bot=False)

bot.launch_time = datetime.datetime.now()

start()  # start the Flask keep-alive server

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def info(ctx):
    user = ctx.author
    await ctx.reply(f"User info:\nName: {user.name}\nID: {user.id}\nCreated: {user.created_at}")

@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    await ctx.reply(f"Server info:\nName: {guild.name}\nID: {guild.id}\nMembers: {guild.member_count}")

@bot.command()
async def avatar(ctx, member: commands.MemberConverter = None):
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
    except:
        await ctx.reply("Format has to be NdN, e.g. 2d6")
        return
    result = [random.randint(1, limit) for _ in range(rolls)]
    await ctx.reply(f"Rolls: {result} Total: {sum(result)}")

@bot.command()
async def help(ctx):
    cmds = ["info", "serverinfo", "avatar", "clear", "roll", "help", "stats", "quote"]
    await ctx.reply("Commands: " + ", ".join(cmds))

@bot.command()
async def stats(ctx):
    uptime = datetime.datetime.now() - bot.launch_time
    await ctx.reply(f"Bot uptime: {str(uptime).split('.')[0]}")

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
print(f'TOKEN: "{token[:5]}..."' if token else "No token found")

bot.run(token)
