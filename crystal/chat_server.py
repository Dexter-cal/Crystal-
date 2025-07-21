import asyncio
import websockets
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

connected_clients = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            encrypted_message = cipher_suite.encrypt(message.encode())
            for client in connected_clients:
                if client != websocket:
                    await client.send(encrypted_message)
    finally:
        connected_clients.remove(websocket)

async def main():
    print(f"Chat server started with key: {key.decode()}")
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
