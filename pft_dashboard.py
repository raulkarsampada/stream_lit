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

# 2. Expiratory Test Section
with st.expander("🌬️ Expiratory Test"):
    fev1 = st.number_input("📉 FEV1 (Forced Expiratory Volume in 1s) - L", min_value=0.0, step=0.1)
    fvc_exp = st.number_input("📊 FVC (Forced Vital Capacity) - L", min_value=0.0, step=0.1)
    pef = st.number_input("📈 PEF (Peak Expiratory Flow) - L/min", min_value=0.0, step=0.1)
    mep = st.number_input("💪 MEP (Max Expiratory Pressure) - cmH₂O", min_value=0.0, step=0.1)

    if st.button("📤 Submit Expiratory Test"):
        st.success("✅ Expiratory Test Submitted")

# 3. Inspiratory Test Section
with st.expander("🌬️ Inspiratory Test"):
    fivc = st.number_input("🌬️ FIVC (Forced Inspiratory Vital Capacity) - L", min_value=0.0, step=0.1)
    mip = st.number_input("💪 MIP (Max Inspiratory Pressure) - cmH₂O", min_value=0.0, step=0.1)
    pif = st.number_input("💨 PIF (Peak Inspiratory Flow) - L/min", min_value=0.0, step=0.1)

    if st.button("📤 Submit Inspiratory Test"):
        st.success("✅ Inspiratory Test Submitted")

# 4. FVC Test Section
with st.expander("📊 FVC Test"):
    svc = st.number_input("📊 SVC (Slow Vital Capacity) - L", min_value=0.0, step=0.1)
    mvv = st.number_input("🫁 MVV (Max Voluntary Ventilation) - L/min", min_value=0.0, step=0.1)

    if st.button("📤 Submit FVC Test"):
        st.success("✅ FVC Test Submitted")

# 5. Final Report Section
with st.expander("📄 Report Summary", expanded=False):
    st.markdown("### 🧾 Summary Report")

    st.markdown("#### 🔹 Patient Info")
    st.markdown(f"**Name:** {name if name else 'N/A'}")
    st.markdown(f"**Age:** {age if age else 'N/A'}")
    st.markdown(f"**Gender:** {gender if gender else 'N/A'}")
    st.markdown(f"**Patient ID:** {patient_id if patient_id else 'N/A'}")

    st.markdown("#### 🔹 Expiratory Test")
    st.markdown(f"- FEV1: {fev1} L")
    st.markdown(f"- FVC: {fvc_exp} L")
    st.markdown(f"- PEF: {pef} L/min")
    st.markdown(f"- MEP: {mep} cmH₂O")

    st.markdown("#### 🔹 Inspiratory Test")
    st.markdown(f"- FIVC: {fivc} L")
    st.markdown(f"- MIP: {mip} cmH₂O")
    st.markdown(f"- PIF: {pif} L/min")

    st.markdown("#### 🔹 FVC Test")
    st.markdown(f"- SVC: {svc} L")
    st.markdown(f"- MVV: {mvv} L/min")
