from cogs.embed import Embed
from discord.ext import commands

class Vote(commands.cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def vote(self, ctx):
        await Embed.embed(self, "Vote", "Please [vote](https://top.gg/bot/858724881004232724/vote) for **Aries**, it really helps! :))", None, ctx.channel)

def setup(bot):
    bot.add_cog(Vote(bot))