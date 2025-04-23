import streamlit as st

st.set_page_config(page_title="Pulmonary Function Test", layout="centered")

st.markdown(
    """
    <style>
    .stTabs [role="tablist"] {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 0.5rem;
        gap: 10px;
    }
    .stTabs [role="tab"] {
        padding: 0.6rem 1rem;
        border: 1px solid #d0d0d0;
        border-radius: 6px;
        margin-right: 5px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("https://cdn-icons-png.flaticon.com/512/3004/3004593.png", width=80)
st.title("🫁 Pulmonary Function Test")
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
    fvc_exp = st.number_input("📊 FVC (L)", min_value=0.0, step=0.1)
    pef = st.number_input("📈 PEF (L/min)", min_value=0.0, step=0.1)
    mep = st.number_input("💪 MEP (cmH₂O)", min_value=0.0, step=0.1)

    if st.button("Submit Expiratory Test"):
        st.success("✅ Expiratory Test Saved")

# 3. Inspiratory Test Tab
with tabs[2]:
    st.image("https://cdn-icons-png.flaticon.com/512/3004/3004593.png", width=60)
    fivc = st.number_input("🌬️ FIVC (L)", min_value=0.0, step=0.1)
    mip = st.number_input("💪 MIP (cmH₂O)", min_value=0.0, step=0.1)
    pif = st.number_input("💨 PIF (L/min)", min_value=0.0, step=0.1)

    if st.button("Submit Inspiratory Test"):
        st.success("✅ Inspiratory Test Saved")

# 4. FVC Test Tab
with tabs[3]:
    st.image("https://cdn-icons-png.flaticon.com/512/1321/1321360.png", width=60)
    svc = st.number_input("📊 SVC (L)", min_value=0.0, step=0.1)
    mvv = st.number_input("🫁 MVV (L/min)", min_value=0.0, step=0.1)

    if st.button("Submit FVC Test"):
        st.success("✅ FVC Test Saved")

# 5. Report Tab
with tabs[4]:
    st.image("https://cdn-icons-png.flaticon.com/512/3039/3039437.png", width=60)
    st.subheader("🧾 Summary Report")

    st.markdown("#### 👤 Patient Info")
    st.markdown(f"- Name: **{name if name else 'N/A'}**")
    st.markdown(f"- Age: **{age if age else 'N/A'}**")
    st.markdown(f"- Gender: **{gender if gender else 'N/A'}**")
    st.markdown(f"- ID: **{patient_id if patient_id else 'N/A'}**")

    st.mark
