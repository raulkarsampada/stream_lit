import streamlit as st

st.set_page_config(page_title="Bank Expense Manager", layout="centered")

# Custom styling (optional)
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 10px;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #4CAF50;
    }
    .stNumberInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #4CAF50;
    }
    .stTabs>div>div>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("💰 Bank Expense Manager")
st.caption("Built with ❤️ by Sampada Raulkar")  # Your name added here

# --- NAVIGATION ---
tab1, tab2, tab3 = st.tabs(["🏠 Main Budget", "🔐 Emergency Access", "ℹ️ Info"])

# --- MAIN BUDGET TAB ---
with tab1:
