from discord.ext import commands
import random

class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        quotes = [
            "Stay hungry, stay foolish. — Steve Jobs",
            "Be yourself; everyone else is already taken. — Oscar Wilde",
            "Simplicity is the ultimate sophistication. — Leonardo da Vinci",
            "The only limit to our realization of tomorrow is our doubts of today. — FDR"
        ]
        await ctx.reply(random.choice(quotes))

def setup(bot):
    bot.add_cog(Quote(bot))