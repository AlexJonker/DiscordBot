from discord.ext import commands

class Ping(commands.Cog):
    """Responds with bot latency in milliseconds"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Responds with bot latency in milliseconds."""
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'Pong! 🏓 Latency: {latency}ms')

async def setup(bot):
    await bot.add_cog(Ping(bot))
