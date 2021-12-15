from fastapi import FastAPI

app = FastAPI()
TEMP = 0

@app.get("/")
async def root():
    return TEMP


@app.post("/webhook")
async def temperoutput(item: dict):
    TEMP = item
    return {"OK": True}

