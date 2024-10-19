import pandas as pd
def check_duplicates(data):
    """Check for duplicates in the DataFrame."""
    return data.duplicated().sum()

def drop_duplicates(data):
    """Remove duplicates from the DataFrame."""
    return data.drop_duplicates()

def convert_to_datetime(data, columns):
    """Convert specified columns to datetime format."""
    for column in columns:
        data[column] = pd.to_datetime(data[column])
    return data

def convert_to_int(data, columns):
    """Convert specified columns to integer type."""
    for column in columns:
        data[column] = data[column].astype('int64')
    return data
