import discord
from cogs.embed import *
from discord.ext import commands

class Kick(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        if reason is None:
            await user.kick(reason=f"{ctx.author.name}")
            await Embed.embed(self, "Kick", f":white_check_mark: Successfully kicked **{user}** ({user.id}).", 0x00ff00, ctx.channel)
        else:
            await user.kick(reason=reason)
            await Embed.embed(self, "Kick", f":white_check_mark: Successfully kicked **{user}** ({user.id}) for: **{reason}**.", 0x00ff00, ctx.channel)

    @kick.error
    async def kickError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await Embed.embed(self, "Error", ":x: User does not have permission: **kick_members**!", 0xff0000, ctx.channel)

def setup(bot):
    bot.add_cog(Kick(bot))