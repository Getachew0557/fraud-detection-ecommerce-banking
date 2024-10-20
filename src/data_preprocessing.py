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

# Function to convert IP address to integer
def ip_to_integer(ip):
    try:
        return int(ip)
    except ValueError:
        return None  # Handle cases where conversion fails

# Function to merge fraud and IP address data based on bounds
def merge_ip_data(fraud_data, ip_address_data):
    # Convert IP addresses in Fraud_Data to integer
    fraud_data['ip_address'] = fraud_data['ip_address'].apply(ip_to_integer)

    # Convert lower and upper bound IP addresses in IpAddress_Data to integer if needed
    ip_address_data['lower_bound_ip_address'] = ip_address_data['lower_bound_ip_address'].apply(ip_to_integer)
    ip_address_data['upper_bound_ip_address'] = ip_address_data['upper_bound_ip_address'].apply(ip_to_integer)

    # Check if the column is in float format (it may be in scientific notation)
    if fraud_data['ip_address'].dtype == 'float64':
        fraud_data['ip_address'] = fraud_data['ip_address'].astype('int64')

    # Merge the datasets based on lower_bound_ip_address first
    merged_data = fraud_data.merge(
        ip_address_data, 
        how='left', 
        left_on='ip_address', 
        right_on='lower_bound_ip_address', 
        suffixes=('', '_country')  # Temporary suffix to avoid conflicts
    )

    # Filter to keep only rows where ip_address falls within the specified bounds
    merged_data = merged_data[
        (merged_data['ip_address'] >= merged_data['lower_bound_ip_address']) & 
        (merged_data['ip_address'] <= merged_data['upper_bound_ip_address'])
    ]

    # Drop unnecessary columns after the merge
    merged_data.drop(columns=['lower_bound_ip_address', 'upper_bound_ip_address'], inplace=True)

    # Display the merged and filtered data
    print("Merged Data Sample:")
    print(merged_data.head())
    
    return merged_data