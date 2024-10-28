# app/preprocessing.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

def preprocess_data(data):
    # Convert IP addresses
    data['ip_address'] = data['ip_address'].apply(ip_to_integer)

    # Handle potential float format in IPs
    if data['ip_address'].dtype == 'float64':
        data['ip_address'] = data['ip_address'].astype('int64')

    # Ensure datetime columns are in the right format
    data['signup_time'] = pd.to_datetime(data['signup_time'])
    data['purchase_time'] = pd.to_datetime(data['purchase_time'])

    # Transaction frequency (Assuming you have these columns in your data)
    transaction_frequency = data.groupby(['user_id', 'purchase_time']).size().reset_index(name='frequency')
    data = data.merge(transaction_frequency, on=['user_id', 'purchase_time'], how='left')

    # Transaction velocity
    transaction_velocity = data.groupby(['user_id', 'purchase_time'])['purchase_value'].sum().reset_index(name='velocity')
    data = data.merge(transaction_velocity, on=['user_id', 'purchase_time'], how='left')

    # Time-based feature extraction
    data['hour_of_day'] = data['purchase_time'].dt.hour
    data['day_of_week'] = data['purchase_time'].dt.dayofweek
    data['time_diff'] = (data['purchase_time'] - data['signup_time']).dt.total_seconds()
    data['signup_hour'] = data['signup_time'].dt.hour
    data['signup_day_of_week'] = data['signup_time'].dt.dayofweek

    # Drop unnecessary columns (ensure these columns are in your data)
    data.drop(columns=['signup_time', 'purchase_time', 'user_id', 'device_id'], inplace=True)

    # Apply MinMax scaling
    scaler = MinMaxScaler()
    data[['purchase_value', 'age', 'ip_address', 'hour_of_day', 'day_of_week']] = scaler.fit_transform(
        data[['purchase_value', 'age', 'ip_address', 'hour_of_day', 'day_of_week']]
    )

    # One-hot encoding for categorical features
    data = pd.get_dummies(data, columns=['source', 'browser', 'sex'], drop_first=True)

    return data

def ip_to_integer(ip):
    # Ensure the IP is converted to integer correctly
    try:
        return int(ip)
    except ValueError:
        return None