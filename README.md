# Rate Limiter Gateway

A lightweight gateway service built with FastAPI that implements basic IP-based rate limiting. Designed to protect backend services from excessive traffic, potential denial-of-service attacks, or abusive clients.

---

## Overview

This project demonstrates practical use of IP-based rate limiting using FastAPI. It tracks client IPs in memory and enforces request limits within a configurable time window. It’s a foundation for more advanced gateway control mechanisms in production-grade systems.

---

## Features

- IP-based rate limiting per client  
- Configurable rate limit parameters via environment variables  
- Minimal and clean FastAPI application structure  
- Basic automated endpoint testing with pytest  
- Modular setup ready for Redis, JWT, or admin extensions  

---

## Technologies

- Python 3.13.5  
- FastAPI  
- python-dotenv  
- pytest  

```text
rate-limiter-gateway/
├── app/
│   ├── __init__.py
│   ├── main.py        # API routes and rate limiting logic
│   └── config.py      # Environment configuration
│
├── tests/
│   └── test_main.py   # Unit tests for endpoints
│
├── .env               # Environment variables (not committed)
├── requirements.txt   # Python dependencies
├── .gitignore
└── README.md
```

## Getting Started

Clone the repository:

git clone https://github.com/Mosho967/rate-limiter-gateway.git
cd rate-limiter-gateway

Create a virtual environment and activate it:

python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Create a .env file with the following content:

REQUEST_LIMIT=5
TIME_WINDOW=60

Run the development server:

uvicorn app.main:app --reload

---

## Running Tests

pytest tests/test_main.py

---

## API Endpoints

Method    Endpoint        Description
GET       /ping           Health check
GET       /limit-test     Endpoint with rate limit

Example Successful Response:

{
  "message": "Request successful"
}

After Rate Limit Exceeded:

{
  "detail": "Rate limit exceeded. Try again later."
}

---

## Future Enhancements

- Redis-based distributed rate limiting  
- JWT user-level throttling  
- Retry headers with dynamic backoff  
- Admin UI to monitor IP activity  

---

## Author

Mosho  
GitHub: https://github.com/Mosho967
