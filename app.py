import asyncio
import websockets
connected = set()
async def hello(websocket, path):
    connected.add(websocket)
    try:
        while True:
            msg = await websocket.recv()
            name,data = msg.split("0u0")
            for web in connected:
                if web != websocket:
                    await web.send(msg)
                    print(f"{name} > {data}")
    except:
        print("connection disconnected")
    finally:
        # Unregister.
        connected.remove(websocket)

start_server = websockets.serve(hello, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()