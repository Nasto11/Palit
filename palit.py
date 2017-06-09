
from discord.ext import commands
import discord
from cogs.utils import checks
import datetime, re
import json, asyncio
import copy
import logging
import traceback
import sys
from collections import Counter

description = """
Hello!
"""

try:
    import uvloop
except ImportError:
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

initial_extensions = [
    'cogs.owner',
    'cogs.help',
    'cogs.lenny',
    'cogs.esay',
]


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
help_attrs = dict(hidden=True)

prefix = ['!']
bot = commands.Bot(command_prefix=prefix, description=description, help_attrs=help_attrs, pm_help=True)
client = discord.Client()

bot.remove_command("help")


@bot.event
async def on_ready():
    print('Logged in as:')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------')
    if not hasattr(bot, 'uptime'):
        bot.uptime = datetime.datetime.utcnow()
    await bot.change_presence(game=discord.Game(name="Type !commands"))

@bot.event
async def on_resumed():
    print('Resumed from sleep...')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)




def load_credentials():
    with open('credentials.json') as f:
        return json.load(f)

if __name__ == '__main__':
    credentials = load_credentials()


    token = credentials['token']

    bot.client_id = credentials['client_id']



    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

    
bot.run(token)
