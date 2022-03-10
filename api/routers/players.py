import json
from fastapi import APIRouter
from database.mongo import db
from bson import json_util
from json import loads

router = APIRouter()
@router.get("/players")
async def players_all():
    res = db["data_players"].find({})
    print(res)
    return loads(json_util.dumps(res))

@router.get("/players/{name}")
async def players_data(name):
    res = db["data_players"].find({"name":name})
    return loads(json_util.dumps(res))

@router.get("/teams")
async def teams_all():
    res = db["data_teams"].find({})
    return loads(json_util.dumps(res))

@router.get("/team/{team}")
async def team_data(team):
    res = db["data_teams"].find({"team":team})
    return loads(json_util.dumps(res))
    