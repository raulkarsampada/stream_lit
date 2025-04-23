import streamlit as st

st.set_page_config(page_title="Pulmonary Function Test", layout="centered")

# Custom CSS to style the tabs to be larger and square-shaped
st.markdown(
    """
    <style>
    .stTabs [role="tablist"] {
        background-color: #f0f2f6;
        border-radius: 0px;
        padding: 0.5rem;
        gap: 10px;
    }
    .stTabs [role="tab"] {
        padding: 1rem 2rem;
        border: 2px solid #d0d0d0;
        border-radius: 8px;
        font-weight: 600;
        font-size: 16px;
        background-color: #ffffff;
        transition: background-color 0.3s ease;
    }
    .stTabs [role="tab"]:hover {
        background-color: #d0d0d0;
    }
    .stTabs [role="tab"][aria-selected="true"] {
        background-color: #4caf50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("https://cdn-icons-png.flaticon.com/512/3004/3004593.png", width=80)
st.title("🫁 Pulmonary Function Test")  # Corrected the string here
st.markdown("Use the tabs below to enter and view data for different lung function tests.")

# Tabs Navigation
tabs = st.tabs(["🧍 Patient Info", "🌬️ Expiratory Test", "🌬️ Inspiratory Test", "📊 FVC Test", "📄 Report"])

# 1. Patient Info Tab
with tabs[0]:
    with st.form("patient_form"):
        st.image("https://cdn-icons-png.flaticon.com/512/747/747376.png", width=60)
        name = st.text_input("👤 Full Name")
        age = st.number_input("🎂 Age", min_value=0, max_value=120, step=1)
        gender = st.selectbox("⚧️ Gender", ["Male", "Female", "Other"])
        patient_id = st.text_input("🆔 Patient ID")
        submit = st.form_submit_button("💾 Save Info")

        if submit:
            st.success(f"Saved: {name}, {age} yrs, {gender}, ID: {patient_id}")

# 2. Expiratory Test Tab
with tabs[1]:
    st.image("https://cdn-icons-png.flaticon.com/512/553/553416.png", width=60)
    fev1 = st.number_input("📉 FEV1 (L)", min_value=0.0, step=0.1)
    fvc_exp = st.number_input("📊 FVC (L)", min_value=0.0_
