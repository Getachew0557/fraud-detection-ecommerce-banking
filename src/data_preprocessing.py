import os
import sys
import pandas as pd
# Append the correct src path for custom module imports
sys.path.append(os.path.abspath('../src'))
sys.path.append(os.path.abspath('../data'))
from data_cleaning import check_duplicates, drop_duplicates, convert_to_datetime, convert_to_int

def preprocess_data(fraud_data, creditcard_data, ip_address_data):
    """Preprocess the data by checking for missing values and cleaning."""
    
    # Statistical data description
    print(fraud_data.info())
    print(fraud_data.describe())
    print(fraud_data['class'].value_counts())

    print(ip_address_data.info())
    print(ip_address_data.describe())
    
    print(creditcard_data.info())
    print(creditcard_data.describe())

    # Handling missing values
    print("Missing values of fraud data", fraud_data.isnull().sum())
    print("Missing values of IpAddress to country", ip_address_data.isnull().sum())
    print("Missing values of Credit score data", creditcard_data.isnull().sum())

    # Check for duplicates in each dataset
    print("Fraud_Data duplicates: ", check_duplicates(fraud_data))
    print("Creditcard_Data duplicates: ", check_duplicates(creditcard_data))
    print("IpAddress_Data duplicates: ", check_duplicates(ip_address_data))

    # Remove duplicates if they exist
    creditcard_data = drop_duplicates(creditcard_data)
    print("Creditcard_Data cleaned duplicates: ", check_duplicates(creditcard_data))

    # Convert datetime columns in Fraud_Data
    fraud_data = convert_to_datetime(fraud_data, ['signup_time', 'purchase_time'])

    # Convert 'ip_address' and 'lower_bound_ip_address' to int
    fraud_data = convert_to_int(fraud_data, ['ip_address'])
    ip_address_data = convert_to_int(ip_address_data, ['lower_bound_ip_address'])

    # Verifying the changes
    print("Updated Fraud_Data data types:\n", fraud_data.dtypes)
    print("\nUpdated IpAddress_Data data types:\n", ip_address_data.dtypes)

    return fraud_data, creditcard_data, ip_address_data
