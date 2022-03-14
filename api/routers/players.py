import json
from fastapi import APIRouter
from database.mongo import get_data, db
from bson import json_util
from json import loads

router = APIRouter()
@router.get("/players")
async def players_all():
    res = get_data("data_players")
    return loads(json_util.dumps(res))

@router.get("/player/most")
async def players_most_data(estadistic:str):
    if estadistic == 'goals':
        res = list(db["data_players"].find({}, {"_id":0, "name":1,"goals":1}).sort("goals", -1).limit(2))
    elif estadistic == 'assist':
        res = list(db["data_players"].find({}, {"_id":0, "name":1,"assistance":1}).sort("assistance", -1).limit(2))
    else:
        return {"mesagge": "That stadistic not exist"}
    try:   
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "Oh, sorry, there's been a problem!"}
    

@router.get("/player/most/cards")
async def players_data(color:str):
    if color == 'yellow':
        res = list(db["data_players"].find({}, {"_id":0, "name":1,"yellow_cards":1}).sort("yellow_cards", -1).limit(2))
        return loads(json_util.dumps(res[0]))
    elif color == 'red':
        res = list(db["data_players"].find({}, {"_id":0, "name":1,"red_cards":1}).sort("red_cards", -1).limit(2))
    try:   
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "Oh, sorry, there's been a problem!"}
    

@router.get("/player/{name}")
async def players_data(name:str):
    res = get_data("data_players", {"name":name})
    try:
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "Oh, sorry, there's been a problem! That player does not exist"}



@router.get("/player/{name}/goals")
async def players_data(name:str):
    res = get_data("data_players", {"name":name}, {"_id":0, "goals":1})
    try:
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "Oh, sorry, there's been a problem! That player does not exist"}

@router.get("/players/name/all")
async def players_all_name():
    res = get_data("data_players", {}, {"name":1, "_id": 0})
    name_teams = []
    for name in res:
        name_teams.append(name["name"])
    name_teams.sort()
    return name_teams

@router.get("/player/{name}/assist")
async def players_data(name:str):
    res = get_data("data_players", {"name":name}, {"_id":0, "assistance":1})
    try:
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "Oh, sorry, there's been a problem! That player does not exist"}

@router.get("/player/{name}/cards")
async def players_data(name:str, color:str):
    if color == 'yellow':
        res = get_data("data_players", {"name":name}, {"_id":0, "yellow_cards":1})
    elif color == 'red':
        res = get_data("data_players", {"name":name}, {"_id":0, "red_cards":1})
    else:
        return {"mesagge": "That's not a valid card"}
    try:
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "Oh, sorry, there's been a problem! That player does not exist"}

@router.get("/players/name/all")
async def players_all():
    res = get_data("data_players", {}, {"name":1, "_id": 0})
    name_players = []
    for player in res:
        name_players.append(player["name"])
    name_players.sort()
    return name_players