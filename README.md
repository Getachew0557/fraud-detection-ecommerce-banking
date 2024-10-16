# Fraud Detection System for E-Commerce and Banking Transactions Using Machine Learning

## Overview
This project focuses on detecting fraudulent transactions in e-commerce and banking datasets using machine learning models. It includes data preprocessing, feature engineering, model building, and deployment. Additionally, geolocation analysis is integrated into the fraud detection pipeline to enhance detection accuracy.

## Business Need
Financial fraud can lead to significant losses for businesses and customers. This system helps Adey Innovations Inc. identify and prevent fraudulent activities using advanced machine learning models. Real-time monitoring and geolocation-based fraud detection provide added layers of security.

## Datasets
1. **Fraud_Data.csv**: Contains e-commerce transactions data with details such as user information, device, purchase details, and fraud labels.
2. **IpAddress_to_Country.csv**: Maps IP addresses to countries to identify the geolocation of the user.
3. **creditcard.csv**: Contains anonymized bank credit card transaction data curated for fraud detection.

## Features
- Transaction Frequency and Velocity Features
- Time-Based Features: Hour of day, Day of the week
- Geolocation-based fraud detection using IP-to-country mapping

## Machine Learning Models
The project implements and compares several machine learning models:
- Logistic Regression
- Random Forest
- Decision Tree
- Gradient Boosting
- Neural Networks (MLP, CNN, RNN, LSTM)

## Model Explainability
We use SHAP and LIME to explain model predictions and feature importance. This enhances transparency and trust in the model.

## Flask API and Docker Deployment
The fraud detection model is deployed using Flask, containerized with Docker, and exposed via a REST API for real-time prediction. Logging is integrated for continuous monitoring.

## Dash Dashboard
An interactive dashboard built with Dash to visualize fraud detection insights such as:
- Transaction counts and fraud cases
- Fraud trends over time
- Geolocation analysis of fraud cases
- Device and browser comparisons for fraudulent activities

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fraud-detection-ecommerce-banking.git
