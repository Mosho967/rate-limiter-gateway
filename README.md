# Rate Limiter Gateway

A backend microservice built with FastAPI to enforce rate limiting on incoming API requests.

## Features

- Enforces request limits per client (e.g., 10 requests per minute)
- Prevents abuse and protects backend services from overload
- Lightweight and suitable as a gateway layer for microservice architectures
- Ready to expand with Redis, authentication, and deployment pipelines

## Project Structure

```
rate-limiter-gateway/
├── app/
│   └── main.py
├── .gitignore 
├── README.md
├── requirements.txt
```

## Getting Started

### 1. Clone the Repository

```
git clone https://github.com/Mosho967/rate-limiter-gateway.git
cd rate-limiter-gateway
```

### 2. Set Up Virtual Environment (Windows)

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run the App

```
uvicorn app.main:app --reload
```

Then open:

- http://127.0.0.1:8000/ping – test route
- http://127.0.0.1:8000/docs – Swagger API documentation

## To-Do

- [ ] Implement rate limiting logic
- [ ] Add `/limit-test` route
- [ ] Add unit tests for endpoints
- [ ] Support environment variables for configuration
- [ ] Optional: Integrate Redis for distributed rate limits
- [ ] Optional: Deploy to Render or Railway
