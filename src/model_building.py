import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

def split_data(creditcard_data, fraud_data):
    """Split the credit card and fraud data into training and testing sets."""
    # For Credit Card Data
    X_creditcard = creditcard_data.drop(columns=['Class'])  # Independent features
    y_creditcard = creditcard_data['Class']                   # Target variable

    # For Fraud Data
    X_fraud = fraud_data.drop(columns=['class'])  # Independent features
    y_fraud = fraud_data['class']      # Target variable

    # Train-test split for Credit Card Data
    X_train_creditcard, X_test_creditcard, y_train_creditcard, y_test_creditcard = train_test_split(
        X_creditcard, y_creditcard, test_size=0.2, random_state=42, stratify=y_creditcard
    )

    # Train-test split for Fraud Data
    X_train_fraud, X_test_fraud, y_train_fraud, y_test_fraud = train_test_split(
        X_fraud, y_fraud, test_size=0.2, random_state=42, stratify=y_fraud
    )

    return (X_train_creditcard, X_test_creditcard, y_train_creditcard, y_test_creditcard,
            X_train_fraud, X_test_fraud, y_train_fraud, y_test_fraud)

def apply_smote(X_train_creditcard, y_train_creditcard, X_train_fraud, y_train_fraud):
    """Apply SMOTE to the training data for both credit card and fraud datasets."""
    # Apply SMOTE for Credit Card Data
    smote_creditcard = SMOTE(random_state=42)
    X_train_creditcard_resampled, y_train_creditcard_resampled = smote_creditcard.fit_resample(X_train_creditcard, y_train_creditcard)

    # Apply SMOTE for Fraud Data
    smote_fraud = SMOTE(random_state=42)
    X_train_fraud_resampled, y_train_fraud_resampled = smote_fraud.fit_resample(X_train_fraud, y_train_fraud)

    return (X_train_creditcard_resampled, y_train_creditcard_resampled,
            X_train_fraud_resampled, y_train_fraud_resampled)
