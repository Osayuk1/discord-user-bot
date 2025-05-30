from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send("Available commands: !ping, !avatar, !info, !serverinfo, !clear, !roll, !stats, !quote")

async def setup(bot):
    await bot.add_cog(Help(bot))