# app/serve_model.py
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
from preprocessing import preprocess_data

app = Flask(__name__)

# Load the XGBoost model
model = joblib.load('../notebooks/model/XGBClassifier.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        json_data = request.json
        data = pd.DataFrame([json_data])
        
        # Preprocess the input data
        processed_data = preprocess_data(data)
        
        # Make predictions
        prediction = model.predict(processed_data)
        
        # Return the result as JSON
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
