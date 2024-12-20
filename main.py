from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

# Initialize FastAPI app
app = FastAPI()

# Load the trained logistic regression model
try:
    model = joblib.load("logistic_regression_best.joblib")
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading the model: {e}")
    raise RuntimeError(f"Failed to load model: {e}")

# Define the input schema
class InputFeatures(BaseModel):
    area_mean: float
    area_se: float
    area_worst: float
    compactness_mean: float
    compactness_se: float
    compactness_worst: float
    concave_points_mean: float
    concave_points_se: float
    concave_points_worst: float
    concavity_mean: float
    concavity_se: float
    concavity_worst: float
    fractal_dimension_mean: float
    fractal_dimension_se: float
    fractal_dimension_worst: float
    perimeter_mean: float
    perimeter_se: float
    perimeter_worst: float
    radius_mean: float
    radius_se: float
    radius_worst: float
    smoothness_mean: float
    smoothness_se: float
    smoothness_worst: float
    symmetry_mean: float
    symmetry_se: float
    symmetry_worst: float
    texture_mean: float
    texture_se: float
    texture_worst: float

@app.get("/")
def root():
    """Root endpoint to check API health."""
    return {"message": "Breast Cancer Prediction API is up and running!"}

@app.post("/predict")
def predict(input_data: InputFeatures):
    """Endpoint to predict diagnosis based on input features."""
    try:
        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data.dict()])

        # Add feature-engineered columns
        input_df['area_to_radius_mean'] = input_df['area_mean'] / input_df['radius_mean']
        input_df['radius_mean_squared'] = input_df['radius_mean'] ** 2
        input_df['log_area_mean'] = np.log1p(input_df['area_mean'])

        # Perform prediction
        prediction = model.predict(input_df)
        diagnosis = "Malignant" if prediction[0] == 1 else "Benign"

        return {"diagnosis": diagnosis}

    except Exception as e:
        # Handle errors and return meaningful messages
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
