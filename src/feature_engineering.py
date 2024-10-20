import pandas as pd

def create_transaction_frequency(fraud_data):
    """Creates transaction frequency per user per day."""
    # Extract transaction date from purchase_time and normalize it
    fraud_data['transaction_date'] = fraud_data['purchase_time'].dt.normalize()

    # Count transactions per user per day (i.e., transaction frequency)
    transaction_frequency = fraud_data.groupby(['user_id', 'transaction_date']).size().reset_index(name='frequency')

    # Merge frequency back to fraud_data
    fraud_data = fraud_data.merge(transaction_frequency, on=['user_id', 'transaction_date'], how='left')

    return fraud_data


def create_transaction_velocity(fraud_data):
    """Creates transaction velocity (sum of purchase values per user per day)."""
    # Summing purchase values per user per day (i.e., transaction velocity)
    transaction_velocity = fraud_data.groupby(['user_id', 'transaction_date'])['purchase_value'].sum().reset_index(name='velocity')

    # Merge velocity back to fraud_data
    fraud_data = fraud_data.merge(transaction_velocity, on=['user_id', 'transaction_date'], how='left')

    return fraud_data


def extract_time_based_features(fraud_data):
    """Extracts time-based features such as hour of day, day of week, and time differences."""
    # Hour of Day from purchase_time
    fraud_data['hour_of_day'] = fraud_data['purchase_time'].dt.hour

    # Day of Week from purchase_time
    fraud_data['day_of_week'] = fraud_data['purchase_time'].dt.dayofweek  # Monday=0, Sunday=6

    # Time difference between signup and purchase in seconds
    fraud_data['time_diff'] = (fraud_data['purchase_time'] - fraud_data['signup_time']).dt.total_seconds()

    # Hour of signup
    fraud_data['signup_hour'] = fraud_data['signup_time'].dt.hour

    # Day of Week of signup and purchase
    fraud_data['signup_day_of_week'] = fraud_data['signup_time'].dt.dayofweek
    fraud_data['purchase_day_of_week'] = fraud_data['purchase_time'].dt.dayofweek

    return fraud_data


def drop_unused_columns(fraud_data):
    """Drops columns that are no longer needed after feature engineering."""
    fraud_data.drop(columns=['signup_time', 'purchase_time', 'transaction_date', 'user_id', 'device_id'], inplace=True)
    return fraud_data


def perform_feature_engineering(fraud_data):
    """Main function to perform all feature engineering steps."""
    fraud_data = create_transaction_frequency(fraud_data)
    fraud_data = create_transaction_velocity(fraud_data)
    fraud_data = extract_time_based_features(fraud_data)
    fraud_data = drop_unused_columns(fraud_data)
    
    return fraud_data
