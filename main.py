from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/webhook")
async def root():
    return {}