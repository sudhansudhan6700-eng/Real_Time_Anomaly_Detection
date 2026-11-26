
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from pathlib import Path

app = FastAPI(
    title="Real-Time Financial Anomaly Detection API",
    description="Detect suspicious financial transactions",
    version="1.0"
)

# Load trained model
MODEL_PATH = (
    Path(__file__).resolve().parent
    / "saved_model"
    / "anomaly_detection_pipeline.joblib"
)

model_package = joblib.load(MODEL_PATH)

model = model_package["model"]
threshold = model_package["threshold"]
feature_names = model_package["feature_names"]


class Transaction(BaseModel):
    features: dict[str, float]


@app.get("/")
def home():
    return {"message": "Anomaly Detection API is running"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True
    }


@app.post("/predict")
def predict(transaction: Transaction):

    try:
        features = transaction.features

        if set(features.keys()) != set(feature_names):
            raise HTTPException(
                status_code=400,
                detail="Please provide all required transaction features."
            )

        values = np.array(
            [[features[name] for name in feature_names]]
        )

        anomaly_score = -model.decision_function(values)[0]

        is_anomaly = int(anomaly_score >= threshold)

        return {
            "prediction": is_anomaly,
            "result": "Anomaly" if is_anomaly else "Normal",
            "anomaly_score": float(anomaly_score),
            "threshold": float(threshold)
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
