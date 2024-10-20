import os
import sys
# Append the correct src path for custom module imports
sys.path.append(os.path.abspath('../src'))
sys.path.append(os.path.abspath('../data'))
from data_loading import load_data
from data_preprocessing import preprocess_data, merge_ip_data
from eda import univariateAnalysis, bivariateAnalysis
from feature_engineering import perform_feature_engineering

def main():
    # Load dataset paths
    fraud_data_path = "../data/Fraud_Data.csv"
    creditcard_data_path = "../data/creditcard.csv"
    ip_address_data_path = "../data/IpAddress_to_Country.csv"

    # Load data
    fraud_data, creditcard_data, ip_address_data = load_data(
        fraud_data_path,
        creditcard_data_path,
        ip_address_data_path
    )

    # Preprocess data
    fraud_data, creditcard_data, ip_address_data = preprocess_data(fraud_data, creditcard_data, ip_address_data)
    #univariateAnalysis(fraud_data, creditcard_data, ip_address_data)
    #bivariateAnalysis(fraud_data, creditcard_data, ip_address_data)

    # Preprocess data
    fraud_data, creditcard_data, ip_address_data = preprocess_data(fraud_data, creditcard_data, ip_address_data)

    # Merge IP data after preprocessing
    merged_data = merge_ip_data(fraud_data, ip_address_data)

    # Perform feature engineering on fraud data
    fraud_data = perform_feature_engineering(fraud_data)
    # Display the final dataset with the newly engineered features
    print("Feature engineered fraud data:")
    print(fraud_data.head())
    

if __name__ == "__main__":
    main()
