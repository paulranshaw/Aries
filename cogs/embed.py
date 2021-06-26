import discord
import datetime
from discord.ext import commands

class Embed(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    async def embed(self, title, description, channel):
        embed = discord.Embed(title=title, description=description, colour=0xe6f5ff, timestamp=datetime.datetime.utcnow())
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Embed(bot))