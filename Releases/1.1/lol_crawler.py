import requests
def requestID(summonerName):
    url = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + summonerName + '?api_key=<YOUR TOKEN HERE>'
    getObj = requests.get(url)
    print(getObj.json())
    return getObj.json()["id"]

def requestRank(summonerId):

    url = 'https://na1.api.riotgames.com/lol/league/v3/leagues/by-summoner/' + summonerId  + '?api_key=<YOUR TOKEN HERE>'
    getObj = requests.get(url)
    print(getObj.json())
    return getObj.json()

def getStats(summonerName):
    print(str(requestID(summonerName)))
    try:
        summonerID = str(requestID(summonerName))
    except:

        return "That IGN is not valid"

    summonerInfos = requestRank(summonerID)
    try:
        tier = summonerInfos[0]['tier']
    except:
        return "This summoner is unrank, try getting at least b4 this season 8^]"

    rank = summonerInfos[0]['entries'][0]['rank']
    answer = summonerName + "\ntier: " + tier + "\nrank: " + rank
    return answer
