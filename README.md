# ServicePulse

REST API built with **FastAPI**, **Pydantic**, and **HTTPX** to monitor HTTP service availability and response latency.

## Features
- `GET /health`: Basic health check endpoint for the API itself.
- `POST /checks`: Asynchronous HTTP check for a target URL, returning status (`up`/`down`), HTTP status code, latency in milliseconds, timestamp, and error details when unreachable.
- Interactive API documentation via Swagger UI (`/docs`).

## Project Structure
```text
ServicePulse/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── checker.py
├── .env.example
├── .gitignore
└── requirements.txt```