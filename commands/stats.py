from discord.ext import commands
import datetime

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.launch_time = datetime.datetime.now()

    @commands.command()
    async def stats(self, ctx):
        uptime = datetime.datetime.now() - self.bot.launch_time
        await ctx.reply(f"Uptime: {str(uptime).split('.')[0]}")

def setup(bot):
    bot.add_cog(Stats(bot))