import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize_data(fraud_data):
    """Normalize numerical features using Min-Max Scaling."""
    scaler = MinMaxScaler()
    fraud_data[['purchase_value', 'age', 'ip_address', 'hour_of_day', 'day_of_week']] = scaler.fit_transform(
        fraud_data[['purchase_value', 'age', 'ip_address', 'hour_of_day', 'day_of_week']]
    )
    return fraud_data

def check_unique_categories(fraud_data, categorical_features):
    """Check the number of unique categories for categorical features."""
    for feature in categorical_features:
        unique_count = fraud_data[feature].nunique()
        print(f"{feature}: {unique_count} unique categories")

def one_hot_encode(fraud_data, categorical_features):
    """Perform One-Hot Encoding for categorical features."""
    fraud_data = pd.get_dummies(fraud_data, columns=categorical_features, drop_first=True)
    return fraud_data

def perform_normalization_and_encoding(fraud_data):
    """Perform normalization and encoding on the fraud data."""
    fraud_data = normalize_data(fraud_data)
    
    categorical_features = ['source', 'browser', 'sex']
    check_unique_categories(fraud_data, categorical_features)
    
    fraud_data = one_hot_encode(fraud_data, categorical_features)

    # Save the cleaned DataFrame
    fraud_data.to_csv("../data/Fraud_cleaned.csv", index=False)

    return fraud_data
