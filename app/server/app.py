from fastapi import FastAPI
from app.server.routes.player import router as PlayerRouter

app = FastAPI()

app.include_router(PlayerRouter, tags=["Player"], prefix="/player")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to my players API"}
