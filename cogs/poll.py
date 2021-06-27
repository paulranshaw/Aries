from cogs.embed import * 
from discord.ext import commands

class Poll(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def poll(self, ctx, *, poll):
        poll = await Embed.embed(self, "Poll", f"{poll}", None, ctx.channel)
        await poll.add_reaction("✅")
        await poll.add_reaction("❌")

def setup(bot):
    bot.add_cog(Poll(bot))