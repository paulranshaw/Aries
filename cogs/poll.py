import datetime
import discord
from discord.ext import commands

class Poll(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def poll(self, ctx, *, poll):
        pollEmbed = discord.Embed(title="Poll", description=poll, colour=0xe6f5ff, timestamp=datetime.datetime.utcnow())
        poll = await ctx.send(embed=pollEmbed)
        await poll.add_reaction("✅")
        await poll.add_reaction("❌")

def setup(bot):
    bot.add_cog(Poll(bot))