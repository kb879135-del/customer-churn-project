import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# ------------------ TITLE ------------------
st.title("🚀 Customer Analytics & Churn Prediction")
st.markdown("### Enter customer details to predict behavior")


# ------------------ INPUT ------------------
recency = st.number_input("Recency (days)", min_value=0)
frequency = st.number_input("Frequency", min_value=0)
monetary = st.number_input("Monetary", min_value=0.0)
engagement = st.number_input("Engagement Score", min_value=0.0)
gap = st.number_input("Avg Purchase Gap", min_value=0.0)
trend = st.number_input("Activity Trend", value=0.0)

# ------------------ DUMMY MODEL (Replace later with your trained model) ------------------
# NOTE: Replace this with your trained model (pickle file later)
import pickle
model=pickle.load(open('model.pkl','rb'))


# ------------------ SEGMENT LOGIC ------------------
def get_segment(recency, frequency, monetary):
    if recency < 30 and frequency > 5:
        return "VIP 🔥"
    elif frequency > 3:
        return "Loyal 🙂"
    elif recency > 90:
        return "At Risk ⚠️"
    else:
        return "Regular"

# ------------------ PREDICTION ------------------
if st.button("Predict"):

    input_data = np.array([[recency, frequency, monetary, engagement, gap, trend]])

    prediction = model.predict(input_data)

    segment = get_segment(recency, frequency, monetary)

    st.subheader("📊 Results")

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer is active")

    st.info(f"Customer Segment: {segment}")
