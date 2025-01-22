import requests

def checkInternetStatus():
    try:
        response = requests.get("http://google.com",timeout=5)
        return True
    except requests.ConnectionError:
        return False

if checkInternetStatus():
    print("Masz internet")
else:
    print("brak")