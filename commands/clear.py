from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount: int = 5):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Cleared {amount} messages.", delete_after=2)

async def setup(bot):
    await bot.add_cog(Clear(bot))