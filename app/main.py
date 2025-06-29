from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from redis import Redis
from app.config import REQUEST_LIMIT, TIME_WINDOW, REDIS_HOST, REDIS_PORT
import time

app = FastAPI()

# Connect to Redis
redis = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/limit-test")
async def limit_test(request: Request):
    client_ip = request.client.host
    key = f"rate_limit:{client_ip}"

    current = redis.incr(key)

    if current == 1:
        redis.expire(key, TIME_WINDOW)

    if current > REQUEST_LIMIT:
        ttl = redis.ttl(key)
        # Safety fallback if key doesn't exist for some reason
        if ttl == -2:
            ttl = TIME_WINDOW
        return JSONResponse(
            status_code=429,
            content={"detail": f"Rate limit exceeded. Try again in {ttl} seconds."}
        )

    return {
        "message": "Request successful",
        "requests_left": REQUEST_LIMIT - current
    }
