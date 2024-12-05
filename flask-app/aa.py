from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder
from datetime import datetime

# Load the trained model
model = joblib.load('../notebooks/model/XGBoost_model_fraud.pkl')

# Initialize FastAPI app
app = FastAPI()

# Serve static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Utility functions
def convert_ip_to_int(ip_str):
    try:
        octets = ip_str.split('.')
        return int(octets[0]) * 256**3 + int(octets[1]) * 256**2 + int(octets[2]) * 256 + int(octets[3])
    except Exception:
        return None

def preprocess_input(data):
    # Create DataFrame from dictionary
    df = pd.DataFrame([data])

    # Handle IP address conversion
    df['ip_address'] = df['ip_address'].apply(lambda x: convert_ip_to_int(x) if x != 'nan' else None)
    df['lower_bound_ip_addres'] = df['lower_bound_ip_addres'].apply(lambda x: convert_ip_to_int(x) if x != 'nan' else None)
    df['upper_bound_ip_adress'] = df['upper_bound_ip_adress'].apply(lambda x: convert_ip_to_int(x) if x != 'nan' else None)

    # Ensure the columns are correctly converted to numeric values (handling missing values if any)
    df['ip_address'] = pd.to_numeric(df['ip_address'], errors='coerce')
    df['lower_bound_ip_addres'] = pd.to_numeric(df['lower_bound_ip_addres'], errors='coerce')
    df['upper_bound_ip_adress'] = pd.to_numeric(df['upper_bound_ip_adress'], errors='coerce')

    # Convert datetime fields
    df['signup_time'] = pd.to_datetime(df['signup_time'], errors='coerce')
    df['purchase_time'] = pd.to_datetime(df['purchase_time'], errors='coerce')

    # Calculate signup_purchase_diff
    df['signup_purchase_diff'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds()

    # Calculate transaction_count (dummy since we process single data)
    df['transaction_count'] = 1

    # Extract hour_of_day and day_of_week
    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.dayofweek

    # Normalize purchase_value and signup_purchase_diff
    scaler = StandardScaler()
    df[['purchase_value', 'signup_purchase_diff']] = scaler.fit_transform(df[['purchase_value', 'signup_purchase_diff']])

    # Encode categorical variables
    label_encoders = {}
    for col in ['source', 'browser', 'sex', 'country']:
        label_encoders[col] = LabelEncoder()
        df[col] = label_encoders[col].fit_transform(df[col])

    # Drop unused columns
    df.drop(columns=['device_id', 'signup_time', 'purchase_time'], inplace=True)

    return df


@app.get("/", response_class=HTMLResponse)
async def read_form():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/submit")
async def submit_form(
    user_id: int = Form(...),
    signup_time: str = Form(...),
    purchase_time: str = Form(...),
    purchase_value: float = Form(...),
    device_id: str = Form(...),
    source: str = Form(...),
    browser: str = Form(...),
    sex: str = Form(...),
    age: int = Form(...),
    ip_address: str = Form(...),
    country: str = Form(...),
    lower_bound_ip_addres: str = Form(...),
    upper_bound_ip_adress: str = Form(...)
):
    try:
        # Convert form data to dictionary
        form_data = {
            "user_id": user_id,
            "signup_time": signup_time,
            "purchase_time": purchase_time,
            "purchase_value": purchase_value,
            "device_id": device_id,
            "source": source,
            "browser": browser,
            "sex": sex,
            "age": age,
            "ip_address": ip_address,
            "country": country,
            "lower_bound_ip_addres": lower_bound_ip_addres,
            "upper_bound_ip_adress": upper_bound_ip_adress,
        }

        # Preprocess the input
        input_data = preprocess_input(form_data)

        # Align columns with model
        required_columns = [
            'user_id', 'purchase_value', 'source', 'browser', 'sex', 'age',
            'ip_address', 'country', 'lower_bound_ip_addres', 'upper_bound_ip_adress',
            'signup_purchase_diff', 'transaction_count', 'hour_of_day', 'day_of_week'
        ]
        input_data = input_data[required_columns]

        # Make prediction
        prediction = model.predict(input_data)
        fraud_probability = model.predict_proba(input_data)[0][1]  # Probability of fraud

        return {
            "prediction": int(prediction[0]),
            "fraud_probability": fraud_probability
        }

    except Exception as e:
        return {"error": str(e)}
