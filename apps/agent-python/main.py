from fastapi import FastAPI

app = FastAPI(title="PANOS Agent")

@app.get("/health")
def health():
    return {"status": "ok"}
