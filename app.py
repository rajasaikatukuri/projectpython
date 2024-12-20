import streamlit as st
import requests

# FastAPI endpoint URL (Replace with your Render deployment URL)
FASTAPI_URL = "https://projectpython-h775.onrender.com/predict"

# Streamlit app title
st.title("Breast Cancer Prediction App")

# App description
st.markdown("""
This app predicts whether a breast cancer tumor is **Malignant** or **Benign** based on input features.
The prediction is powered by a FastAPI backend deployed on Render.
""")

# Input fields for user
st.header("Enter Tumor Features")

# Input fields
area_mean = st.number_input("Area Mean", min_value=0.0, value=1001.0)
area_se = st.number_input("Area SE", min_value=0.0, value=20.5)
area_worst = st.number_input("Area Worst", min_value=0.0, value=1200.3)
compactness_mean = st.number_input("Compactness Mean", min_value=0.0, value=0.1)
compactness_se = st.number_input("Compactness SE", min_value=0.0, value=0.02)
compactness_worst = st.number_input("Compactness Worst", min_value=0.0, value=0.3)
concave_points_mean = st.number_input("Concave Points Mean", min_value=0.0, value=0.15)
concave_points_se = st.number_input("Concave Points SE", min_value=0.0, value=0.02)
concave_points_worst = st.number_input("Concave Points Worst", min_value=0.0, value=0.3)
concavity_mean = st.number_input("Concavity Mean", min_value=0.0, value=0.2)
concavity_se = st.number_input("Concavity SE", min_value=0.0, value=0.03)
concavity_worst = st.number_input("Concavity Worst", min_value=0.0, value=0.4)
fractal_dimension_mean = st.number_input("Fractal Dimension Mean", min_value=0.0, value=0.05)
fractal_dimension_se = st.number_input("Fractal Dimension SE", min_value=0.0, value=0.006)
fractal_dimension_worst = st.number_input("Fractal Dimension Worst", min_value=0.0, value=0.08)
perimeter_mean = st.number_input("Perimeter Mean", min_value=0.0, value=120.5)
perimeter_se = st.number_input("Perimeter SE", min_value=0.0, value=8.5)
perimeter_worst = st.number_input("Perimeter Worst", min_value=0.0, value=150.3)
radius_mean = st.number_input("Radius Mean", min_value=0.0, value=15.0)
radius_se = st.number_input("Radius SE", min_value=0.0, value=1.2)
radius_worst = st.number_input("Radius Worst", min_value=0.0, value=18.5)
smoothness_mean = st.number_input("Smoothness Mean", min_value=0.0, value=0.1)
smoothness_se = st.number_input("Smoothness SE", min_value=0.0, value=0.005)
smoothness_worst = st.number_input("Smoothness Worst", min_value=0.0, value=0.12)
symmetry_mean = st.number_input("Symmetry Mean", min_value=0.0, value=0.2)
symmetry_se = st.number_input("Symmetry SE", min_value=0.0, value=0.02)
symmetry_worst = st.number_input("Symmetry Worst", min_value=0.0, value=0.25)
texture_mean = st.number_input("Texture Mean", min_value=0.0, value=19.5)
texture_se = st.number_input("Texture SE", min_value=0.0, value=1.0)
texture_worst = st.number_input("Texture Worst", min_value=0.0, value=22.0)

# Submit button
if st.button("Predict"):
    # Create input data payload
    input_data = {
        "area_mean": area_mean,
        "area_se": area_se,
        "area_worst": area_worst,
        "compactness_mean": compactness_mean,
        "compactness_se": compactness_se,
        "compactness_worst": compactness_worst,
        "concave_points_mean": concave_points_mean,
        "concave_points_se": concave_points_se,
        "concave_points_worst": concave_points_worst,
        "concavity_mean": concavity_mean,
        "concavity_se": concavity_se,
        "concavity_worst": concavity_worst,
        "fractal_dimension_mean": fractal_dimension_mean,
        "fractal_dimension_se": fractal_dimension_se,
        "fractal_dimension_worst": fractal_dimension_worst,
        "perimeter_mean": perimeter_mean,
        "perimeter_se": perimeter_se,
        "perimeter_worst": perimeter_worst,
        "radius_mean": radius_mean,
        "radius_se": radius_se,
        "radius_worst": radius_worst,
        "smoothness_mean": smoothness_mean,
        "smoothness_se": smoothness_se,
        "smoothness_worst": smoothness_worst,
        "symmetry_mean": symmetry_mean,
        "symmetry_se": symmetry_se,
        "symmetry_worst": symmetry_worst,
        "texture_mean": texture_mean,
        "texture_se": texture_se,
        "texture_worst": texture_worst
    }

    # Send POST request to FastAPI
    try:
        response = requests.post(FASTAPI_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['diagnosis']}")
        else:
            st.error(f"Error: {response.json()['detail']}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
