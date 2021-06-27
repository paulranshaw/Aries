import discord
from cogs.embed import *
from discord.ext import commands

class Ban(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        if reason is None:
            await user.ban(reason=f"{ctx.author.name}")
            await Embed.embed(self, "Ban", f":white_check_mark: Successfully banned **{user}** ({user.id}).", 0x00ff00, ctx.channel)
        else:
            await user.ban(reason=reason)
            await Embed.embed(self, "Ban", f":white_check_mark: Successfully banned **{user}** ({user.id}) for: **{reason}**.", 0x00ff00, ctx.channel)

    @ban.error
    async def banError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await Embed.embed(self, "Error", ":x: User does not have permission: **ban_members**!", 0xff0000, ctx.channel)

def setup(bot):
    bot.add_cog(Ban(bot))        