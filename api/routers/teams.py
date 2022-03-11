import json
from fastapi import APIRouter
from database.mongo import get_data
from bson import json_util
from json import loads

router = APIRouter()
@router.get("/teams")
async def teams_all():
    res = get_data("data_teams", {"_id":0})
    return loads(json_util.dumps(res))

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
