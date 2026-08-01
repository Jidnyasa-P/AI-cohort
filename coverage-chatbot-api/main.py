from fastapi import FastAPI

app = FastAPI(title="Coverage Chatbot API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
