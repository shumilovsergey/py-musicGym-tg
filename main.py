from typing import Union
from pydantic import BaseModel
import asyncio
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

class Item(BaseModel):
    name: str
    price: int
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "This is py-musicGym-tg bot"}


@app.post("/bot")
async def print_request(request: Request):
    body = await request.json()
    print(body)
    
    return 
