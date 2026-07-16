from fastapi import FastAPI
from pathlib import Path
import sys


BACKEND_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BACKEND_DIR))


from velocity_detection.velocity import load_transactions, detect_velocity

app = FastAPI(
    title="Mlinzi Fraud Detection API",
    version="1.0.0",
)

@app.get("/")
def home():
    return {
        "message": "Mlinzi Fraud Detection API"
    }

@app.get("/velocity")
def velocity_detection():
    transactions = load_transactions()
    flagged = detect_velocity(transactions)
    return flagged