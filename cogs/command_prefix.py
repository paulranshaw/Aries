import json
from cogs.embed import *
from discord.ext import commands

class command_prefix(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    def get_prefix(self, message):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        return prefixes[str(message.guild.id)]

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, *, prefix):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f)

        await Embed.embed(self, "Prefix", f":white_check_mark: Successfully set prefix to: **{prefix}**", 0x00ff00, ctx.channel)

    @prefix.error
    async def prefixError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await Embed.embed(self, "Error", ":x: User does not have permission: **administrator**!", 0xff0000, ctx.channel)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = "a!"

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f)
    
def setup(bot):
    bot.add_cog(command_prefix(bot))