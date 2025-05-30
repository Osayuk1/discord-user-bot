from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 5):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Deleted {amount} messages", delete_after=5)

def setup(bot):
    bot.add_cog(Clear(bot))