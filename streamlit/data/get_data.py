import requests
url = "http://127.0.0.1:8000"

def get_all_players():
    return requests.get(url + "/players").json()

def get_player(name):
    return requests.get(url + f"/player/{name}").json()

def get_all_name_players():
    return requests.get(url + "/players/name/all").json()

def get__all_teams():
    return requests.get(url + "/teams").json()

def get_team(name):
    return requests.get(url + f"/team/{name}").json()

def get_all_name_teams():
    return requests.get(url + "/teams/name/all").json()