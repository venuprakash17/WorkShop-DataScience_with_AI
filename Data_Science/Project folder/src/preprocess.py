# src/preprocess.py
"""
Data Preprocessing for E-Commerce Dataset
- Removes IDs and date
- Encodes categorical variables
- Scales numerical features
- Returns feature names for deployment
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_and_preprocess(filepath):
    # Load dataset
    df = pd.read_csv(filepath)

    # Drop irrelevant columns
    df = df.drop(columns=["user_id", "session_id", "date"])

    # Encode categorical features
    cat_cols = df.select_dtypes(include=["object"]).columns
    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    # Split features/target
    X = df.drop(columns=["purchase"])
    y = df["purchase"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, X.columns.tolist()
