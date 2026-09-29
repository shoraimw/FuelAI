from fastapi import FastAPI

from app.simulator.client import simulator
from app.ml.predictor import predictor
from app.decision.engine import engine

app = FastAPI(
    title="FuelAI Operations Platform",
    description="AI Powered Fuel Supply Decision System"
)

@app.get("/")
def root():
    return {
        "system": "FuelAI",
        "status": "running"
    }

@app.get("/health")
def health():
    return simulator.health()

@app.get("/dashboard")
def dashboard():
    return {
        "instance": simulator.instance(),
        "depots": simulator.depots(),
        "stations": simulator.stations(),
        "metrics": simulator.metrics()
    }

@app.get("/prediction/{station}")
def prediction(station: str):
    result = predictor.predict(
        5000,
        [1000, 1200, 1300, 1500]
    )
    return {
        "station": station,
        "prediction": result
    }

@app.get("/recommend/{station}")
def recommendation(station: str):

    prediction_result = predictor.predict(
        5000,
        [1000, 1200, 1500]
    )

    return engine.generate(
        station,
        prediction_result
    )
