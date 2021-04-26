from discord.ext import commands
import discord

class Help(commands.Cog):
    """Cog for the help command."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx: commands.context):
        for command in self.ctx.commands:
            await ctx.send(command)

def setup(bot: commands.Bot):
    """Loads cog."""
    bot.add_cog(Help(bot))