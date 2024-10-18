import pandas as pd

def load_sample_data():
    """Load sample datasets as DataFrames."""
    # Sample Fraud Data
    fraud_data = pd.DataFrame({
        'user_id': [22058, 333320, 1359],
        'signup_time': pd.to_datetime(['2015-02-24 22:55:49', '2015-06-07 20:39:50', '2015-01-01 18:52:44']),
        'purchase_time': pd.to_datetime(['2015-04-18 02:47:11', '2015-06-08 01:38:54', '2015-01-01 18:52:45']),
        'purchase_value': [34, 16, 15],
        'device_id': ['QVPSPJUOCKZAR', 'EOGFQPIZPYXFZ', 'YSSKYOSJHPPLJ'],
        'source': ['SEO', 'Ads', 'SEO'],
        'browser': ['Chrome', 'Chrome', 'Opera'],
        'sex': ['M', 'F', 'M'],
        'age': [39, 53, 53],
        'ip_address': [732758400, 350311400, 2621474000],
        'class': [0, 0, 1]
    })

    # Sample IP Address Data
    ip_address_data = pd.DataFrame({
        'lower_bound_ip_address': [16777216.0, 16777472.0, 16777728.0],
        'upper_bound_ip_address': [16777471, 16777727, 16778239],
        'country': ['Australia', 'China', 'China']
    })

    # Sample Credit Score Data
    creditcard_data = pd.DataFrame({
        'Time': [0.0, 0.0, 1.0],
        'V1': [-1.359807, 1.191857, -1.358354],
        'V2': [-0.072781, 0.266151, -1.340163],
        'V3': [2.536347, 0.166480, 1.773209],
        'V4': [1.378155, 0.448154, 0.379780],
        'V5': [-0.338321, 0.060018, -0.503198],
        'Amount': [149.62, 2.69, 378.66],
        'Class': [0, 0, 0]
    })

    return fraud_data, creditcard_data, ip_address_data
