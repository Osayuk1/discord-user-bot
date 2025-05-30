from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, user=None):
        user = user or ctx.author
        await ctx.send(user.avatar.url)

async def setup(bot):
    await bot.add_cog(Avatar(bot))