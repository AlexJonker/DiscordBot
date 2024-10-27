from discord.ext import commands
import discord

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        """Shows this help command."""
        embedVar = discord.Embed(title="Help", description="Coming Soon", color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await ctx.send(embed=embedVar)

async def setup(bot):
    await bot.add_cog(help(bot))
