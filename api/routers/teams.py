import json
from fastapi import APIRouter
from database.mongo import db
from bson import json_util
from json import loads

router = APIRouter()
@router.get("/teams")
async def teams_all():
    res = db["data_teams"].find({})
    return loads(json_util.dumps(res))

@router.get("/team/{team}")
async def team_data(team):
    print(team)
    res = db["data_teams"].find({"team":team})
    return []