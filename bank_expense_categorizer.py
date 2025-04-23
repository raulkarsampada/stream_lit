import streamlit as st

# Set the page title
st.set_page_config(page_title="Bank Account Expense Manager", layout="centered")

# Title of the app
st.title("💰 Bank Account Expense Manager")

# Input for monthly income
income = st.number_input("Enter your monthly income (₹)", min_value=0, value=30000, step=1000)

st.markdown("---")

# Default allocations (you can customize this)
st.subheader("📊 Allocate your income into categories:")
default_allocations = {
    "Groceries": 5000,
    "Clothes": 5000,
    "Savings": 10000,
    "Send Home": 10000
}

# Editable sliders for each category
allocations = {}
total_allocated = 0

for category, default_value in default_allocations.items():
    allocations[category] = st.slider(
        f"{category} (₹)", 
        0, 
        income, 
        default_value, 
        step=500
    )
    total_allocated += allocations[category]

# Remaining balance
remaining = income - total_allocated

st.markdown("---")

# Display results
if remaining < 0:
    st.error(f"🚫 Over-allocated by ₹{abs(remaining)}. Adjust your categories.")
else:
    st.success(f"✅ Remaining Balance: ₹{remaining}")

    st.subheader("💼 Summary:")
    for category, amount in allocations.items():
        st.write(f"- **{category}**: ₹{amount}")

# Optional: Pie chart
if st.checkbox("Show Pie Chart"):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.pie(allocations.values(), labels=allocations.keys(), autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
