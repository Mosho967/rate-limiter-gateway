import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time
from collections import defaultdict

load_dotenv()


app = FastAPI()

# Stores request timestamps per IP address
request_log = defaultdict(list)

# Rate limit settings from .env
REQUEST_LIMIT = int(os.getenv("REQUEST_LIMIT", 5))     # number of allowed requests
TIME_WINDOW = int(os.getenv("TIME_WINDOW", 60)) 


@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/limit-test")
async def limit_test(request: Request):
    client_ip = request.client.host
    current_time = time.time()

    # Get previous request times for this IP
    request_times = request_log[client_ip]

    # Filter out timestamps older than the time window
    request_times = [t for t in request_times if current_time - t < TIME_WINDOW]

    # Update the log with filtered times
    request_log[client_ip] = request_times

    if len(request_times) >= REQUEST_LIMIT:
        return JSONResponse(
            status_code=429,
            content={"detail": "Rate limit exceeded. Try again later."}
        )

    # Add current request timestamp
    request_log[client_ip].append(current_time)

    return {"message": "Request successful"}


