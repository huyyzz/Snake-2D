from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from game import SnakeGame
import json
import asyncio

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

game = SnakeGame()


FPS = 12
Temp_FPS = FPS

def getFPS():
    return FPS

def get_temp_speed():
    return Temp_FPS

def set_temp_speed(fps: int):
    global FPS
    Temp_FPS = FPS

@app.post("/speed/{fps}")
async def set_speed(fps: int):
    global FPS
    FPS = max(0, min(fps, 60))  # max 60
    return {"fps": FPS}


@app.get("/")
async def home():
    html = Path("board/index.html").read_text(encoding="utf8")
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket(ws: WebSocket):
    await ws.accept()
    async def receiver():
        while True:
            data = await ws.receive_text()
            if data in ["UP", "DOWN", "LEFT", "RIGHT"]:
                game.change_direction(data)
            elif data == "RESET":  
                game.reset()

            # if data == "STOP":
            #     if getFPS() > 0:
            #         set_temp_speed(getFPS())
            #         await set_speed(0)
            #     if getFPS() == 0:
            #         await set_speed(get_temp_speed())
    async def sender():
        while True:
            # if FPS == 0:
            #     await asyncio.sleep(0.1)
            #     continue
            game.update()
            await ws.send_text(json.dumps(game.state()))
            await asyncio.sleep(1/FPS)
    await asyncio.gather(receiver(), sender())