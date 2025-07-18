import os
from dotenv import load_dotenv

load_dotenv()

# Rate limit settings from .env
REQUEST_LIMIT = int(os.getenv("REQUEST_LIMIT", 5))     # number of allowed requests
TIME_WINDOW = int(os.getenv("TIME_WINDOW", 60))        # time window in seconds
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))