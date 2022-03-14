import json
from fastapi import APIRouter
from database.mongo import get_data, db
from bson import json_util
from json import loads

router = APIRouter()
@router.get("/teams")
async def teams_all():
    res = get_data("data_teams")
    return loads(json_util.dumps(res))

@router.get("/team/most")
async def team_most_data(estadistic:str):
    if estadistic == 'goalscored':
        res = list(db["data_teams"].find({}, {"_id":0, "team":1,"goals_favor":1}).sort("goals_favor", -1).limit(2))
    elif estadistic == 'goalown':
        res = list(db["data_teams"].find({}, {"_id":0, "team":1,"goals_received":1}).sort("goals_received", -1).limit(2))
    elif estadistic == 'possession':
        res = list(db["data_teams"].find({}, {"_id":0, "team":1,"possession_total":1}).sort("possession_total", -1).limit(2))
    elif estadistic == 'penaltys':
        res = list(db["data_teams"].find({}, {"_id":0, "team":1,"penaltys_total":1}).sort("penaltys_total", -1).limit(2))
    elif estadistic == 'shots':
        res = list(db["data_teams"].find({}, {"_id":0, "team":1,"shots":1}).sort("shots", -1).limit(2))
    else:
        return {"mesagge": "That stadistic not exist"}
    try:   
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "Oh, sorry, there's been a problem!"}

@router.get("/team/{team}")
async def team_data(team):
    res = get_data("data_teams", {"team":team}, {"_id":0})
    try:
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "That team does not exist"}

@router.get("/team/{team}/possession")
async def team_data(team):
    res = get_data("data_teams", {"team":team}, {"_id":0, "possession_total":1})
    try:
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "That team does not exist"}

@router.get("/team/{team}/shots")
async def team_data(team):
    res = get_data("data_teams", {"team":team}, {"_id":0,"shots":1})
    try:
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "That team does not exist"}

@router.get("/team/{team}/goals/scored")
async def team_data(team):
    res = get_data("data_teams", {"team":team}, {"_id":0,"goals_favor":1})
    try:
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "That team does not exist"}

@router.get("/team/{team}/goals/received")
async def team_data(team):
    res = get_data("data_teams", {"team":team}, {"_id":0,"goals_received":1})
    try:
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "That team does not exist"}

@router.get("/team/{team}/goals/penaltys")
async def team_data(team):
    res = get_data("data_teams", {"team":team}, {"_id":0,"penaltys_total":1})
    try:
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "That team does not exist"}


@router.get("/teams/name/all")
async def teams_all_name():
    res = get_data("data_teams", {}, {"team":1, "_id": 0})
    name_teams = []
    for team in res:
        name_teams.append(team["team"])
    return name_teams

