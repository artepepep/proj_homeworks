import requests
with open('key.txt', 'r') as file:
    GIPHY_KEY = file.read()
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
data_2 = resp.json()
for gifs in data_2.get("data", []):
    print (gifs['url'])