from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Esta es mi primera api."}