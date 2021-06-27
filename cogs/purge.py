from cogs.embed import *
from discord.ext import commands

class Purge(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command(name="clear", pass_context=True)
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        channel = ctx.message.channel
        messages = []
        async for message in channel.history(limit=amount + 1):
              messages.append(message)
        await channel.delete_messages(messages)
        await Embed.embed(self, "Purge", f"Successfully purged **{amount}** messages!", 0x00ff00, ctx.channel)

    @purge.error
    async def purgeError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await Embed.embed(self, "Error", ":x: User does not have permission: **manage_messages**!", 0xff0000, ctx.channel)

def setup(bot):
    bot.add_cog(Purge(bot))