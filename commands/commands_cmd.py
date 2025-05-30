from discord.ext import commands

class CommandsList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="commands")
    async def commands_cmd(self, ctx):
        cmds = ["info", "serverinfo", "avatar", "clear", "roll", "commands", "stats", "quote"]
        await ctx.reply("Commands: " + ", ".join(cmds))

def setup(bot):
    bot.add_cog(CommandsList(bot))