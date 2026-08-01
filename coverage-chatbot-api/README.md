# Coverage Chatbot API

A minimal FastAPI app with a health check endpoint.

## Run locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   uvicorn main:app --reload
   ```
3. Open:
   - http://127.0.0.1:8000/health

## Endpoint

- GET /health returns:
  ```json
  {"status": "ok"}
  ```
