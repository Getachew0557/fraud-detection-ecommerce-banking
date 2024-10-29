# preprocessing.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from imblearn.combine import SMOTETomek
from datetime import datetime
import pandas as pd

# Set display options to show all columns and rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.expand_frame_repr', False)  # Don't wrap the output

def preprocess_data(fraud_data):
    # Debugging: Print initial data
    print("Initial Data:\n", fraud_data)

    # Convert 'signup_time' and 'purchase_time' to datetime
    fraud_data['signup_time'] = pd.to_datetime(fraud_data['signup_time'])
    fraud_data['purchase_time'] = pd.to_datetime(fraud_data['purchase_time'])
    print("After datetime conversion:\n", fraud_data)

    # Convert 'ip_address' from float64 to int64
    if fraud_data['ip_address'].dtype == 'float64':
        fraud_data['ip_address'] = fraud_data['ip_address'].astype('int64')
    print("After ip_address conversion:\n", fraud_data)

    # Transaction Frequency
    fraud_data['transaction_date'] = fraud_data['purchase_time'].dt.date
    fraud_data['transaction_date'] = fraud_data['purchase_time'].dt.normalize() 
    transaction_frequency = fraud_data.groupby(['user_id', 'transaction_date']).size().reset_index(name='frequency')

    # Merge frequency back to fraud_data
    fraud_data = fraud_data.merge(transaction_frequency, on=['user_id', 'transaction_date'], how='left')

    # Transaction Velocity
    transaction_velocity = fraud_data.groupby(['user_id', 'transaction_date'])['purchase_value'].sum().reset_index(name='velocity')

    # Merge velocity back to fraud_data
    fraud_data = fraud_data.merge(transaction_velocity, on=['user_id', 'transaction_date'], how='left')

    print("After adding transaction velocity and frequency:\n", fraud_data)

    ## time based feature extraction
    #  Hour of Day
    fraud_data['hour_of_day'] = fraud_data['purchase_time'].dt.hour

    #  Day of Week
    fraud_data['day_of_week'] = fraud_data['purchase_time'].dt.dayofweek  # Monday=0, Sunday=6

    # Create new features based on datetime
    fraud_data['time_diff'] = (fraud_data['purchase_time'] - fraud_data['signup_time']).dt.total_seconds()
    fraud_data['signup_hour'] = fraud_data['signup_time'].dt.hour
    fraud_data['signup_day_of_week'] = fraud_data['signup_time'].dt.dayofweek
    fraud_data['purchase_day_of_week'] = fraud_data['purchase_time'].dt.dayofweek

    # Drop original datetime columns if they are not needed anymore
    fraud_data.drop(columns=['signup_time', 'purchase_time', 'transaction_date', 'user_id', 'device_id'], inplace=True)
    # One-Hot Encoding for categorical variables
    fraud_data = pd.get_dummies(fraud_data, columns=['source', 'browser', 'sex'], drop_first=True)

    # Ensure all columns are numeric
    fraud_data = fraud_data.apply(pd.to_numeric, errors='coerce')

    print("After feature extraction and encoding:\n", fraud_data)
        # Create a template with all expected columns
    expected_columns = ['purchase_value', 'age', 'ip_address', 'frequency', 'velocity', 
                        'hour_of_day', 'day_of_week', 'time_diff', 'signup_hour', 
                        'signup_day_of_week', 'purchase_day_of_week', 
                        'source_Direct', 'source_SEO', 'browser_FireFox', 
                        'browser_IE', 'browser_Opera', 'browser_Safari', 
                        'sex_M']
    
    # Reindex fraud_data to match expected columns, filling missing ones with 0
    fraud_data = fraud_data.reindex(columns=expected_columns, fill_value=0)


    return fraud_data
