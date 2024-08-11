import streamlit as st

# Sample data for recipes, grocery stores, and cloud kitchens
recipes = {
    "Spaghetti Bolognese": "https://example.com/spaghetti-bolognese",
    "Chicken Curry": "https://example.com/chicken-curry",
    "Vegetarian Pizza": "https://example.com/vegetarian-pizza",
}

grocery_stores = {
    "Fresh Market": "https://example.com/fresh-market",
    "Grocery Hub": "https://example.com/grocery-hub",
    "Daily Needs": "https://example.com/daily-needs",
}

cloud_kitchens = {
    "Kitchen A": "https://example.com/kitchen-a",
    "Kitchen B": "https://example.com/kitchen-b",
    "Kitchen C": "https://example.com/kitchen-c",
}

part_time_jobs = {
    "Apply Here": "https://example.com/apply-here",
}

# Streamlit app
st.title("Food Lovers' Hub")

st.header("1. Discover Recipes")
st.write("Here are some popular recipes you can try:")
for recipe, url in recipes.items():
    st.write(f"[{recipe}]({url})")

st.header("2. Find Grocery Stores Near You")
st.write("Check out these grocery stores for all your cooking needs:")
for store, url in grocery_stores.items():
    st.write(f"[{store}]({url})")

st.header("3. Explore Cloud Kitchens")
st.write("Order from these cloud kitchens to enjoy delicious meals delivered to your doorstep:")
for kitchen, url in cloud_kitchens.items():
    st.write(f"[{kitchen}]({url})")

st.header("4. Join Our Community of Cooks")
st.write("Are you passionate about cooking? Apply for part-time work here:")
for job, url in part_time_jobs.items():
    st.write(f"[{job}]({url})")

st.write("We are here to support your culinary journey!")
