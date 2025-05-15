from fastapi import APIRouter
from fastapi import WebSocket

ws_router = APIRouter()


@ws_router.websocket("/healthcheck")
async def healthcheck(ws: WebSocket):
    await ws.accept()
    await ws.send_json({"status": "ok"})
    await ws.close()
