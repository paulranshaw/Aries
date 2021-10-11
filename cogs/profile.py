import discord
from cogs.embed import Embed
from cogs.utils import time
from discord.ext import commands

class Profile(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def profile(self, ctx, *, user: discord.Member=None):
        if not user:
            user = ctx.author
        em = discord.Embed()
        em.set_thumbnail(url=user.avatar_url_as(size=128))
        em.set_author(name=user.name, icon_url=user.avatar_url)
        em.add_field(name='Username', value=user, inline=True)
        em.add_field(name='ID', value=user.id, inline=True)
        em.add_field(name='Nickname', value=user.nick, inline=True)
        em.add_field(name='Created', value=time.time_ago(user.created_at), inline=True)
        em.add_field(name='Joined', value=time.time_ago(user.joined_at), inline=True)
        em.colour = 0xe6f5ff
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Profile(bot))