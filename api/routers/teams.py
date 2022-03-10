import json
from fastapi import APIRouter
from database.mongo import get_data
from bson import json_util
from json import loads

router = APIRouter()
@router.get("/teams")
async def teams_all():
    res = get_data("data_teams")
    return loads(json_util.dumps(res))

@router.get("/team/{team}")
async def team_data(team):
    res = get_data("data_teams", {"team":team})
    try:
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "That team does not exist"}