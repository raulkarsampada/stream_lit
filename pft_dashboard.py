import streamlit as st

# Set up page
st.set_page_config(page_title="Pulmonary Function Test", layout="centered")

# Initialize session state for navigation if not already set
if "page" not in st.session_state:
    st.session_state.page = "Patient Info"

# Function to navigate to a new page
def go_to(page_name):
    st.session_state.page = page_name

# Sidebar buttons to navigate
st.sidebar.title("Navigation")
st.sidebar.button("Patient Info", on_click=go_to, args=("Patient Info",))
st.sidebar.button("Expiratory Test", on_click=go_to, args=("Expiratory Test",))
st.sidebar.button("Inspiratory Test", on_click=go_to, args=("Inspiratory Test",))
st.sidebar.button("FVC Test", on_click=go_to, args=("FVC Test",))
st.sidebar.button("Report", on_click=go_to, args=("Report",))

# Page content based on navigation state
page = st.session_state.page

# 1. Patient Info
if page == "Patient Info":
    st.image("https://cdn-icons-png.flaticon.com/512/747/747376.png", width=60)
    st.title("🧑‍⚕️ Patient Information")
    with st.form("patient_info_form"):
        st.session_state.name = st.text_input("Name", st.session_state.get("name", ""))
        st.session_state.age = st.number_input("Age", value=st.session_state.get("age", 0), min_value=0, max_value=120)
        st.session_state.gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=0)
        st.session_state.patient_id = st.text_input("Patient ID", st.session_state.get("patient_id", ""))
        submitted = st.form_submit_button("Save & Continue ➡️")
        if submitted:
            go_to("Expiratory Test")

# 2. Expiratory Test
elif page == "Expiratory Test":
    st.title("💨 Expiratory Test")
    st.session_state.fev1 = st.number_input("FEV1 (L)", value=st.session_state.get("fev1", 0.0), step=0.1)
    st.session_state.fvc_exp = st.number_input("FVC (L)", value=st.session_state.get("fvc_exp", 0.0), step=0.1)
    st.session_state.pef = st.number_input("PEF (L/min)", value=st.session_state.get("pef", 0.0), step=0.1)
    st.session_state.mep = st.number_input("MEP (cmH₂O)", value=st.session_state.get("mep", 0.0), step=0.1)
    if st.button("Next ➡️"):
        go_to("Inspiratory Test")

# 3. Inspiratory Test
elif page == "Inspiratory Test":
    st.title("🫁 Inspiratory Test")
    st.session_state.fivc = st.number_input("FIVC (L)", value=st.session_state.get("fivc", 0.0), step=0.1)
    st.session_state.mip = st.number_input("MIP (cmH₂O)", value=st.session_state.get("mip", 0.0), step=0.1)
    st.session_state.pif = st.number_input("PIF (L/min)", value=st.session_state.get("pif", 0.0), step=0.1)
    if st.button("Next ➡️"):
        go_to("FVC Test")

# 4. FVC Test
elif page == "FVC Test":
    st.title("📊 FVC Test")
    st.session_state.svc = st.number_input("SVC (L)", value=st.session_state.get("svc", 0.0), step=0.1)
    st.session_state.mvv = st.number_input("MVV (L/min)", value=st.session_state.get("mvv", 0.0), step=0.1)
    if st.button("Next ➡️"):
        go_to("Report")

# 5. Report
elif page == "Report":
    st.title("🧾 Final Report")
    st.markdown(f"**Name:** {st.session_state.get('name', 'N/A')}")
    st.markdown(f"**Age:** {st.session_state.get('age', 'N/A')}")
    st.markdown(f"**Gender:** {st.session_state.get('gender', 'N/A')}")
    st.markdown(f"**Patient ID:** {st.session_state.get('patient_id', 'N/A')}")
    st.markdown("---")
    st.markdown("### Expiratory Test")
    st.markdown(f"- FEV1: {st.session_state.get('fev1', 'N/A')} L")
    st.markdown(f"- FVC: {st.session_state.get('fvc_exp', 'N/A')} L")
    st.markdown(f"- PEF: {st.session_state.get('pef', 'N/A')} L/min")
    st.markdown(f"- MEP: {st.session_state.get('mep', 'N/A')} cmH₂O")
    st.markdown("### Inspiratory Test")
    st.markdown(f"- FIVC: {st.session_state.get('fivc', 'N/A')} L")
    st.markdown(f"- MIP: {st.session_state.get('mip', 'N/A')} cmH₂O")
    st.markdown(f"- PIF: {st.session_state.get('pif', 'N/A')} L/min")
    st.markdown("### FVC Test")
    st.markdown(f"- SVC: {st.session_state.get('svc', 'N/A')} L")
    st.markdown(f"- MVV: {st.session_state.get('mvv', 'N/A')} L/min")

    if st.button("⬅️ Back to Start"):
        go_to("Patient Info")
