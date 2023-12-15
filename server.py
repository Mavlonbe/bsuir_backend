import asyncio
import uvicorn

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    config = uvicorn.Config("notes.asgi:application", host="0.0.0.0", port=23335)
    server = uvicorn.Server(config)
    loop.run_until_complete(server.serve())
