import datetime
import discord
from discord.ext import commands

class Avatar(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def avatar(self, ctx, member: discord.Member=None):
            if member == None:
                member = ctx.author
            avatarEmbed = discord.Embed(title=f"{member.name}\'s Avatar", colour=0xe6f5ff, timestamp=datetime.datetime.utcnow())
            avatarEmbed.set_image(url=member.avatar_url)
            await ctx.send(embed=avatarEmbed)

def setup(bot):
    bot.add_cog(Avatar(bot))