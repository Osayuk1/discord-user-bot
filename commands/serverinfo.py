from discord.ext import commands

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        await ctx.send(f"Server name: {guild.name}\nMembers: {guild.member_count}")

async def setup(bot):
    await bot.add_cog(ServerInfo(bot))