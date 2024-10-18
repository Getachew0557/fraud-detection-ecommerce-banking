import pandas as pd
import os
import sys
# Append the correct src path for custom module imports
sys.path.append(os.path.abspath('../src'))
sys.path.append(os.path.abspath('../tests'))


from data_cleaning import check_duplicates, drop_duplicates, convert_to_datetime
import pandas as pd
from data_preprocessing import preprocess_data
from test_data_loading import load_sample_data

def test_preprocess_data():
    fraud_data, creditcard_data, ip_address_data = load_sample_data()

    # Running preprocessing
    processed_fraud_data, processed_creditcard_data, processed_ip_address_data = preprocess_data(
        fraud_data, creditcard_data, ip_address_data
    )

    # Assertions to verify the data has been preprocessed correctly
    assert processed_fraud_data['signup_time'].dtype == 'datetime64[ns]'
    assert processed_fraud_data['purchase_time'].dtype == 'datetime64[ns]'
    assert processed_creditcard_data.shape[0] == 3  # Same number of rows
    assert processed_ip_address_data.shape[0] == 3  # Same number of rows
    assert check_duplicates(processed_creditcard_data) == 0  # No duplicates after cleaning
