# dashboard/callback.py

from dash import Input, Output
import plotly.express as px

def register_callbacks(app, fraud_data):

    @app.callback(
        Output('line-chart', 'figure'),
        Input('line-chart', 'id')
    )
    def update_line_chart(_):
        # Line chart for fraud cases over time
        fraud_over_time = fraud_data[fraud_data['class'] == 1].groupby('purchase_time').size()
        fig = px.line(fraud_over_time, title="Fraud Cases Over Time")
        return fig

    @app.callback(
        Output('geo-chart', 'figure'),
        Input('geo-chart', 'id')
    )
    def update_geo_chart(_):
        # Geographical visualization of fraud by country
        fraud_by_country = fraud_data[fraud_data['class'] == 1].groupby('country').size().reset_index(name='fraud_cases')
        fig = px.choropleth(fraud_by_country, locations='country', locationmode='country names',
                            color='fraud_cases', title="Fraud Cases by Country")
        return fig

    @app.callback(
        Output('device-bar-chart', 'figure'),
        Input('device-bar-chart', 'id')
    )
    def update_device_bar_chart(_):
        # Bar chart for fraud cases by device
        fraud_by_device = fraud_data[fraud_data['class'] == 1].groupby('device_id').size().reset_index(name='fraud_cases')
        fig = px.bar(fraud_by_device, x='device_id', y='fraud_cases', title="Fraud Cases by Device")
        return fig

    @app.callback(
        Output('browser-bar-chart', 'figure'),
        Input('browser-bar-chart', 'id')
    )
    def update_browser_bar_chart(_):
        # Bar chart for fraud cases by browser
        fraud_by_browser = fraud_data[fraud_data['class'] == 1].groupby('browser').size().reset_index(name='fraud_cases')
        fig = px.bar(fraud_by_browser, x='browser', y='fraud_cases', title="Fraud Cases by Browser")
        return fig
