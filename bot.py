from discord.ext import commands, tasks
import discord
import random
from os import *
from itertools import cycle
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')

bot = commands.Bot(command_prefix=config.get('main', 'prefix'), intents = discord.Intents.all(), description='A simple example of bot made with Discord.py')

bot.remove_command('help')


async def load_cogs():
	for cog in listdir('./cogs'):
		if cog.endswith('.py'):
			try:
				await bot.load_extension(f'cogs.{cog[:-3]}')
				print(f'Loaded {cog}')
			except Exception as e:
				print(f'Failed to load cog {cog}: {e}')



@bot.event
async def on_ready():
	await load_cogs()
	print(f'{bot.user.name} is online and ready!')

	change_status.start()


statuslist = cycle([
    'Working in da fields',
    'Doing stuff...',
    'Browsing memes 🌐',
    'Serving the finest pings',
    'Counting binary sheep 🐑',
    'In your server, stealing your bandwidth',
    'Error 404: Status not found',
    'Beep boop, I am alive',
    'Running low on coffee ☕',
    'Upgrading to Bot v2.0',
    'Reading the lore 📖',
    'Just vibin\' 😎',
    'Calculating… still calculating…',
])



@tasks.loop(seconds=60)
async def change_status():
    await bot.change_presence(activity=discord.Game(random.choice(statuslist)))

bot.run(getenv("TOKEN"))