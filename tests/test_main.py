import os
from fastapi.testclient import TestClient
from app.main import app
from app.config import REQUEST_LIMIT  # Now pulled from config.py

client = TestClient(app)

def test_limit_test_allows_until_limit():
    for _ in range(REQUEST_LIMIT):
        response = client.get("/limit-test")
        assert response.status_code == 200
        assert response.json()["message"] == "Request successful"

def test_limit_test_blocks_after_limit():
    response = client.get("/limit-test")
    assert response.status_code == 429
    assert "Rate limit exceeded" in response.json()["detail"]

