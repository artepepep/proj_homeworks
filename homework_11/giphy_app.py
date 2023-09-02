import requests
import json

GIPHY_KEY = 'AhV2XU87boO7jvHdWnjmMxRLByk3oSUP'
GIPHY_URL = 'https://api.giphy.com/v1/gifs/search'
user_input = input("search the gif:")

resp = requests.get(
    GIPHY_URL,
    params={
        'api_key': GIPHY_KEY,
        'q': user_input,
        "limit": 1
    }
)
data = resp.json()
for gifs in data.get("data", []):
    print (gifs['url'])