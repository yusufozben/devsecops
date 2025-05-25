from fastapi import FastAPI
from pydantic import BaseModel
import os
import uvicorn

app = FastAPI(
    title="DevSecOps FastAPI Application",
    description="A sample FastAPI application for DevSecOps pipeline demonstration",
    version="1.0.0"
)

class HealthResponse(BaseModel):
    status: str

class MessageResponse(BaseModel):
    message: str
    version: str
    environment: str

@app.get("/", response_model=MessageResponse)
async def read_root():
    return MessageResponse(
        message="Hello DevSecOps with FastAPI!",
        version="1.0.0",
        environment=os.getenv("ENV", "development")
    )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="healthy")

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(
        "app:app", 
        host="0.0.0.0", 
        port=int(os.getenv("PORT", 8000)),
        reload=False
    ) 