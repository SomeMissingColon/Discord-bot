import requests, asyncio, discord
from discord.ext import commands
# Personal mods
from lol_crawler import *
from dbManager import *

# ^^^^^^^^^^^^^#


queueMatcherBot = commands.Bot(command_prefix="!", description="queueMatcher v1.1")


@queueMatcherBot.event
async def on_ready():
    print("CONNECTED")


@queueMatcherBot.command(pass_context=True)
async def setrank(ctx):
    authorRaw = str(ctx.message.author)
    author = authorRaw.split('#')[0]
    authorId = authorRaw.split('#')[1]


@queueMatcherBot.command()
async def rank(*args):
    s = " "
    string_args = s.join(args)
    summonerName = string_args
    await queueMatcherBot.say(getStats(summonerName))


queueMatcherBot.run('<BOT TOKEN GOES HERE>')
