from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scan/{symbol}")
def scan(symbol: str):
    signals = ["BUY", "SELL", "HOLD"]
    return {
        "symbol": symbol.upper(),
        "signal": random.choice(signals),
        "entry": round(random.uniform(100, 300), 2),
        "stop_loss": round(random.uniform(90, 99), 2),
        "target": round(random.uniform(310, 350), 2),
        "confidence": random.randint(60, 90)
    }
