from cogs.embed import *
from discord.ext import commands

class Help(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def help(self, ctx):
        await Embed.embed(self, "Help", "Checkout **Aries** documentation at: [Help](https://github.com/paulranshaw/aries/blob/master/README.md)", None, ctx.channel)

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))
