from discord.ext import commands
import platform

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx):
        await ctx.send(f"Python version: {platform.python_version()}")

async def setup(bot):
    await bot.add_cog(Stats(bot))