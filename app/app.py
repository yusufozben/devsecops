import os
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

OPENAI_API_KEY = '123445'  # TODO: 5- secret scan OPENAI_A I_KEY

app = FastAPI(
    title="DevSecOps FastAPI Application",
    description=
    "A sample FastAPI application for DevSecOps pipeline demonstration",
    version="1.0.0")


class HealthResponse(BaseModel):
    status: str  # TODO: 1- pylint syntax error. delete tab


# TODO: 2- add blank lines for formatting error
class MessageResponse(BaseModel):
    message: str
    version: str
    environment: str


@app.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(status="ok")


class SumResponse(BaseModel):
    result: int


@app.get("/sum", response_model=SumResponse)
async def sum_two_numbers(a: int, b: int):
    return SumResponse(result=a + b)


if __name__ == "__main__":
    uvicorn.run("app:app",
                host="127.0.0.1",
                port=int(os.getenv("PORT", "8000")),
                reload=False)
