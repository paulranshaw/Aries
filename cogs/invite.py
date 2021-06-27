from cogs.embed import *
from discord.ext import commands

class Invite(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot 

    @commands.command()
    @commands.guild_only()
    async def invite(self, ctx):
        await Embed.embed(self, "Invite", "Invite [Aries](https://discord.com/api/oauth2/authorize?client_id=858724881004232724&permissions=171437510&scope=bot) to your own server!", None, ctx.channel)

def setup(bot): 
    bot.add_cog(Invite(bot))