import asyncio
import websockets

clients = set()

async def handler(websocket):
    print("Client connected")
    clients.add(websocket)

    try:
        async for message in websocket:
            print(f"Received {message}")

            for client in clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

    finally:
        clients.remove(websocket)



async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Server started: ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())