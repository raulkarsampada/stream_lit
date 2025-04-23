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

# Corrected the st.image() line
st.image("https://cdn-icons-png.flaticon.com/512/3004/3004593.png", width=80)
st.title("🫁 Pulmonary Function Test")  # Corrected the string here
st.markdown("Use the tabs below to enter and view data for different lung function tests.")

# Create two columns to arrange the tabs in a row format
col1, col2 = st.columns(2)

# Tabs Navigation in Column Layout
with col1:
    tabs_1 = st.radio("🧍 Patient Info", ["Patient Info"])

with col2:
    tabs_2 = st.radio("🌬️ Test Tabs", ["Expiratory Test", "Inspiratory Test", "FVC Test", "Report"])

# 1. Patient Info Tab
if tabs_1 == "Patient Info":
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
if tabs_2 == "Expiratory Test":
    st.image("https://cdn-icons-png.flaticon.com/512/553/553416.png", width=60)
    fev1 = st.number_input("📉 FEV1 (L)", min_value=0.0, step=0.1)
    fvc_exp = st.number_input("📊 FVC (L)", min_value=0.0, step=0.1)
    pef = st.number_input("📈 PEF (L/min)", min_value=0.0, step=0.1)
    mep = st.number_input("💪 MEP (cmH₂O)", min_value=0.0, step=0.1)

    if st.button("Submit Expiratory Test"):
        st.success("✅ Expiratory Test Saved")

# 3. Inspiratory Test Tab
if tabs_2 == "Inspiratory Test":
    st.image("https://cdn-icons-png.flaticon.com/512/3004/3004593.png", width=60)
    fivc = st.number_input("🌬️ FIVC (L)", min_value=0.0, step=0.1)
    mip = st.number_input("💪 MIP (cmH₂O)", min_value=0.0, step=0.1)
    pif = st.number_input("💨 PIF (L/min)", min_value=0.0, step=0.1)

    if st.button("Submit Inspiratory Test"):
        st.success("✅ Inspiratory Test Saved")

# 4. FVC Test Tab
if tabs_2 == "FVC Test":
    st.image("https://cdn-icons-png.flaticon.com/512/1321/1321360.png", width=60)
    svc = st.number_input("📊 SVC (L)", min_value=0.0, step=0.1)
    mvv = st.number_input("🫁 MVV (L/min)", min_value=0.0, step=0.1)

    if st.button("Submit FVC Test"):
        st.success("✅ FVC Test Saved")

# 5. Report Tab
if tabs_2 == "Report":
    st.image("https://cdn-icons-png.flaticon.com/512/3039/3039437.png", width=60)
    st.subheader("🧾 Summary Report")

    # Safely get the data for the report (fallback to 'N/A' if values are missing)
    patient_name = name if name else "N/A"
    patient_age = age if age else "N/A"
    patient_gender = gender if gender else "N/A"
    patient_id_value = patient_id if patient_id else "N/A"

    # Expiratory Test data
    fev1_value = fev1 if fev1 else "N/A"
    fvc_exp_value = fvc_exp if fvc_exp else "N/A"
    pef_value = pef if pef else "N/A"
    mep_value = mep if mep else "N/A"

    # Inspiratory Test data
    fivc_value = fivc if fivc else "N/A"
    mip_value = mip if mip else "N/A"
    pif_value = pif if pif else "N/A"

    # FVC Test data
    svc_value = svc if svc else "N/A"
    mvv_value = mvv if mvv else "N/A"

    # Display Summary Report
    st.markdown(f"#### 👤 Patient Info")
    st.markdown(f"- Name: **{patient_name}**")
    st.markdown(f"- Age: **{patient_age}**")
    st.markdown(f"- Gender: **{patient_gender}**")
    st.markdown(f"- ID: **{patient_id_value}**")

    st.markdown(f"#### 🌬️ Expiratory Test")
    st.markdown(f"- FEV1: **{fev1_value}** L")
    st.markdown(f"- FVC: **{fvc_exp_value}** L")
    st.markdown(f"- PEF: **{pef_value}** L/min")
    st.markdown(f"- MEP: **{mep_value}** cmH₂O")

    st.markdown(f"#### 🌬️ Inspiratory Test")
    st.markdown(f"- FIVC: **{fivc_value}** L")
    st.markdown(f"- MIP: **{mip_value}** cmH₂O")
    st.markdown(f"- PIF: **{pif_value}** L/min")

    st.markdown(f"#### 📊 FVC Test")
    st.markdown(f"- SVC: **{svc_value}** L")
    st.markdown(f"- MVV: **{mvv_value}** L/min")
