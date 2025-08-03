import streamlit as st
import numpy as np
import pickle
import base64

def set_background_gif_from_url(gif_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{gif_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Paste your copied GIF URL here
gif_url = "https://cdn.dribbble.com/users/568/screenshots/2937224/browserpreview_tmp.gif"
set_background_gif_from_url(gif_url)

# Load model
model = joblib.load('sonar_model.joblib')


# App title and layout
st.set_page_config(page_title="Sonar Signal Classifier", layout="centered")
st.title("🔊 Sonar Signal Classification")
st.markdown("Classify whether the sonar return signal indicates a **Rock** 🪨 or a **Mine** 💣")

st.markdown("---")
st.markdown("### 🧠 Choose Your Input Method")

mode = st.radio("Select Input Mode:", ["🔸 Paste All Features (1 Line)", "🔹 Enter Manually (60 Fields)"], horizontal=True)
st.markdown("---")

features = []

# Option 1: Paste all features in one line
if mode == "🔸 Paste All Features (1 Line)":
    st.markdown("#### 📥 Paste 60 comma-separated values below")
    with st.form("paste_input"):
        raw_input = st.text_area("✏️ Example: 0.02, 0.037, 0.043, ...", height=130, placeholder="Paste your 60 values here...")
        submitted = st.form_submit_button("🚀 Classify")

    if submitted:
        try:
            features = list(map(float, raw_input.strip().split(',')))
            if len(features) != 60:
                st.error("❌ Please enter exactly 60 values.")
            else:
                input_array = np.array(features).reshape(1, -1)
                prediction = model.predict(input_array)[0]
                result = "🪨 Rock" if prediction == 'R' else "💣 Mine"
                st.success(f"✅ **Prediction:** {result}")
        except ValueError:
            st.error("⚠️ Invalid input — please ensure all values are numbers and comma-separated.")

# Option 2: Enter each feature manually
elif mode == "🔹 Enter Manually (60 Fields)":
    st.markdown("#### 🧾 Enter values for all 60 features manually")

    with st.form("manual_input"):
        cols = st.columns(4)
        for i in range(60):
            with cols[i % 4]:
                val = st.number_input(f"F{i+1}", key=f"f_{i}", format="%.4f", step=0.01)
                features.append(val)
        submitted = st.form_submit_button("🚀 Classify")

    if submitted:
        input_array = np.array(features).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        result = "🪨 Rock" if prediction == 'R' else "💣 Mine"
        st.success(f"✅ **Prediction:** {result}")


