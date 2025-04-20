from fastapi import FastAPI, Request, HTTPException
from bucket import Bucket
from fastapi.responses import JSONResponse
import random

app = FastAPI()


buckets = {}
flowers = ["🌷", "💐", "🪷", "🪻", "🌺", "🌼", "🌸", "🌻"]

CAPACITY = 3          
REFILL_RATE = 1         

def get_client_ip(request: Request):
    return request.client.host

@app.middleware("http")
async def rate_limiter(request: Request, call_next):
    client_ip = get_client_ip(request)

    if client_ip not in buckets:
        buckets[client_ip] = Bucket(CAPACITY, REFILL_RATE)

    bucket = buckets[client_ip]

    if not bucket.allow_request():
        return JSONResponse(
            status_code=429,
            content={"message": "😴"}
        )

    response = await call_next(request)
    return response

@app.get("/flower")
def get_data():
    return {"message": random.choice(flowers)}

@app.get("/")
def root():
    return {"message": "Welcome to the rate-limited API!"}
