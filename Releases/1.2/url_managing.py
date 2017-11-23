import requests

def get(url):
    try: return requests.get(url)
    except requests.exceptions.ConnectionError: print("Website down or wrong url")
    except requests.exceptions.MissingSchema: print("Invalid Url")
    else: print("Something went wrong")
    return


