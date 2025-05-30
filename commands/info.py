from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        await ctx.send(f"Logged in as {ctx.author}")

async def setup(bot):
    await bot.add_cog(Info(bot))