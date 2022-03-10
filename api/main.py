from fastapi import FastAPI
from routers import players, stage, teams
app = FastAPI()
app.include_router(players.router)
app.include_router(teams.router)

@app.get("/")
async def root():
    return {"message":"Welcome to the Euro 2020 data analysis"}


