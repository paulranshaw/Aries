import datetime
import discord
from discord.ext import commands
from mal import *

class MyAnimeList(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def anime(self, ctx, *, query):
        result = AnimeSearch(query)
        animeEmbed = discord.Embed(title=result.results[0].title, description=f"**Synopsis**\n{result.results[0].synopsis}", colour=0xe6f5ff, timestamp=datetime.datetime.utcnow())
        animeEmbed.set_thumbnail(url=result.results[0].image_url)
        animeEmbed.url = result.results[0].url
        animeEmbed.add_field(name="MyAnimeList ID", value=result.results[0].mal_id, inline=False)
        animeEmbed.add_field(name="Type", value=result.results[0].type, inline=True)
        animeEmbed.add_field(name="Score", value=result.results[0].score, inline=True)
        animeEmbed.add_field(name="Episodes", value=result.results[0].episodes, inline=True)
        await ctx.send(embed=animeEmbed)

    @commands.command()
    @commands.guild_only()
    async def manga(self, ctx, *, query):
        result = MangaSearch(query)
        mangaEmbed = discord.Embed(title=result.results[0].title, description=f"**Synopsis**\n{result.results[0].synopsis}", colour=0xe6f5ff, timestamp=datetime.datetime.utcnow())
        mangaEmbed.set_thumbnail(url=result.results[0].image_url)
        mangaEmbed.url = result.results[0].url
        mangaEmbed.add_field(name="MyAnimeList ID", value=result.results[0].mal_id, inline=False)
        mangaEmbed.add_field(name="Type", value=result.results[0].type, inline=True)
        mangaEmbed.add_field(name="Score", value=result.results[0].score, inline=True)
        mangaEmbed.add_field(name="Volumes", value=result.results[0].volumes, inline=True)
        await ctx.send(embed=mangaEmbed)

def setup(bot):
    bot.add_cog(MyAnimeList(bot))