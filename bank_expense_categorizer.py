import streamlit as st

st.set_page_config(page_title="Bank Expense Manager", layout="centered")

# Custom styling (minimalistic)
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
tabs = st.tabs(["🏠 Budget Setup", "🔐 Emergency Access", "ℹ️ Info"])

# --- BUDGET SETUP TAB ---
with tabs[0]:
    st.header("💸 Monthly Budget Setup")
    
    # Add an image to make it visually appealing
    st.image("https://www.example.com/budget-image.jpg", caption="Manage your expenses effectively!", width=500)  # Replace with your own image URL

    st.markdown("""
        <div style='background-color: #e8f5e9; padding: 10px; border-radius: 8px;'>
            <h3 style="color
