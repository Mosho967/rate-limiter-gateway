# Rate Limiter Gateway

A lightweight gateway service built with FastAPI that implements basic IP-based rate limiting. Designed to protect backend services from excessive traffic, potential denial-of-service attacks, or abusive clients.

## Overview

This project demonstrates practical use of IP-based rate limiting using FastAPI. It tracks client IPs in memory or Redis and enforces request limits within a configurable time window. It’s a foundation for more advanced gateway control mechanisms in production-grade systems.

## Features

- IP-based rate limiting per client
- Configurable rate limit parameters via environment variables
- Redis support for distributed rate limiting
- Minimal and clean FastAPI application structure
- Basic automated endpoint testing with pytest
- Modular setup ready for JWT or admin extensions

## Technologies

- Python 3.13.5
- FastAPI
- python-dotenv
- redis
- pytest

## Project Structure

```
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

```bash
git clone https://github.com/Mosho967/rate-limiter-gateway.git
cd rate-limiter-gateway
```

Create a virtual environment and activate it:

```bash
python -m venv venv
```

**Windows**

```bash
.\venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file with the following content:

```
REQUEST_LIMIT=5
TIME_WINDOW=60
REDIS_HOST=localhost
REDIS_PORT=6379
```

Run the development server:

```bash
uvicorn app.main:app --reload
```

Make sure Redis is running before testing the rate limiter.

## Running Tests

```bash
pytest tests/test_main.py
```

## API Endpoints

- **GET `/ping`**  
  Used for health checks to ensure the server is running properly.

- **GET `/limit-test`**  
  This is the rate-limited endpoint. It tracks requests from each IP and enforces limits based on the configured environment settings.

### Example Successful Response

```json
{
  "message": "Request successful"
}
```

### After Rate Limit Exceeded

```json
{
  "detail": "Rate limit exceeded. Try again later."
}
```

## Future Enhancements

- JWT user-level throttling
- Retry headers with dynamic backoff
- Admin UI to monitor IP activity

## Author

**Mosho**

GitHub: [https://github.com/Mosho967](https://github.com/Mosho967)
