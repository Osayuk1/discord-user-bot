from discord.ext import commands

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        await ctx.reply(f"**Server Info**\nName: {guild.name}\nID: {guild.id}\nMembers: {guild.member_count}")

def setup(bot):
    bot.add_cog(ServerInfo(bot))