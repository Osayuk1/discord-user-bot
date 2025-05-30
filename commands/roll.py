import random
from discord.ext import commands

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, max_number: int = 100):
        number = random.randint(1, max_number)
        await ctx.send(f"You rolled: {number}")

async def setup(bot):
    await bot.add_cog(Roll(bot))