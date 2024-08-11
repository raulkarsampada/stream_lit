import streamlit as st
import pandas as pd

# Sample data for grocery stores, cloud kitchens, part-time jobs, and recipes
grocery_stores = {
    "Store Name": ["Healthy Foods", "Grocery Mart", "Fitness Market"],
    "Location": ["Downtown", "Uptown", "Suburb"],
    "Contact": ["123-456-7890", "234-567-8901", "345-678-9012"]
}

cloud_kitchens = {
    "Kitchen Name": ["Chef's Kitchen", "Home Cooked Meals", "Healthy Eats"],
    "Location": ["Downtown", "Uptown", "Suburb"],
    "Contact": ["chef@kitchen.com", "homecook@meals.com", "info@healthyeats.com"]
}

job_listings = {
    "Job Title": ["Cook", "Kitchen Assistant", "Dishwasher", "Server"],
    "Location": ["Downtown Cafe", "Uptown Bistro", "Suburb Restaurant", "Hotel XYZ"],
    "Contact": ["admin@downtowncafe.com", "hr@uptownbistro.com", "info@suburbrestaurant.com", "hr@hotelxyz.com"],
    "Apply URL": [
        "https://example.com/apply-cook",
        "https://example.com/apply-kitchen-assistant",
        "https://example.com/apply-dishwasher",
        "https://example.com/apply-server"
    ]
}

recipes = {
    "Recipe Name": ["Protein Pancakes", "Grilled Chicken Salad", "Quinoa Bowl", "Beef Stir Fry"],
    "Ingredients": [
        "2 Eggs, 1/2 cup Oats, 1/2 Banana, 1 scoop Protein Powder",
        "200g Grilled Chicken, Lettuce, Cherry Tomatoes, Avocado",
        "1 cup Quinoa, 1 cup Mixed Vegetables, Olive Oil, Lemon Juice",
        "200g Beef, Broccoli, Bell Peppers, Soy Sauce, Garlic"
    ],
    "Calories": [300, 400, 350, 500],
    "Description": [
        "High-protein pancakes perfect for breakfast.",
        "A healthy salad packed with protein and nutrients.",
        "A nutritious bowl rich in protein and fiber.",
        "Flavorful beef stir fry with vegetables."
    ]
}

# Streamlit App
st.title("Gym Recipe & Community Platform")

# Recipe Search
st.header("Find Recipes for Gym Enthusiasts")
food_item = st.text_input("Enter a food item:")
if food_item:
    # Filter recipes based on user input
    filtered_recipes = pd.DataFrame(recipes)
    mask = filtered_recipes['Recipe Name'].str.contains(food_item, case=False)
    result = filtered_recipes[mask]
    
    if not result.empty:
        st.write("### Matching Recipes:")
        st.dataframe(result)
    else:
        st.write("No recipes found for that food item.")

# Grocery Store Section
st.header("Grocery Stores")
store_df = pd.DataFrame(grocery_stores)
st.write(store_df)

# Cloud Kitchen Section
st.header("Cloud Kitchens")
kitchen_df = pd.DataFrame(cloud_kitchens)
st.write(kitchen_df)

# Link to add a new Cloud Kitchen
st.markdown("[Add Your Cloud Kitchen](https://example.com/add-kitchen)")

# Job Listings Section
st.header("Part-time Cooking Jobs")
job_df = pd.DataFrame(job_listings)
st.write(job_df)

# Add Apply Links
for index, row in job_df.iterrows():
    st.markdown(f"[Apply for {row['Job Title']} at {row['Location']}]({row['Apply URL']})")
