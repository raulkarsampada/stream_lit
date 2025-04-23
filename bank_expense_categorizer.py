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
st.caption("Built with ❤️ by Your Name")  # Replace with your name

# --- NAVIGATION ---
tab1, tab2, tab3 = st.tabs(["🏠 Main Budget", "🔐 Emergency Access", "ℹ️ Info"])

# --- MAIN BUDGET TAB ---
with tab1:
    st.header("💸 Monthly Budget Setup")
    
    st.markdown("""
        <div style='background-color: #e8f5e9; padding: 10px; border-radius: 8px;'>
            <h3 style="color:#388e3c">Set up your monthly budget by allocating funds across categories</h3>
        </div>
    """, unsafe_allow_html=True)

    # Income input
    income = st.number_input("Enter your monthly income (₹)", min_value=0, value=30000, step=1000)

    st.subheader("📊 Allocate your budget manually")
    
    # Manual inputs for each category
    groceries = st.number_input("Groceries (₹)", min_value=0, value=5000, step=500)
    clothes = st.number_input("Clothes (₹)", min_value=0, value=5000, step=500)
    savings = st.number_input("Savings (₹)", min_value=0, value=10000, step=500)
    send_home = st.number_input("Send Home (₹)", min_value=0, value=10000, step=500)

    total = groceries + clothes + savings + send_home
    remaining = income - total

    # Showing budget summary
    st.markdown("---")
    st.success(f"Total Allocated: ₹{total}")
    st.info(f"Remaining Balance: ₹{remaining}")

    # Option to view details or reset budget
    with st.expander("📅 View All Details"):
        st.write(f"**Income**: ₹{income}")
        st.write(f"**Groceries**: ₹{groceries}")
        st.write(f"**Clothes**: ₹{clothes}")
        st.write(f"**Savings**: ₹{savings}")
        st.write(f"**Send Home**: ₹{send_home}")

# --- EMERGENCY ACCESS TAB ---
with tab2:
    st.header("🚨 Emergency Funds Access")
    st.markdown("""
        <div style='background-color: #ffebee; padding: 10px; border-radius: 8px;'>
            <h3 style="color:#d
