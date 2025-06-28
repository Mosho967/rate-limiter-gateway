import os
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from app.main import app, REQUEST_LIMIT

load_dotenv()

REQUEST_LIMIT = int(os.getenv("REQUEST_LIMIT", 5))

client = TestClient(app)

def test_limit_test_allows_until_limit():
    # Send 5 requests within rate limit
    for _ in range(REQUEST_LIMIT):
        response = client.get("/limit-test")
        assert response.status_code == 200
        assert response.json()["message"] == "Request successful"

def test_limit_test_blocks_after_limit():
    # 6th request should be blocked
    response = client.get("/limit-test")
    assert response.status_code == 429
    assert "Rate limit exceeded" in response.json()["detail"]
