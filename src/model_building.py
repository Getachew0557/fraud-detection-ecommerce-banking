import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier

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
# Define a Function for Model Training and Evaluation
def evaluate_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model: {model.__class__.__name__}")
    print(f"Accuracy: {accuracy:.4f}")
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))
    
    # Plot ROC Curve
    y_prob = model.predict_proba(X_test)[:, 1]  # Get probabilities for the positive class
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    
    plt.plot(fpr, tpr, label=f'{model.__class__.__name__} (AUC = {roc_auc:.2f})')
    
    return roc_auc

def plot_confusion_matrix(cm, model_name):
    """Plot the confusion matrix."""
    plt.figure(figsize=(6, 5))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title(f'Confusion Matrix for {model_name}')
    plt.colorbar()
    tick_marks = np.arange(2)
    plt.xticks(tick_marks, ['No Fraud', 'Fraud'])
    plt.yticks(tick_marks, ['No Fraud', 'Fraud'])
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
    plt.show()

## machine learning model building and evaluation
def evaluate_models(X_train_creditcard_resampled, y_train_creditcard_resampled, 
                    X_test_creditcard, y_test_creditcard, 
                    X_train_fraud_resampled, y_train_fraud_resampled, 
                    X_test_fraud, y_test_fraud):
    """Evaluate and compare models on Credit Card and Fraud data."""
    
    models = [
        LogisticRegression(max_iter=1000),
        DecisionTreeClassifier(),
        RandomForestClassifier(),
        GradientBoostingClassifier(),
        MLPClassifier(max_iter=1000)
    ]

    auc_scores = []

    # Evaluate models for Credit Card Data
    plt.figure(figsize=(10, 6))
    for model in models:
        print(f"\nEvaluating {model.__class__.__name__} on Credit Card Data:")
        auc_score = evaluate_model(model, X_train_creditcard_resampled, y_train_creditcard_resampled, 
                                   X_test_creditcard, y_test_creditcard)
        auc_scores.append(auc_score)

    # Evaluate models for Fraud Data
    for model in models:
        print(f"\nEvaluating {model.__class__.__name__} on Fraud Data:")
        evaluate_model(model, X_train_fraud_resampled, y_train_fraud_resampled, 
                       X_test_fraud, y_test_fraud)

    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()

    return auc_scores