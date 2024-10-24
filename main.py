import discord
from discord.ext import commands
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')


# add cogs


bot = commands.Bot(command_prefix=config.get('main', 'prefix'), intents = discord.Intents.all())


@bot.event
async def on_ready():
    print("Everything's all ready to go~")


@bot.event
async def on_message(message):
    print("The message's content was", message.content)
    await bot.process_commands(message)





@bot.command()
async def echo(ctx, *, content:str):
    '''
    Make the bot say whatever you want.
    '''
    await ctx.send(content)


class SomeCategory:
    """Category documentations"""

    @bot.command()
    async def ping(ctx):
        '''
        Ping the bot and see the latency.
        '''
        latency = bot.latency
        await ctx.send(latency)

bot.add_cog(SomeCategory())


bot.run(os.getenv("TOKEN"))
