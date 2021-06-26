import datetime
import discord
from discord.ext import commands
import json

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

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = "a!"

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f)
    
def setup(bot):
    bot.add_cog(command_prefix(bot))