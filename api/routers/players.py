from fastapi import APIRouter
from router import players
router = APIRouter()

@router.get("/players")
async def players_data():
    return 0