from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, member=None):
        member = member or ctx.author
        try:
            await ctx.reply(member.avatar.url)
        except AttributeError:
            await ctx.reply("Could not fetch avatar.")

def setup(bot):
    bot.add_cog(Avatar(bot))