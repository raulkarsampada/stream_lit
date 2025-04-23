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
tab1, tab2, tab3 = st.tabs(["🏠 Budget Setup", "🔐 Emergency Access", "ℹ️ Info"])

# --- BUDGET SETUP TAB ---
with tab1:
    st.header("💸 Monthly Budget Setup")
    
    # Add an image to make it visually appealing
    st.image("https://www.example.com/budget-image.jpg", caption="Manage your expenses effectively!", width=500)  # Replace with your own image URL

    st.markdown("""
        <div style='background-color: #e8f5e9; padding: 10px; border-radius: 8px;'>
            <h3 style="color:#388e3c">Allocate your monthly budget</h3>
        </div>
    """, unsafe_allow_html=True)

    # Income input
    income = st.number_input("Enter your monthly income (₹)", min_value=0, value=30000, step=1000)

    st.subheader("📊 Budget Allocation")
    
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

# --- EMERGENCY ACCESS TAB ---
with tab2:
    st.header("🚨 Emergency Funds Access")
    st.markdown("""
        <div style='background-color: #ffebee; padding: 10px; border-radius: 8px;'>
            <h3 style="color:#d32f2f">Enter emergency password</h3>
        </div>
    """, unsafe_allow_html=True)

    password = st.text_input("Enter emergency password", type="password")

    if password == "1105":  # 🔐 Emergency password set to 1105
        st.success("Access granted to Emergency Funds section.")
        emergency_funds = st.number_input("How much do you want to access?", min_value=0, step=500)
        st.warning(f"You are trying to access ₹{emergency_funds} from your emergency funds.")
    elif password:
        st.error("Incorrect password. Try again.")

# --- INFO TAB ---
with tab3:
    st.header("ℹ️ About This App")
    st.markdown("""
        <div style='background-color: #e1f5fe; padding: 10px; border-radius: 8px;'>
            <h3 style="color:#0288d1">This app helps you divide your monthly income into key expense categories.</h3>
        </div>
    """,
