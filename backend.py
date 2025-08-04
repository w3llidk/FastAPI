from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestData(BaseModel):
    intent: str
    payload: dict

@app.post("/run")
async def run_intent(data: RequestData):
    if data.intent == "join_lobby":
        return {"joined": True, "player": data.payload.get("player", "Unknown")}
    elif data.intent == "echo":
        return {"response": data.payload}
    return {"message": "Unhandled intent"}

@app.get("/health")
async def health():
    return {"status": "running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
