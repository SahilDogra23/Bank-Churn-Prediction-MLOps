from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI(title="Bank Churn Prediction API")

# Load model and scaler
model = joblib.load("models/bank_churn_mlp.pkl")
scaler = joblib.load("models/bank_churn_scaler.pkl")

class CustomerData(BaseModel):
    CreditScore: float
    Age: float
    Tenure: float
    Balance: float
    NumOfProducts: float
    HasCrCard: float
    IsActiveMember: float
    EstimatedSalary: float
    Geography_Germany: int = 0
    Geography_Spain: int = 0
    Gender_Male: int = 0

@app.get("/")
def root():
    return {"status": "Bank Churn Prediction API is running ✅"}

@app.post("/predict")
def predict(data: CustomerData):
    try:
        input_array = np.array([[
            data.CreditScore, data.Age, data.Tenure, data.Balance,
            data.NumOfProducts, data.HasCrCard, data.IsActiveMember,
            data.EstimatedSalary, data.Geography_Germany,
            data.Geography_Spain, data.Gender_Male
        ]])
        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]
        return {
            "prediction": int(prediction),
            "result": "Customer will Churn ⚠️" if prediction == 1 else "Customer will Stay ✅",
            "churn_probability": round(float(probability) * 100, 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))