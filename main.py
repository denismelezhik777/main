from fastapi import FastAPI

app = FastAPI()
TEMP = 0
PRUT = 0

@app.get("/")
async def root():
    global PRUT, TEMP
    PRUT += 1
    return PRUT, TEMP["temperature"]


@app.post("/webhook")
async def temperoutput(item: dict):
    global TEMP
    TEMP = item
    print(item)
    return {"OK": True}

