from fastapi import FastAPI, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from starlette.requests import Request
import os
import requests
import json
from const import BASE_URL





app = FastAPI()

app.mount("/static", StaticFiles(directory="build"), name="static")



def send_message(chat_id, text, reply_markup=None):
    url = f'{BASE_URL}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': json.dumps(reply_markup) if reply_markup else None
    }
    response = requests.post(url, data=data)
    return response.json()

def send_inline_button_message(chat_id):
    text = 'Привет! Заходи в мой магазинчик! 👇'
    inline_keyboard = {
        'inline_keyboard': [
            [
                {'text': 'Магазинчик Шумилова', 'url': 'https://t.me/sh_musicGym_bot/shop24x7'}
            ]
        ]
    }
    send_message(chat_id, text, inline_keyboard)





@app.get("/")
def read_root():
    return {"Hello": "This is py-musicGym-tg bot"}


@app.post("/bot")
async def print_request(request: Request):
    body = await request.json()
    chat_id = body["message"]["chat"]["id"]
    send_inline_button_message(chat_id=chat_id)
    
    
    return 


@app.get("/test", response_class=HTMLResponse)
def read_root():
    # Read and return the content of index.html from the build folder
    index_path = os.path.join("build", "index.html")
    with open(index_path, "r", encoding="utf-8") as file:
        content = file.read()
    return HTMLResponse(content=content)