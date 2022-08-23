from keep_alive import keep_alive
from discord.ext import commands
from dotenv import load_dotenv
import discord
load_dotenv()
import os

class Bot(commands.Bot):
    async def setup_hook(self):
        guild = discord.Object(id=os.getenv('GUILD_ID'))
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

        await self.load_extension('cogs.cog')

intents = discord.Intents.all()
activity = discord.Game(name='activity')
bot = Bot(command_prefix='~', intents=intents, activity=activity)

@bot.event
async def on_ready():
    print('logged in...')

bot.run(os.getenv('TOKEN'))
keep_alive()