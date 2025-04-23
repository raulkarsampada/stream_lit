import streamlit as st

st.set_page_config(page_title="Bank Expense Manager", layout="centered")

st.title("💰 Bank Expense Manager")
st.caption("Built with ❤️ by Your Name")  # ← Replace with your name

# --- NAVIGATION ---
tab1, tab2, tab3 = st.tabs(["🏠 Main Budget", "🔐 Emergency Access", "ℹ️ Info"])

# --- MAIN BUDGET TAB ---
with tab1:
    st.header("💸 Monthly Budget Setup")

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

    st.markdown("----")
    st.success(f"Total Allocated: ₹{total}")
    st.info(f"Remaining Balance: ₹{remaining}")

# --- EMERGENCY ACCESS TAB ---
with tab2:
    st.header("🚨 Emergency Funds Access")

    password = st.text_input("Enter emergency password", type="password")

    if password == "letmein123":  # 🔐 Change this to your secret password!
        st.success("Access granted to Emergency Funds section.")
        emergency_funds = st.number_input("How much do you want to access?", min_value=0, step=500)
        st.warning(f"You are trying to access ₹{emergency_funds} from your emergency funds.")
    elif password:
        st.error("Incorrect password. Try again or leave it blank.")

# --- INFO TAB ---
with tab3:
    st.header("ℹ️ About This App")
    st.markdown("""
    This app helps you manually divide your monthly income into key expense categories.  
    Use the Emergency tab only when truly needed — and protect your password! 🔐  
    Customize it anytime to track your own personal budgeting goals.
    """)  # ✅ Fixed here by closing the triple quotes properly

