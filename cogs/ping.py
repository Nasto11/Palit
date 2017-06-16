import discord
from discord.ext import commands
import time
from random import choice, randint

class Ping:
    """a semi-actual ping"""

    def __init__(self,bot):
        self.bot = bot
        

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Pong."""
        t1 = time.perf_counter()
        await self.bot.send_typing(ctx.message.channel)
        t2 = time.perf_counter()
        thedata = ("**Pong.**\nTime: " + str(round((t2-t1)*1000)) + "ms")
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        data = discord.Embed(description=thedata, colour=discord.Colour(value=color))
        
        await self.bot.say(embed=data)


def setup(bot):
    bot.add_cog(Ping(bot))



