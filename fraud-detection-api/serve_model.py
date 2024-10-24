# serve_model.py
import json
import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model

# Initialize Flask app
app = Flask(__name__)

# Load the trained fraud detection model
model = load_model("../notebooks/model/lstm_fraud.h5")

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input data from request
        input_data = request.json
        data = np.array(input_data["data"])

        # Perform prediction using the trained model
        prediction = model.predict(data)
        prediction_label = (prediction > 0.5).astype("int32").tolist()

        # Return the prediction as JSON
        return jsonify({"prediction": prediction_label})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Start the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
