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

def bivariateAnalysis(fraud_data, creditcard_data, ip_address_data):
    # Bar plots for categorical features vs. class
    plt.figure(figsize=(10, 5))
    sns.countplot(data=fraud_data, x='sex', hue='class')
    plt.title('Count of Users by Sex and Class')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    plt.legend(title='Class')
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.countplot(data=fraud_data, x='source', hue='class')
    plt.title('Count of Users by Source and Class')
    plt.xlabel('Source')
    plt.ylabel('Count')
    plt.legend(title='Class')
    plt.show()

    # Creditcard_Data Correlation matrix
    plt.figure(figsize=(18, 14))
    correlation = creditcard_data.corr()
    sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Matrix for Creditcard_Data')
    plt.show()

    # Box plot for Time vs. target variable (assuming 'Class' is the target)
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=creditcard_data, x='Class', y='Time')
    plt.title('Box Plot of Time by Class')
    plt.xlabel('Class')
    plt.ylabel('Time')
    plt.show()

    # Count plot for lower_bound_ip_address and country
    plt.figure(figsize=(14, 14))
    sns.boxplot(data=ip_address_data, x='country', y='lower_bound_ip_address')
    plt.title('Box Plot of Lower Bound IP Address by Country')
    plt.xlabel('Country')
    plt.ylabel('Lower Bound IP Address')
    plt.xticks(rotation=45)
    plt.show()

    # Top 10 Countries by IP Address Count
    plt.figure(figsize=(12, 8))
    country_counts = ip_address_data['country'].value_counts()
    country_counts[:10].plot(kind='barh')  # Show top 10 countries
    plt.title('Top 10 Countries by IP Address Count')
    plt.xlabel('Count')
    plt.ylabel('Country')
    plt.show()

    # Bivariate analysis of purchase value vs fraud class
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='class', y='purchase_value', data=fraud_data)
    plt.title('Purchase Value vs Fraud Class')
    plt.show()

    # Bivariate analysis of age vs fraud class
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='class', y='age', data=fraud_data)
    plt.title('Age vs Fraud Class')
    plt.show()


    # Bivariate analysis for categorical variables (e.g., 'browser' vs 'class')
    plt.figure(figsize=(12, 6))
    sns.countplot(x='browser', hue='class', data=fraud_data)
    plt.title('Browser Usage by Fraud Class')
    plt.show()

    # Bivariate analysis for 'age' vs 'purchase_value'
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='age', y='purchase_value', hue='class', data=fraud_data)
    plt.title('Age vs Purchase Value (Colored by Fraud Class)')
    plt.show()

