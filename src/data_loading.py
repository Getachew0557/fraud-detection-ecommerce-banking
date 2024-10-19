import pandas as pd

def load_data(fraud_data_path, creditcard_data_path, ip_address_data_path):
    """Load datasets from specified paths."""
    fraud_data = pd.read_csv(fraud_data_path)
    creditcard_data = pd.read_csv(creditcard_data_path)
    ip_address_data = pd.read_csv(ip_address_data_path)
    
    return fraud_data, creditcard_data, ip_address_data
