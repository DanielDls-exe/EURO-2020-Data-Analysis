import json
from fastapi import APIRouter
from database.mongo import get_data
from bson import json_util
from json import loads

router = APIRouter()
@router.get("/players")
async def players_all():
    res = get_data("data_players")
    return loads(json_util.dumps(res))

@router.get("/player/{name}")
async def players_data(name:str):
    res = get_data("data_players", {"name":name})
    try:
        return loads(json_util.dumps(res[0]))
    except:
        return {"mesagge": "Oh, sorry, there's been a problem! That player does not exist"}

