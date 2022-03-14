import requests
url = "http://127.0.0.1:8000"

def get_all_players():
    return requests.get(url + "/players").json()

def get_player(name):
    return requests.get(url + f"/player/{name}").json()

def get_all_name_players():
    return requests.get(url + "/players/name/all").json()

def get_stadistic_player(stadistic):
    return requests.get(url + "/player").json()

def get__all_teams():
    return requests.get(url + "/teams").json()

def get_team(name):
    return requests.get(url + f"/team/{name}").json()

def get_all_name_teams():
    return requests.get(url + "/teams/name/all").json()

def get_stadistic_team(stadistic):
    return requests.get(url + f"/team/most?estadistic={stadistic}").json()

def get_stadistic_player(stadistic):
    return requests.get(url + f"/player/most?estadistic={stadistic}").json()

def get_stadistic_player_cards(color):
    return requests.get(url + f"/player/most/cards?color={color}").json()