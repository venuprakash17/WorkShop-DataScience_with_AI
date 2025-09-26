# src/evaluate.py
"""
Evaluate trained ML model
"""

import joblib
from preprocess import load_and_preprocess
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def evaluate_model():
    (
        X_train, X_test, y_train, y_test,
        scaler, feature_names
    ) = load_and_preprocess("data/Realistic_E-Commerce_Dataset.csv")

    # Load model
    model = joblib.load("models/ecommerce_model.pkl")

    # Predictions
    y_pred = model.predict(X_test)

    # Metrics
    print("📊 Model Performance:\n")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(classification_report(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    evaluate_model()
