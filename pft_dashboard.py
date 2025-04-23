import streamlit as st

st.set_page_config(page_title="Pulmonary Function Test Dashboard", layout="centered")

# Sidebar Navigation
st.sidebar.title("🧪 Test Navigation")
test_type = st.sidebar.radio(
    "Select Test Type",
    ("Patient Details", "Respiratory Test", "Expiratory Test", "Inspiratory Test", "FVC Test")
)

# Patient Info
if test_type == "Patient Details":
    st.title("🧍 Patient Information")
    
    with st.form("patient_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        patient_id = st.text_input("Patient ID")
        submit = st.form_submit_button("Save Patient Info")
        
        if submit:
            st.success(f"Patient Info Saved: {name}, {age} yrs, {gender}, ID: {patient_id}")

# Respiratory Test
elif test_type == "Respiratory Test":
    st.title("🫁 Respiratory Test")
    st.write("Enter or upload respiratory test data below:")
    
    test_result = st.text_area("Respiratory Test Observations")
    uploaded_file = st.file_uploader("Upload Respiratory Test Report (Optional)", type=["csv", "pdf", "txt"])
    
    if st.button("Submit Respiratory Test"):
        st.success("Respiratory Test data submitted.")

# Expiratory Test
elif test_type == "Expiratory Test":
    st.title("🌬️ Expiratory Test")
    st.write("Enter expiratory test values:")

    pef = st.number_input("Peak Expiratory Flow (PEF) - L/min", min_value=0.0, step=0.1)
    fev1 = st.number_input("Forced Expiratory Volume in 1 second (FEV1) - L", min_value=0.0, step=0.1)
    
    if st.button("Submit Expiratory Test"):
        st.success(f"Data saved: PEF = {pef} L/min, FEV1 = {fev1} L")

# Inspiratory Test
elif test_type == "Inspiratory Test":
    st.title("🌬️ Inspiratory Test")
    st.write("Enter inspiratory test values:")

    mvv = st.number_input("Maximum Voluntary Ventilation (MVV) - L/min", min_value=0.0, step=0.1)
    tidal_volume = st.number_input("Tidal Volume - L", min_value=0.0, step=0.1)

    if st.button("Submit Inspiratory Test"):
        st.success(f"Inspiratory test data submitted: MVV = {mvv} L/min, Tidal Volume = {tidal_volume} L")

# FVC Test
elif test_type == "FVC Test":
    st.title("📊 Forced Vital Capacity (FVC) Test")
    st.write("Enter FVC test data:")

    fvc = st.number_input("Forced Vital Capacity (FVC) - L", min_value=0.0, step=0.1)
    fev1_fvc_ratio = st.number_input("FEV1/FVC Ratio (%)", min_value=0.0, max_value=100.0, step=0.1)

    if st.button("Submit FVC Test"):
        st.success(f"FVC Test Submitted: FVC = {fvc} L, FEV1/FVC Ratio = {fev1_fvc_ratio}%")
