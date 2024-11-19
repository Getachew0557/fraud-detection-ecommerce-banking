from flask import Flask, request, jsonify, send_from_directory
import joblib
import pandas as pd
from preprocessing import preprocess_data
from flask_cors import CORS

app = Flask(__name__, static_folder='../react-dashboard/build', static_url_path='/')
CORS(app)

# Load the ML model
try:
    model = joblib.load('../notebooks/model/XGBoost_model_fraud.pkl')
except Exception as e:
    print(f"Error loading model: {e}")

# Load the data
fraud_data = pd.read_csv('../data/Fraud_Data.csv')
ip_address_data = pd.read_csv('../data/IpAddress_to_Country.csv')

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/overview', methods=['GET'])
def overview():
    total_transactions = len(fraud_data)
    fraudulent_transactions = fraud_data['class'].sum()
    non_fraudulent_transactions = total_transactions - fraudulent_transactions

    overview_data = {
        "total_transactions": total_transactions,
        "fraudulent_transactions": fraudulent_transactions,
        "non_fraudulent_transactions": non_fraudulent_transactions
    }
    return jsonify(overview_data)

@app.route('/distribution', methods=['GET'])
def distribution():
    distribution_data = fraud_data['class'].value_counts().to_dict()
    return jsonify(distribution_data)

@app.route('/ip-country-distribution', methods=['GET'])
def ip_country_distribution():
    country_counts = ip_address_data['country'].value_counts().head(20).to_dict()
    return jsonify(country_counts)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
