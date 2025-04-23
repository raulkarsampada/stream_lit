import streamlit as st

st.set_page_config(page_title="Pulmonary Function Test Dashboard", layout="centered")

st.title("🧬 Pulmonary Function Test Dashboard")

# Create Tabs
tabs = st.tabs(["Patient Details", "Respiratory Test", "Expiratory Test", "Inspiratory Test", "FVC Test"])

# Patient Details Tab
with tabs[0]:
    st.header("🧍 Patient Information")
    with st.form("patient_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        patient_id = st.text_input("Patient ID")
        submit = st.form_submit_button("Save Patient Info")
        
        if submit:
            st.success(f"Patient Info Saved: {name}, {age} yrs, {gender}, ID: {patient_id}")

# Respiratory Test Tab
with tabs[1]:
    st.header("🫁 Respiratory Test")
    st.write("Enter or upload respiratory test data below:")
    
    resp_result = st.text_area("Respiratory Test Observations")
    resp_file = st.file_uploader("Upload Respiratory Test Report (Optional)", type=["csv", "pdf", "txt"])
    
    if st.button("Submit Respiratory Test"):
        st.success("Respiratory Test data submitted.")

# Expiratory Test Tab
with tabs[2]:
    st.header("🌬️ Expiratory Test")
    st.write("Enter expiratory test values:")

    pef = st.number_input("Peak Expiratory Flow (PEF) - L/min", min_value=0.0, step=0.1)
    fev1 = st.number_input("Forced Expiratory Volume in 1 second (FEV1) - L", min_value=0.0, step=0.1)
    
    if st.button("Submit Expiratory Test"):
        st.success(f"Expiratory Test Submitted: PEF = {pef} L/min, FEV1 = {fev1} L")

# Inspiratory Test Tab
with tabs[3]:
    st.header("🌬️ Inspiratory Test")
    st.write("Enter inspiratory test values:")

    mvv = st.number_input("Maximum Voluntary Ventilation (MVV) - L/min", min_value=0.0, step=0.1)
    tidal_volume = st.number_input("Tidal Volume - L", min_value=0.0, step=0.1)

    if st.button("Submit Inspiratory Test"):
        st.success(f"Inspiratory Test Submitted: MVV = {mvv} L/min, Tidal Volume = {tidal_volume} L")

# FVC Test Tab
with tabs[4]:
    st.header("📊 Forced Vital Capacity (FVC) Test")
    st.write("Enter FVC test data:")

    fvc = st.number_input("Forced Vital Capacity (FVC) - L", min_value=0.0, step=0.1)
    fev1_fvc_ratio = st.number_input("FEV1/FVC Ratio (%)", min_value=0.0, max_value=100.0, step=0.1)

    if st.button("Submit FVC Test"):
        st.success(f"FVC Test Submitted: FVC = {fvc} L, FEV1/FVC Ratio = {fev1_fvc_ratio}%")
