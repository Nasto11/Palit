from discord.ext import commands
import discord


class Clist:
    """A help command what did ya think"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def commands(self, ctx):
        author = ctx.message.author
        server = ctx.message.server
        channel = ctx.message.channel
        embed=discord.Embed(color=0xf600ff)
        embed.set_author(name="Palit Commands", icon_url="https://cdn.discordapp.com/avatars/299190096064937986/27e6a456fc5ce7d8bd4c6bde6047ee87.png")        
        embed.add_field(name="!help", value="Displays this. What did ya' think?", inline=False)
        embed.add_field(name="!summon", value="Summons the bot to your voice channel.", inline=False)
        embed.add_field(name="!play", value="Plays the music, duh.", inline=False)
        embed.add_field(name="!skip", value="Skip the music, duh.", inline=False)
        embed.add_field(name="!playing", value="Shows info about the song.", inline=False)
        embed.add_field(name="!stop", value="Stops the music, duh.", inline=False)
        embed.add_field(name="!pause", value="Pauses playing music.", inline=False)
        embed.add_field(name="!resume", value="Resumes the music.", inline=False)
        embed.add_field(name="!lenny", value="Shows a lenny.", inline=False)
        embed.add_field(name="!esay", value="Makes things you say in embeds!", inline=False)
        embed.add_field(name="!epenis", value="Shows the accurate penis size of mentioned person.", inline=False)
        embed.set_footer(text="Made by Nasto")
        await self.bot.whisper(embed=embed)

def setup(bot):
    bot.add_cog(Clist(bot))




