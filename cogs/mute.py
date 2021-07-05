import asyncio
import discord
from cogs.embed import *
from discord.ext import commands

class Mute(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(mute_members=True)
    async def mute(self, ctx, user: discord.Member, time, *, reason=None):
        permissions = discord.Permissions(send_messages=False, speak=False)
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if role not in ctx.guild.roles:
            await ctx.guild.create_role(name="Muted", permissions=permissions)
            await user.add_roles(discord.utils.get(ctx.author.guild.roles, name="Muted"))
        else:
            await user.add_roles(discord.utils.get(ctx.author.guild.roles, name="Muted")) 
        if reason is None:
            await Embed.embed(self, "Mute", f":white_check_mark: Successfully muted **{user}** ({user.id}).", 0x00ff00, ctx.channel)
        else:
            await Embed.embed(self, "Mute", f":white_check_mark: Successfully muted **{user}** ({user.id}) for: **{reason}**.", 0x00ff00, ctx.channel)

        convert = {"s":1, "m":60, "h":3600, "d":86400}
        duration = int(time[0]) * convert[time[-1]]
        await asyncio.sleep(duration)

        await user.remove_roles(discord.utils.get(ctx.author.guild.roles, name="Muted"))
        await Embed.embed(self, "Unmute", f":white_check_mark: Successfully unmuted **{user}** ({user.id}) for: **Mute expired**.", 0x00ff00, ctx.channel)

    @mute.error
    async def muteError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await Embed.embed(self, "Error", ":x: User does not have permission: **mute_members**!", 0xff0000, ctx.channel)

def setup(bot):
    bot.add_cog(Mute(bot))