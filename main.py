from fastapi import FastAPI
from app import services

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/analyze")
def analyze():
    return services.analyze_market()
