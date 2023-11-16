import uvicorn as uv

if __name__=='__main__':
    uv.run('notes.asgi:application', host="0.0.0.0", port=8001)