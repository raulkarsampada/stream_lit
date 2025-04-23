import streamlit as st

st.set_page_config(page_title="Pulmonary Function Test Dashboard", layout="centered")

st.title("🧬 Pulmonary Function Test Dashboard")
st.markdown("---")

# 1. Patient Information Section
with st.expander("🧍 Patient Information", expanded=True):
    with st.form("patient_form"):
        name = st.text_input("👤 Full Name")
        age = st.number_input("🎂 Age", min_value=0, max_value=120, step=1)
        gender = st.selectbox("⚧️ Gender", ["Male", "Female", "Other"])
        patient_id = st.text_input("🆔 Patient ID")
        submit = st.form_submit_button("💾 Save Patient Info")

        if submit:
            st.success(f"✅ Patient Info Saved: {name}, {age} yrs, {gender}, ID: {patient_id}")

# 2. Respiratory Test Section
with st.expander("🫁 Respiratory Test"):
    resp_result = st.text_area("📝 Observations")
    resp_file = st.file_uploader("📎 Upload Respiratory Report (Optional)", type=["csv", "pdf", "txt"])
    
    if st.button("📤 Submit Respiratory Test"):
        st.success("✅ Respiratory Test Data Submitted")

# 3. Expiratory Test Section
with st.expander("🌬️ Expiratory Test"):
    pef = st.number_input("📈 Peak Expiratory Flow (PEF) - L/min", min_value=0.0, step=0.1)
    fev1 = st.number_input("📉 Forced Expiratory Volume in 1s (FEV1) - L", min_value=0.0, step=0.1)

    if st.button("📤 Submit Expiratory Test"):
        st.success(f"✅ Submitted: PEF = {pef} L/min, FEV1 = {fev1} L")

# 4. Inspiratory Test Section
with st.expander("🌬️ Inspiratory Test"):
    mvv = st.number_input("🫁 Maximum Voluntary Ventilation (MVV) - L/min", min_value=0.0, step=0.1)
    tidal_volume = st.number_input("💨 Tidal Volume - L", min_value=0.0, step=0.1)

    if st.button("📤 Submit Inspiratory Test"):
        st.success(f"✅ Submitted: MVV = {mvv} L/min, Tidal Volume = {tidal_volume} L")

# 5. FVC Test Section
with st.expander("📊 FVC Test"):
    fvc = st.number_input("📊 Forced Vital Capacity (FVC) - L", min_value=0.0, step=0.1)
    fev1_fvc_ratio = st.number_input("🔢 FEV1/FVC Ratio (%)_
