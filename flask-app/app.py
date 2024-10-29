# app/serve_model.py
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
from preprocessing import preprocess_data
import pandas as pd

# Set display options to show all columns and rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.expand_frame_repr', False)  # Don't wrap the output

app = Flask(__name__)

# Load the XGBoost model
try:
    model = joblib.load('../notebooks/model/XGBoost_model_fraud.pkl')
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        json_data = request.json
        if json_data is None:
            return jsonify({'error': 'No input data provided'}), 400
        data = pd.DataFrame([json_data])
        
        # Preprocess the input data
        processed_data = preprocess_data(data)
        print("Processed Data:\n", processed_data)  # Debugging: print processed data

        # Make predictions
        prediction = model.predict(processed_data)
        
        # Return the result as JSON
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        print(f"Error during prediction: {e}")  # Log the error for debugging
        return jsonify({"error": "An internal error occurred: " + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
