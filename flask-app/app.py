from flask import Flask, request, jsonify, send_from_directory
import joblib
import pandas as pd
from preprocessing import preprocess_data
from flask_cors import CORS  # Import CORS to handle cross-origin requests

app = Flask(__name__, static_folder='../react-dashboard/build', static_url_path='/')
CORS(app)  # Allow cross-origin requests for all routes

# Load the ML model
try:
    model = joblib.load('../notebooks/model/XGBoost_model_fraud.pkl')
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/')
def serve():
    # Serve the React build's index.html as the root page
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_data = request.json
        if json_data is None:
            return jsonify({'error': 'No input data provided'}), 400
        data = pd.DataFrame([json_data])
        processed_data = preprocess_data(data)
        prediction = model.predict(processed_data)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/overview', methods=['GET'])
def overview():
    # Return sample data or analytics for the "Overview" page
    overview_data = {
        "total_transactions": 1000,
        "fraudulent_transactions": 45,
        "non_fraudulent_transactions": 955
    }
    return jsonify(overview_data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
