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

st.image("https://cdn-icons-png.flaticon.com/512/3004/3004593.png", width=
