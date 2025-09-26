# app/streamlit_app.py
"""
Streamlit App for E-Commerce Purchase Prediction
Run: streamlit run app/streamlit_app.py
"""

import streamlit as st
import joblib
import pandas as pd

# ---------------------
# Load model, scaler & feature names
# ---------------------
model = joblib.load("models/ecommerce_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_names = joblib.load("models/feature_names.pkl")

st.set_page_config(page_title="E-Commerce Purchase Prediction", layout="centered")
st.title("🛒 E-Commerce Purchase Prediction")
st.write("Predict whether a customer will purchase based on session details.")

# ---------------------
# Sidebar inputs for ALL features
# ---------------------
st.sidebar.header("Customer Session Details")

age = st.sidebar.slider("Age", 18, 70, 30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
location = st.sidebar.selectbox("Location", ["USA", "UK", "Germany", "Canada", "Australia"])
membership_status = st.sidebar.selectbox("Membership Status", ["Guest", "Registered"])
returning_customer = st.sidebar.selectbox("Returning Customer", [0, 1])
device_type = st.sidebar.selectbox("Device Type", ["Mobile", "Desktop", "Tablet"])
browser = st.sidebar.selectbox("Browser", ["Chrome", "Firefox", "Safari", "Edge"])
time_of_day = st.sidebar.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])

time_spent = st.sidebar.slider("Time Spent (minutes)", 1, 120, 30)
pages_viewed = st.sidebar.slider("Pages Viewed", 1, 50, 10)
scroll_depth = st.sidebar.slider("Scroll Depth (%)", 0, 100, 50)
clicks = st.sidebar.slider("Clicks", 0, 100, 10)

traffic_source = st.sidebar.selectbox("Traffic Source", ["Organic", "Social", "Referral", "Paid"])
ad_campaign = st.sidebar.selectbox("Ad Campaign", ["Campaign_A", "Campaign_B", "Campaign_C"])
coupon_used = st.sidebar.selectbox("Coupon Used", [0, 1])
discount_applied = st.sidebar.selectbox("Discount Applied", [0, 1])
product_category = st.sidebar.selectbox("Product Category", ["Clothing", "Electronics", "Home", "Books", "Sports"])
wishlist_items = st.sidebar.slider("Wishlist Items", 0, 20, 2)
cart_items = st.sidebar.slider("Cart Items", 0, 10, 1)
avg_session_value = st.sidebar.slider("Average Session Value", 0, 1000, 100)
payment_method = st.sidebar.selectbox("Payment Method", ["UPI", "Debit Card", "Credit Card", "NetBanking", "COD"])

# ---------------------
# Build input dict
# ---------------------
features = {
    "age": age,
    "gender": gender,
    "location": location,
    "membership_status": membership_status,
    "returning_customer": returning_customer,
    "device_type": device_type,
    "browser": browser,
    "time_of_day": time_of_day,
    "time_spent_minutes": time_spent,
    "pages_viewed": pages_viewed,
    "scroll_depth": scroll_depth,
    "clicks": clicks,
    "traffic_source": traffic_source,
    "ad_campaign": ad_campaign,
    "coupon_used": coupon_used,
    "discount_applied": discount_applied,
    "product_category": product_category,
    "wishlist_items": wishlist_items,
    "cart_items": cart_items,
    "avg_session_value": avg_session_value,
    "payment_method": payment_method,
}

input_df = pd.DataFrame([features])

# ---------------------
# Encode categoricals
# ---------------------
cat_cols = input_df.select_dtypes(include=["object"]).columns
for col in cat_cols:
    input_df[col] = input_df[col].astype("category").cat.codes

# ✅ Reindex to match training feature order
input_df = input_df.reindex(columns=feature_names)

# ---------------------
# Predict
# ---------------------
if st.button("Predict"):
    scaled_input = scaler.transform(input_df)
    pred = model.predict(scaled_input)[0]
    prob = model.predict_proba(scaled_input)[0][1] * 100

    if pred == 1:
        st.success(f"✅ Customer is likely to purchase! (Confidence: {prob:.2f}%)")
    else:
        st.warning(f"❌ Customer is unlikely to purchase. (Confidence: {prob:.2f}%)")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Model: RandomForestClassifier")
