import discord
from cogs.embed import *
from discord.ext import commands 
    
class BannedUser(commands.Converter):
    async def convert(self, ctx, argument):
        bans = await ctx.guild.bans()
        try:
            user_id = int(argument, base=10)
            entity = discord.utils.find(lambda u: u.user.id == user_id, bans)
        except ValueError:
            entity = discord.utils.find(lambda u: str(u.user) == argument, bans)
        if entity is None:
            raise commands.BadArgument(":warning: This member isn\'t banned.")
        return entity
    
class Unban(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: BannedUser, *, reason=None):
        bans = await ctx.guild.bans()
        for user in bans:
            await ctx.guild.unban(user.user, reason=reason)
            if reason is not None:
                await Embed.embed(self, "Unban", f":white_check_mark: Successfully unbanned **{user}** ({user.id}).", 0x00ff00, ctx.channel)
            else:
                await Embed.embed(self, "Unban", f":white_check_mark: Successfully unbanned **{user}** ({user.id}).", 0x00ff00, ctx.channel)

    @unban.error
    async def unbanError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await Embed.embed(self, "Error", ":x: User does not have permission: **ban_members**!", 0xff0000, ctx.channel)

def setup(bot):
    bot.add_cog(Unban(bot))