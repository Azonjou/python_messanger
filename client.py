import asyncio
import websockets


async def send_message(websocket):
    while True:
        message = await asyncio.to_thread(input, "You: ")
        if message:
            await websocket.send(message)


async def receive_message(websocket):
    try:
        async for message in websocket:
            print(f"\r\033[KServer: {message}\nYou: ", end="", flush=True)
    except websockets.exceptions.ConnectionClosed:
        print("\nDisconnected from server")


async def main():
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("WS connected")
        await asyncio.gather(
            send_message(websocket),
            receive_message(websocket),
        )


asyncio.run(main())