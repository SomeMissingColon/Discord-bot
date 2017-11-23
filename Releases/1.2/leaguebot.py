import requests, asyncio, discord, matchingLogic, db, lol_crawler,stringutil
from discord.ext import commands

# Personal mods


queueMatcherBot = commands.Bot(command_prefix="!", description="queueMatcher v1.2")


@queueMatcherBot.event
async def on_ready():
    print("CONNECTED")


@queueMatcherBot.command()
async def rank(*args):
    s = " "
    string_args = s.join(args)
    summonerName = string_args
    print(summonerName)
    await queueMatcherBot.say(lol_crawler.getStats(summonerName, say=True))


@queueMatcherBot.command(pass_context=True)
async def setrank(ctx):
    authorRaw = str(ctx.message.author)
    print(authorRaw)
    author, authorId, raw_message = extractMessageInfos(ctx)
    ign = raw_message.replace("!setrank ", "")

    try:
        tier, rank = lol_crawler.getStats(ign)
    except:
        await queueMatcherBot.say("There was an error getting your rank, make sure \"" + ign + "\" is valid")
        return

    full_rank = (tier + " " + rank)
    rvalue = matchingLogic.R_VALUES[full_rank]
    if db.push_myrank(authorId,author, ign, tier, rank, rvalue) == 1:
        await queueMatcherBot.say(ign + " has been set as the account of " + author + "\n" + "rank: " + full_rank)
        return
    if db.push_myrank(authorId,author, ign, tier, rank, rvalue) == 0:
        await queueMatcherBot.say("Something went wrong, try again later")
        return
    db.push_myrank(authorId,author, ign, tier, rank, rvalue)

    confirmation = (ign + " has been set as the account of " + author + "\n" + "rank: " + full_rank)
    await queueMatcherBot.say(confirmation)


@queueMatcherBot.command(pass_context=True)
async def myrank(ctx):
    author, authorId, waste = extractMessageInfos(ctx)
    try:
        raw_answer = db.pull_myrank(authorId)

    except:
        await queueMatcherBot.say(
            "You do not have a IGN registered to your account, use \"!setrank <YOUR IGN> \" to do so")
        return

    author,ign,tier,rank,waste = extractRankInfos(raw_answer)

    response = ign + ": \n" + tier + " " + rank
    await queueMatcherBot.say(response)


@queueMatcherBot.command(pass_context=True)
async def findteam(ctx):
    author, authorId, waste = extractMessageInfos(ctx)
    teamates = []
    try:
        raw_answer = db.pull_myrank(authorId)

    except:
        await queueMatcherBot.say(
            "You do not have a IGN registered to your account, use \"!setrank <YOUR IGN> \" to do so")
        return

    author, ign,tier,rank,rvalue = extractRankInfos(raw_answer)
    if matchingLogic.isLowElo(rvalue):
        rvalue_min = matchingLogic.LOW_ELO_LIMITS[tier][0]
        rvalue_max = matchingLogic.LOW_ELO_LIMITS[tier][1]

    else:
        full_rank = (tier+" "+rank)
        rvalue_min = matchingLogic.HIGH_ELO_LIMITS[tier][0]
        rvalue_max = matchingLogic.HIGH_ELO_LIMITS[tier][1]
    all_answers = db.pull_teamates(rvalue_min,rvalue_max,authorId)
    await queueMatcherBot.whisper("Following is a list with whomst you can play with")
    for row in all_answers:
        author, ign, tier, rank, waste = extractRankInfos(row)
        teamate = author + ": "+ign + "\n" + tier +" "+rank
        teamates.append(teamate)
        print(teamates)
    await queueMatcherBot.say("List of available teammates sent to your inbox")
    for teamate in teamates:
        await queueMatcherBot.whisper(teamate)

    await queueMatcherBot.whisper("##### END OF MESSAGE ####")
def extractMessageInfos(ctx):
    authorRaw = str(ctx.message.author)
    author = authorRaw.split('#')[0]
    authorId = int(authorRaw.split('#')[1])
    raw_message = ctx.message.content
    return author, authorId, raw_message


@queueMatcherBot.command()
async def spammethefuckup():
    for i in range(100):
        await queueMatcherBot.whisper("you've been spammed")


def extractRankInfos(raw_answer):
    try:
        answer = raw_answer
        author = answer[1]
        ign = answer[2]
        tier = answer[3]
        rank = answer[4]
        rvalue =answer[5]
    except:
        answer = raw_answer[0]
        author = answer[1]
        ign = answer[2]
        tier = answer[3]
        rank = answer[4]
        rvalue = answer[5]
    return author,ign,tier,rank,rvalue

@queueMatcherBot.command()
async def helpme():
    nl =  "\n"
    name = "leaguebot"
    version = "1.2"
    rank = "!rank: get someones rank in the chat"
    setrank = "!setrank: set your rank to the bots database, allowing you access to !myrank and !findteam "
    myrank = "!myrank: basically !rank, but for your rank setup in !setrank"
    findteam = "!findteam: get a list of player in the discord channel whomst used !setrank and are eligible to play rank with you"
    await queueMatcherBot.say(name+version+nl+rank+nl+setrank+nl+myrank+nl+findteam)

queueMatcherBot.run('<BOT TOKEN HERE>')
