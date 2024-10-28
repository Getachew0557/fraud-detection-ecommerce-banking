# dashboard/app.py

from dash import Dash
from flask import Flask, jsonify
from data_load import load_data
from apps import create_layout
from callback import register_callbacks
import dash_bootstrap_components as dbc


# Flask app instance
server = Flask(__name__)

# Dash app instance
app = Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load and prepare data
fraud_data, credit_card_data, summary = load_data()

# Define API endpoints
@server.route('/api/summary', methods=['GET'])
def summary_endpoint():
    return jsonify(summary)

@server.route('/api/fraud-data', methods=['GET'])
def fraud_data_endpoint():
    return jsonify(fraud_data.to_dict())

# Dash Layout and Callbacks
app.layout = create_layout(summary)
register_callbacks(app, fraud_data)

if __name__ == '__main__':
    app.run_server(debug=True)
