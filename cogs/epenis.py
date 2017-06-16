import discord
import random
from discord.ext import commands

class embedpenis:
    """"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def epenis(self, *, user : discord.Member):
        state = random.getstate()
        random.seed(user.id)
        dong = "8{}D".format("=" * random.randint(0, 30))
        em=discord.Embed(description=dong, color=0xff00bb)
        em.set_author(name='{} penis size:'.format(user))
        random.setstate(state)
        await self.bot.say(embed=em)


def setup(bot):
    bot.add_cog(embedpenis(bot))
