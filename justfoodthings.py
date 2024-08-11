import streamlit as st
import pandas as pd

# Sample data for grocery stores, part-time jobs, and recipes
grocery_stores = {
    "Store Name": ["Healthy Foods", "Grocery Mart", "Fitness Market"],
    "Location": ["Downtown", "Uptown", "Suburb"],
    "Contact": ["123-456-7890", "234-567-8901", "345-678-9012"]
}

job_listings = {
    "Job Title": ["Cook", "Kitchen Assistant", "Dishwasher"],
    "Location": ["Downtown Cafe", "Uptown Bistro", "Suburb Restaurant"],
    "Contact": ["admin@downtowncafe.com", "hr@uptownbistro.com", "info@suburbrestaurant.com"]
}

recipes = {
    "Recipe Name": ["Protein Pancakes", "Chicken Salad", "Quinoa Bowl"],
    "Ingredients": [
        "2 Eggs, 1/2 cup Oats, 1/2 Banana, Protein Powder",
        "200g Chicken Breast, Lettuce, Cherry Tomatoes, Olive Oil",
        "1 cup Quinoa, 1 cup Broccoli, 1/2 Avocado, Lemon Juice"
    ],
    "Calories": [250, 300, 400],
    "Description": [
        "High-protein pancakes, great for breakfast.",
        "A healthy salad packed with protein.",
        "A nutritious bowl perfect for lunch."
    ]
}

# Streamlit App
st.title("Gym Recipe & Food Platform")

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

# Job Listings Section
st.header("Part-time Cooking Jobs")
job_df = pd.DataFrame(job_listings)
st.write(job_df)

# Run the Streamlit app
if __name__ == "__main__":
    st.run()

