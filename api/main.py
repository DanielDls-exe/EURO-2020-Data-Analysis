from fastapi import FastAPI
from routers import players, stage, teams
app = FastAPI()
app.include_router(players.router)
app.include_router(teams.router)

@app.get("/")
async def root():
    return {"message":"Bienvenidos a el analisis de datos de la Euro 2020."}


