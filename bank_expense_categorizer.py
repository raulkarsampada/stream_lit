import streamlit as st
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="Random Bank Expense Split", layout="centered")

st.title("🎲 Random Expense Divider")

# Get user income
income = st.number_input("Enter your monthly income (₹)", min_value=0, value=30000, step=1000)

st.markdown("----")

# Expense categories
categories = ["Groceries", "Clothes", "Savings", "Send Home", "Entertainment", "Bills"]

# Generate random allocation percentages that sum to 100
def generate_random_allocation(categories):
    weights = [random.randint(1, 100) for _ in categories]
    total_weight = sum(weights)
    return {cat: round((w / total_weight) * income) for cat, w in zip(categories, weights)}

# Create allocation
allocations = generate_random_allocation(categories)

st.subheader("📊 Randomly Allocated Expenses:")

total_allocated = 0
for category, amount in allocations.items():
    st.write(f"- **{category}**: ₹{amount}")
    total_allocated += amount

remaining = income - total_allocated
st.markdown("----")

# Show remaining balance
st.info(f"Remaining Balance: ₹{remaining}")

# Pie chart
st.subheader("📈 Expense Distribution Chart")
fig, ax = plt.subplots()
ax.pie(allocations.values(), labels=allocations.keys(), autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Option to re-randomize
if st.button("🔁 Re-Randomize Allocation"):
    st.experimental_rerun()
