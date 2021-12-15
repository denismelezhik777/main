from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(value=0.1):
    return value


@app.post("/webhook")
async def temperoutput(item):   
    return root(item)