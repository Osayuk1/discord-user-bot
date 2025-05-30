from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        user = ctx.author
        await ctx.reply(f"**User Info**\nName: {user.name}\nID: {user.id}\nCreated: {user.created_at}")

def setup(bot):
    bot.add_cog(Info(bot))