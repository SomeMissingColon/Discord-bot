import stringutil
import request

def requestID(summoner_name):
    type_api= 'na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/'
    api_key = '<API KEY HERE>'
    summoner_name = stringutil.space_formator(summoner_name)
    url = stringutil.url_setter(True,type_api,summoner_name,api_key)



    return request.get_json(url)["id"] #returning id from json dict


def requestRank(summoner_id):
    type_api= 'na1.api.riotgames.com/lol/league/v3/leagues/by-summoner/'
    api_key= '<API KEY HERE>'
    url = stringutil.url_setter(True,type_api, summoner_id, api_key)
    print(url)
    return request.get_json(url) #json containing info


def getStats(summoner_name, say=False):

    try:
        summonerID = str(requestID(summoner_name))
    except:

        return "That IGN is not valid"

    summoner_infos = requestRank(summonerID)
    try:
        tier = summoner_infos[0]['tier']
    except:
        return "This summoner is unrank, try getting at least b4 this season 8^]"

    rank = summoner_infos[0]['entries'][0]['rank']
    answer = summoner_name + "\ntier: " + tier + "\nrank: " + rank
    if say == True:
        return answer
    else:
        return tier,rank
