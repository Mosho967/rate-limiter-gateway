# Rate Limiter Gateway

A lightweight gateway service built with **FastAPI** that implements IP-based rate limiting. Designed to protect backend services from excessive traffic, denial-of-service attacks, or abusive clients.

---

## Overview

This project enforces request limits per client IP within a configurable time window. It supports **in-memory and Redis-based tracking** and uses a modular structure to enable scaling or extending to JWT or admin-based control logic. 

---

## Use Case

This gateway can be placed in front of any backend service or microservice to protect endpoints from being overwhelmed by repeated or abusive requests. For example:

- **Public APIs**: This system could be used to prevent a single client from hitting `/search` or `/login` endpoints excessively.
- **Authentication services**: Throttle brute-force login attempts by IP.
- **Internal microservices**: Limit inter-service chatter during spikes or failures.
- **Frontend gateways**: Add lightweight rate limiting before forwarding traffic to cloud-based APIs.

By configuring environment variables, teams can adapt the gateway to enforce per-client request limits that align with system capacity and user fairness.


---



## Features

- IP-based rate limiting (token-bucket logic)
- Configurable via `.env` variables
- Optional Redis support for distributed usage
- Minimal and clean FastAPI structure
- Basic endpoint testing with `pytest`
- Modular setup for JWT, user scopes, or dashboards

---

## Technologies

- Python 3.10+
- FastAPI
- python-dotenv
- Redis
- pytest

---

## Project Structure

```
rate-limiter-gateway/
├── app/
│   ├── main.py        # API routes + limiter logic
│   └── config.py      # Env config
├── tests/
│   └── test_main.py   # Unit tests
├── .env
├── requirements.txt
└── README.md
```

---

## Getting Started

```bash
git clone https://github.com/Mosho967/rate-limiter-gateway.git
cd rate-limiter-gateway
python -m venv venv
source venv/bin/activate        # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### Setup `.env`:

```env
REQUEST_LIMIT=5
TIME_WINDOW=60
REDIS_HOST=localhost
REDIS_PORT=6379
```

### Run the dev server:

```bash
uvicorn app.main:app --reload
```

Ensure **Redis** is running before making requests.

---

## Running Tests

```bash
pytest tests/test_main.py
```

---

## API Endpoints

- **GET `/ping`** – Health check
- **GET `/limit-test`** – Rate-limited endpoint

### Success Response

```json
{ "message": "Request successful" }
```

### After Limit Exceeded

```json
{ "detail": "Rate limit exceeded. Try again later." }
```

### Example Usage:

```bash
curl http://localhost:8000/limit-test
```

---

## Future Enhancements

- JWT-based user throttling
- Retry headers with backoff delay
- Admin UI for rate monitor

---

## Author

**Mosho**  
[github.com/Mosho967](https://github.com/Mosho967)
