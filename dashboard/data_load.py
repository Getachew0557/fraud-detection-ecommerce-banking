# dashboard/data_load.py

import pandas as pd

def load_data():
    # Load datasets
    fraud_data = pd.read_csv('../data/Fraud_Data.csv')
    ip_to_country = pd.read_csv('../data/IpAddress_to_Country.csv')
    credit_card_data = pd.read_csv('../data/creditcard.csv')
    
    # Preprocess fraud data and join with IP country data
    fraud_data['ip_address'] = fraud_data['ip_address'].astype(float)
    ip_to_country['lower_bound_ip_address'] = ip_to_country['lower_bound_ip_address'].astype(float)
    ip_to_country['upper_bound_ip_address'] = ip_to_country['upper_bound_ip_address'].astype(float)

    # Merging IP address to country
    fraud_data = pd.merge(
        fraud_data,
        ip_to_country,
        left_on='ip_address',
        right_on='lower_bound_ip_address',
        how='left'
    )

    # Adding summary statistics
    summary = {
        'total_transactions': len(fraud_data),
        'total_fraud_cases': fraud_data['class'].sum(),
        'fraud_percentage': (fraud_data['class'].mean() * 100).round(2),
    }

    return fraud_data, credit_card_data, summary
