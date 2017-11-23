
def url_setter(encrypted,variance1,variance2,variance3):
    '''
    :param encripted: http/https
    :param variance1: api service
    :param variance2: identificator
    :param variance3: api key
    :return: full url for get request
    '''
    variance1 = str(variance1)
    variance2 = str(variance2)
    variance3 = str(variance3)
    if encrypted:
        url_start = "https://"
    else:
        url_start = "http://"
    variance3 = "?api_key="+variance3
    return url_start+variance1+variance2+variance3

def space_formator(string):
    return string.replace(" ","%20")