import streamlit as st
import pandas as pd

# Sample data for grocery stores, cloud kitchens, part-time jobs, and recipes
grocery_stores = {
    "Store Name": ["Healthy Foods", "Grocery Mart", "Fitness Market"],
    "Location": ["Downtown", "Uptown", "Suburb"],
    "Contact": ["123-456-7890", "234-567-8901", "345-678-9012"]
}

cloud_kitchens = {
    "Kitchen Name": ["Chef's Kitchen", "Home Cooked Meals", "Fitness Food Hub"],
    "Location": ["Downtown", "Uptown", "Suburb"],
    "Contact": ["chef@kitchen.com", "homecook@meals.com", "info@fitnessfoodhub.com"]
}

job_listings = {
    "Job Title": ["Cook", "Kitchen Assistant", "Dishwasher"],
    "Location": ["Downtown Cafe", "Uptown Bistro", "Suburb Restaurant"],
    "Contact": ["admin@downtowncafe.com", "hr@uptownbistro.com", "info@suburbrestaurant.com"]
}

recipes = {
    "Recipe Name": ["Spaghetti Bolognese", "Chicken Curry", "Quinoa Salad", "Protein Smoothie"],
    "Ingredients": [
        "200g Spaghetti, 100g Ground Beef, Tomato Sauce, Onion, Garlic",
        "200g Chicken Breast, Curry Powder, Coconut Milk, Vegetables",
        "1 cup Quinoa, 1/2 cup Cherry Tomatoes, Cucumber, Lemon Dressing",
        "1 Banana, 1 scoop Protein Powder, 1 cup Almond Milk, Spinach"
    ],
    "Calories": [400, 600, 350, 250],
    "Description": [
        "Classic Italian pasta dish with rich meat sauce.",
        "Spicy and flavorful chicken curry with vegetables.",
        "Healthy salad packed with protein and nutrients.",
        "Nutritious smoothie perfect for post-workout."
    ]
}

# Streamlit App
st.title("Food Recipe & Community Platform")

# Recipe Search
st.header("Find Recipes")
food_item = st.text_input("Enter a food item:")
if food_item:
    # Filter recipes based on user input
    filtered_recipes = pd.DataFrame(recipes)
    mask = filtered_recipes['Recipe Name'].str.contains(food_item, case=False)
    result = filtered_recipes[mask]
    
    if not result.empty:
        st.write(result)
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

# Job Listings Section
st.header("Part-time Cooking Jobs")
job_df = pd.DataFrame(job_listings)
st.write(job_df)

# Run the Streamlit app
if __name__ == "__main__":
    st.run()

