import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Random Bank Expense Split", layout="centered")

st.title("🎲 Random Expense Divider")

# Get user income
income = st.number_input("Enter your monthly income (₹)", min_value=0, value=30000, step=1000)

st.markdown("----")

# Expense categories
categories = ["Groceries", "Clothes", "Savings", "Send Home", "Entertainment", "Bills"]

# Generate random allocation
def generate_random_allocation(categories):
    weights = [random.randint(1, 100) for _ in categories]
    total_weight = sum(weights)
    return {cat: round((w / total_weight) * income) for cat, w in zip(categories, weights)}

allocations = generate_random_allocation(categories)

# Show allocations
st.subheader("📊 Randomly Allocated Expenses:")
total_allocated = sum_
