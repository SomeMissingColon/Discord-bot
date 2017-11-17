import requests, asyncio, discord

client = discord.Client()

@client.event
async def on_ready():
    print ("CONNECTED")

@client.event
async def on_message(message):
    messageContent = message.content
    wordList = messageContent.split()
    if messageContent.startswith("!rank"):
        print("an actualy command")
        summonerName = messageContent.replace("!rank ", "")
        try: summonerID = str(requestID(summonerName))
        except:
            await client.send_message(message.channel, "That IGN is not valid")
            return
        summonerInfos = requestRank(summonerID)
        try: tier = summonerInfos[0]['tier']
        except:
            await client.send_message(message.channel,
                                      "This summoner is unrank, try getting at least b4 this season 8^]")
            return

        rank = summonerInfos[0]['entries'][0]['rank']
        answer = summonerName + "\ntier: " + tier + "\nrank: " + rank
        await client.send_message(message.channel, answer)
def requestID(summonerName):
    url = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + summonerName + '?api_key=<api key goes here>
    getObj = requests.get(url)
    return getObj.json()["id"]





def requestRank(summonerId):
    url = 'https://na1.api.riotgames.com/lol/league/v3/leagues/by-summoner/' + summonerId  + '?api_key=<api key goes here>
    getObj = requests.get(url)
    return getObj.json()


client.run('<Bot token goes there>')
