from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()
active_connections: List[WebSocket] = []

app.add_middleware(
   CORSMiddleware,
   allow_origins = ["*"],
   allow_credentials = True,
   allow_methods = ["*"],
   allow_headers = ["*"]
)

stateValues = ["on", "off"]

@app.get("/")
async def read_root():
    return {"message": "Success"}

@app.get("/led")
async def ledState(state: str):
    if state.casefold() not in stateValues:
        return {"Error": "Wrong State Value"}
    
    for connection in active_connections:
        await connection.send_text(f"LedState: {state}")

    return {"LedState": state}


@app.websocket("/ws/esp32")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
      while True:
        data = await websocket.receive_text()
        print(f"Received data from {websocket.client.host}: {data}")
    except Exception as e:
      print(f"Error: {e}")
    finally:
      active_connections.remove(websocket)