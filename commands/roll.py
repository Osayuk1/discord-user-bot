from discord.ext import commands
import random

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, dice: str = "1d6"):
        try:
            rolls, limit = map(int, dice.lower().split('d'))
            result = [random.randint(1, limit) for _ in range(rolls)]
            await ctx.reply(f"🎲 Rolls: {result} Total: {sum(result)}")
        except:
            await ctx.reply("Use format NdN (example: `2d6`)")

def setup(bot):
    bot.add_cog(Roll(bot))