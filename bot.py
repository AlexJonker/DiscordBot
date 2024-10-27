from discord.ext import commands, tasks
import discord
import random
from os import *
from itertools import cycle
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
from python_json_config import ConfigBuilder


builder = ConfigBuilder()

config = builder.parse_config('config.json')




bot = commands.Bot(command_prefix=config.prefix, intents = discord.Intents.all())

bot.remove_command("help")


async def load_cogs():
    for cog in listdir("./cogs"):
        if cog.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{cog[:-3]}")
                print(f"Loaded {cog}")
            except Exception as e:
                print(f"Failed to load cog {cog}: {e}")



@bot.event
async def on_ready():
    await load_cogs()
    print(f"{bot.user.name} is online and ready!")

    change_status.start()

@tasks.loop(seconds=60)
async def change_status():
    await bot.change_presence(activity=discord.Game(random.choice(config.statuslist)))

bot.run(getenv("TOKEN"))
