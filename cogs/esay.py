import os
import discord
from discord.ext import commands

class Embedsay:
    """Says stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def esay(self, ctx, *, text):
        """Says stuff!"""

        author = ctx.message.author
        em=discord.Embed(description=text, color=0xff00bb)
        em.set_author(name='{} says'.format(author))
        em.set_thumbnail(url=author.avatar_url)
        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=em)

def setup(bot):
    bot.add_cog(Embedsay(bot))
