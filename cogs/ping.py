# cogs/ping.py
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Responds with bot latency in milliseconds."""
        latency = round(self.bot.latency * 1000)  # Latency in ms
        await ctx.send(f'Pong! 🏓 Latency: {latency}ms')

async def setup(bot):
    await bot.add_cog(Ping(bot))
