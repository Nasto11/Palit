from discord.ext import commands
import discord
from cogs.utils import checks
import datetime, re
import json, asyncio
import traceback

help_attrs = dict(hidden=True)
description = """
Hello!
"""

prefix = ['!']
bot = commands.Bot(command_prefix=prefix, description=description, help_attrs=help_attrs, pm_help=True)


class Heelpp:
    """A help command what did ya think"""

    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def commands(self, ctx):
        author = ctx.message.author
        server = ctx.message.server
        channel = ctx.message.channel
        embed=discord.Embed(color=0xf600ff)
        embed.set_author(name="Palit Commands", icon_url="https://cdn.discordapp.com/avatars/299190096064937986/27e6a456fc5ce7d8bd4c6bde6047ee87.png")
        embed.add_field(name="!help", value="Displays this. What did ya' think?", inline=False)
        embed.add_field(name="!lenny", value="To be implemented.", inline=False)
        embed.add_field(name="!esay", value="To be implemented", inline=False)
        embed.set_footer(text="Made by xxx")
        await self.bot.say(author, embed=embed)
def setup(bot):
    bot.add_cog(Heelpp(bot))




