import requests

url = "https://free-api-live-football-data.p.rapidapi.com/football-get-list-all-team"
querystring = {"leagueid": "42"}
headers = {
        "x-rapidapi-key": "3be01a29a9msh1147fa36f6934f8p13aa60jsn802d2dd1cc9f",
        "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com",
    }

response = requests.get(url, headers=headers, params=querystring).json()
data = response["response"]["list"]

for item in data:
    print(item["name"])