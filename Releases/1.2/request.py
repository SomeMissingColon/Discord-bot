import requests
def get_json(url):
    try:getObj = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Connectivity problems')
        return

    except Exception:
        print("Something went wrong, check your url")
        return
        if getObj.ok:
            access="GRANTED"
            print("successfully accessed url")
        else:
            access="DENIED"
            print("The connection was not successful")
    return getObj.json()
