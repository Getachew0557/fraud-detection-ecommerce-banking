import os
import sys
# Append the correct src path for custom module imports
sys.path.append(os.path.abspath('../src'))
sys.path.append(os.path.abspath('../data'))
from data_loading import load_data
from data_preprocessing import preprocess_data, merge_ip_data
from eda import univariateAnalysis, bivariateAnalysis
from feature_engineering import perform_feature_engineering
from normalization_encoding import perform_normalization_and_encoding
from model_building import split_data, apply_smote, evaluate_models

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
    univariateAnalysis(fraud_data, creditcard_data, ip_address_data)
    bivariateAnalysis(fraud_data, creditcard_data, ip_address_data)

    # Preprocess data
    fraud_data, creditcard_data, ip_address_data = preprocess_data(fraud_data, creditcard_data, ip_address_data)

    # Merge IP data after preprocessing
    merged_data = merge_ip_data(fraud_data, ip_address_data)

    # Perform feature engineering on fraud data
    fraud_data = perform_feature_engineering(fraud_data)
    # Display the final dataset with the newly engineered features
    print("Feature engineered fraud data:")
    print(fraud_data.head())

    # Perform normalization and encoding
    fraud_data = perform_normalization_and_encoding(fraud_data)
    print(fraud_data.head())


    # Split the data into training and testing sets
    (X_train_creditcard, X_test_creditcard, y_train_creditcard, y_test_creditcard,
     X_train_fraud, X_test_fraud, y_train_fraud, y_test_fraud) = split_data(creditcard_data, fraud_data)

    # Apply SMOTE to the training data
    (X_train_creditcard_resampled, y_train_creditcard_resampled,
     X_train_fraud_resampled, y_train_fraud_resampled) = apply_smote(X_train_creditcard, y_train_creditcard,
                                                                     X_train_fraud, y_train_fraud)

    # Display value counts of the resampled data
    print("Resampled Credit Card Training Class Distribution:")
    print(y_train_creditcard_resampled.value_counts())

    print("Resampled Fraud Training Class Distribution:")
    print(y_train_fraud_resampled.value_counts())

    # Evaluate models on Credit Card and Fraud data
    auc_scores = evaluate_models(X_train_creditcard_resampled, y_train_creditcard_resampled, 
                                  X_test_creditcard, y_test_creditcard, 
                                  X_train_fraud_resampled, y_train_fraud_resampled, 
                                  X_test_fraud, y_test_fraud)
    

if __name__ == "__main__":
    main()
