from discord.ext import commands, tasks
from discord import app_commands, Interaction
from discord.utils import get
from helpers import *
import os

class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop.start()

    @tasks.loop(seconds=10)
    async def loop(self):
        return
    
    @app_commands.command()
    async def slash_command(self, interaction: Interaction):
        return

    @commands.command()
    async def command(self, ctx):
        return

    @commands.Cog.listener()
    async def on_message(self, message):
        return
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.channel.send(embed=error_embed(error))

async def setup(bot):
    await bot.add_cog(Cog(bot))