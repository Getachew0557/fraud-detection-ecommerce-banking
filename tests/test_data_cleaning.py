import pandas as pd
import os
import sys
import unittest
import pytest
# Append the correct src path for custom module imports
sys.path.append(os.path.abspath('../src'))
sys.path.append(os.path.abspath('../tests'))

from data_cleaning import check_duplicates, drop_duplicates, convert_to_datetime, convert_to_int
from test_data_loading import load_sample_data

def test_check_duplicates():
    fraud_data, _, _ = load_sample_data()
    assert check_duplicates(fraud_data) == 0  # No duplicates in the sample data

def test_drop_duplicates():
    data = pd.DataFrame({'A': [1, 1, 2], 'B': [2, 2, 3]})
    cleaned_data = drop_duplicates(data)
    assert cleaned_data.shape[0] == 2  # Should have 2 rows after dropping duplicates

def test_convert_to_datetime():
    fraud_data, _, _ = load_sample_data()
    fraud_data = convert_to_datetime(fraud_data, ['signup_time', 'purchase_time'])
    assert fraud_data['signup_time'].dtype == 'datetime64[ns]'
    assert fraud_data['purchase_time'].dtype == 'datetime64[ns]'

def test_convert_to_int():
    fraud_data, _, _ = load_sample_data()
    fraud_data = convert_to_int(fraud_data, ['ip_address'])
    assert fraud_data['ip_address'].dtype == 'int64'
