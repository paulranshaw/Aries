import aiohttp
import config
import datetime
import discord
import traceback
import sys
from cogs.command_prefix import *
from discord.ext import commands

desc=''
intents = discord.Intents().all()

class Aries(commands.Bot):

    def __init__(self):
        super().__init__(intents=intents, command_prefix=command_prefix.get_prefix, description=desc, pm_help=None, case_insensitive=True, help_attrs=dict(hidden=True))
        self.load_cogs()
        self.session = aiohttp.ClientSession(loop=self.loop)

    def load_cogs(self):
        for cog in config.cogs:
            try:
                self.load_extension(cog)
            except Exception as e:
                print(f"Cog: \'{cog}\' failed to load.", file=sys.stderr)
                traceback.print_exc()

    async def on_ready(self):
        if not hasattr(self, 'uptime'):
            self.uptime = datetime.datetime.utcnow()
        print(f'Instance ready: {self.user} ({self.user.id})')

    async def on_resumed(self):
        print(f'Instance resumed: {self.user} ({self.user.id})')

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            pass
        elif isinstance(error, commands.DisabledCommand):
            pass
        elif isinstance(error, commands.BadArgument):
            pass
        elif isinstance(error, commands.CommandInvokeError):
            traceback.print_tb(error.original.__traceback__)

    @property
    def config(self):
        return __import__('config')

    def run(self):
        super().run(config.token)

if __name__ == '__main__':
    aries = Aries()
    aries.run()