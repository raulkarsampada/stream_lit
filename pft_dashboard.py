import streamlit as st

st.set_page_config(page_title="Pulmonary Function Test Dashboard", layout="centered")

st.markdown("<h1 style='text-align: center;'>🧬 Pulmonary Function Test Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# Create Styled Tabs
tabs = st.tabs([
    "🧍 Patient Details",
    "🫁 Respiratory Test",
    "🌬️ Expiratory Test",
    "🌬️ Inspiratory Test",
    "📊 FVC Test"
])

# Tab 1 - Patient Info
with tabs[0]:
    st.markdown("### 🧍 Patient Information")
    st.markdown("#### Enter Patient Details Below")
    st.markdown("---")
    
    with st.form("patient_form"):
        name = st.text_input("👤 Full Name")
        age = st.number_input("🎂 Age", min_value=0, max_value=120, step=1)
        gender = st.selectbox("⚧️ Gender", ["Male", "Female", "Other"])
        patient_id = st.text_input("🆔 Patient ID")
        submit = st.form_submit_button("💾 Save Patient Info")
        
        if submit:
            st.success(f"✅ Patient Info Saved: {name}, {age} yrs, {gender}, ID: {patient_id}")

# Tab 2 - Respiratory
with tabs[1]:
    st.markdown("### 🫁 Respiratory Test")
    st.markdown("#### Record General Observations or Upload a File")
    st.markdown("---")
    
    resp_result = st.text_area("📝 Respiratory Test Observations")
    resp_file = st.file_uploader("📎 Upload Respiratory Report (Optional)", type=["csv", "pdf", "txt"])
    
    if st.button("📤 Submit Respiratory Test"):
        st.success("✅ Respiratory Test Data Submitted")

# Tab 3 - Expiratory
with tabs[2]:
    st.markdown("### 🌬️ Expiratory Test")
    st.markdown("#### Enter Peak and Volume Data")
    st.markdown("---")

    pef = st.number_input("📈 Peak Expiratory Flow (PEF) - L/min", min_value=0.0, step=0.1)
    fev1 = st.number_input("📉 Forced Expiratory Volume in 1s (FEV1) - L", min_value=0.0, step=0.1)

    if st.button("📤 Submit Expiratory Test"):
        st.success(f"✅ Expiratory Test Submitted: PEF = {pef} L/min, FEV1 = {fev1} L")

# Tab 4 - Inspiratory
with tabs[3]:
    st.markdown("### 🌬️ Inspiratory Test")
    st.markdown("#### Record Inspiratory Strength Measures")
    st.markdown("---")

    mvv = st.number_input("🫁 Maximum Voluntary Ventilation (MVV) - L/min", min_value=0.0, step=0.1)
    tidal_volume = st.number_input("💨 Tidal Volume - L", min_value=0_
