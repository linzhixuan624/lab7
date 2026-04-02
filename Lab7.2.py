import requests
import json


API_KEY = " "
STEAM_ID = " "

url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={API_KEY}&steamids={STEAM_ID}&format=json"

response = requests.get(url)
data = response.json()

if response.status_code == 200 and data.get('response'):
    player = data['response']['players'][0]
    print("Nickname:", player['personaname'])
    print("Steam ID:", player['steamid'])
    print("Profile Page:", player['profileurl'])
    print("Avatar:", player['avatarfull'])
    print("Online Status:", player['personastate'])
else:
    print("False")