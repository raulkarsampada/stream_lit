import streamlit as st

# Sample data for recipes, grocery stores, and cloud kitchens for gym people
recipes = {
    "Grilled Chicken Salad": "https://example.com/grilled-chicken-salad",
    "Protein Pancakes": "https://example.com/protein-pancakes",
    "Quinoa and Black Bean Bowl": "https://example.com/quinoa-black-bean-bowl",
}

grocery_stores = {
    "Healthy Grocers": "https://example.com/healthy-grocers",
    "Organic Food Market": "https://example.com/organic-food-market",
    "Fitness Foods": "https://example.com/fitness-foods",
}

cloud_kitchens = {
    "FitKitchen": "https://example.com/fitkitchen",
    "GymEats": "https://example.com/gymeats",
    "Protein House": "https://example.com/protein-house",
}

part_time_jobs = {
    "Apply Here": "https://example.com/apply-here",
}

# Streamlit app
st.title("Health and Fitness Food Hub")

st.header("1. Explore Healthy Recipes")
st.write("Discover these nutritious recipes perfect for your fitness goals:")
for recipe, url in recipes.items():
    st.write(f"[{recipe}]({url})")

st.header("2. Shop at Nearby Grocery Stores")
st.write("These grocery stores offer a wide range of healthy ingredients:")
for store, url in grocery_stores.items():
    st.write(f"[{store}]({url})")

st.header("3. Order from Cloud Kitchens for Gym Enthusiasts")
st.write("Order healthy meals tailored for your fitness needs from these cloud kitchens:")
for kitchen, url in cloud_kitchens.items():
    st.write(f"[{kitchen}]({url})")

st.header("4. Join Our Team of Culinary Enthusiasts")
st.write("Love cooking or interested in hotel management? Apply for part-time opportunities here:")
for job, url in part_time_jobs.items():
    st.write(f"[{job}]({url})")

st.write("Fuel your body and passion with our resources!")
