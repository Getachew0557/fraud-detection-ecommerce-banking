# dashboard/apps.py

from dash import dcc, html
import dash_bootstrap_components as dbc

def create_layout(summary):
    layout = html.Div([
        html.H1("Fraud Detection Dashboard"),
        
        # Summary statistics
        dbc.Row([
            dbc.Col(html.Div(f"Total Transactions: {summary['total_transactions']}"), width=3),
            dbc.Col(html.Div(f"Total Fraud Cases: {summary['total_fraud_cases']}"), width=3),
            dbc.Col(html.Div(f"Fraud Percentage: {summary['fraud_percentage']}%"), width=3)
        ], className="summary-boxes"),

        # Charts and visualizations
        dbc.Row([
            dbc.Col(dcc.Graph(id='line-chart'), width=6),
            dbc.Col(dcc.Graph(id='geo-chart'), width=6)
        ]),

        dbc.Row([
            dbc.Col(dcc.Graph(id='device-bar-chart'), width=6),
            dbc.Col(dcc.Graph(id='browser-bar-chart'), width=6)
        ]),
    ])
    return layout
