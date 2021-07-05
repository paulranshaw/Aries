import discord
from cogs.embed import *
from discord.ext import commands

class Unmute(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(mute_members=True)
    async def unmute(self, ctx, user: discord.Member, *, reason=None):
        await user.remove_roles(discord.utils.get(ctx.author.guild.roles, name="Muted"))
        if reason is None:
            await Embed.embed(self, "Unmute", f":white_check_mark: Successfully unmuted **{user}** ({user.id}).", 0x00ff00, ctx.channel)
        else:
            await Embed.embed(self, "Unmute", f":white_check_mark: Successfully unmuted **{user}** ({user.id}) for: **{reason}**.", 0x00ff00, ctx.channel)

def setup(bot):
    bot.add_cog(Unmute(bot))