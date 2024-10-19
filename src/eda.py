import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

def univariateAnalysis(fraud_data, creditcard_data, ip_address_data):
    # Univariate Analysis for Fraud Data
    # Histogram for purchase_value
    plt.figure(figsize=(10, 5))
    sns.histplot(fraud_data['purchase_value'], bins=30, kde=True)
    plt.title('Distribution of Purchase Value')
    plt.xlabel('Purchase Value')
    plt.ylabel('Frequency')
    plt.show()

    # Histogram for age
    plt.figure(figsize=(10, 5))
    sns.histplot(fraud_data['age'], bins=30, kde=True)
    plt.title('Distribution of Age')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

    # Count plot for categorical features
    plt.figure(figsize=(10, 5))
    sns.countplot(data=fraud_data, x='sex')
    plt.title('Count of Users by Sex')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.countplot(data=fraud_data, x='source')
    plt.title('Count of Users by Source')
    plt.xlabel('Source')
    plt.ylabel('Count')
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.countplot(data=fraud_data, x='browser')
    plt.title('Count of Users by Browser')
    plt.xlabel('Browser')
    plt.ylabel('Count')
    plt.show()

    # Univariate Analysis for Credit Card Data
    # Histogram for Time
    plt.figure(figsize=(10, 5))
    sns.histplot(creditcard_data['Time'], bins=30, kde=True)
    plt.title('Distribution of Time')
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.show()

    # Histograms for V1 to V5 as an example
    for col in creditcard_data.columns[1:6]:  # Adjust column indices as necessary
        plt.figure(figsize=(10, 5))
        sns.histplot(creditcard_data[col], bins=30, kde=True)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.show()

    # Univariate Analysis for IP Address Data
    # Histogram for lower_bound_ip_address
    plt.figure(figsize=(10, 5))
    sns.histplot(ip_address_data['lower_bound_ip_address'], bins=30, kde=True)
    plt.title('Distribution of Lower Bound IP Address')
    plt.xlabel('Lower Bound IP Address')
    plt.ylabel('Frequency')
    plt.show()

    # Histogram for upper_bound_ip_address
    plt.figure(figsize=(10, 5))
    sns.histplot(ip_address_data['upper_bound_ip_address'], bins=30, kde=True)
    plt.title('Distribution of Upper Bound IP Address')
    plt.xlabel('Upper Bound IP Address')
    plt.ylabel('Frequency')
    plt.show()

    # Count plot for country
    plt.figure(figsize=(10, 5))
    sns.countplot(data=ip_address_data, x='country', order=ip_address_data['country'].value_counts().index)
    plt.title('Count of IP Addresses by Country')
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

