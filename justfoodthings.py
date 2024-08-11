import streamlit as st
import pandas as pd

# Load data
recipes_df = pd.read_csv('recipes.csv')
grocery_df = pd.read_csv('grocery_items.csv')

# Streamlit app
st.title("Gym Recipe App")

# Navigation sidebar
st.sidebar.title("Navigation")
options = st.sidebar.radio("Choose a section:", ("Home", "Recipes", "Grocery Store", "Cloud Kitchen", "Part-time Cooking Jobs"))

if options == "Home":
    st.subheader("Welcome to the Gym Recipe App")
    st.write("This app provides healthy recipes for gym enthusiasts, grocery items, cloud kitchen services, and opportunities for part-time cooking jobs.")
    
elif options == "Recipes":
    st.subheader("Healthy Recipes")
    st.dataframe(recipes_df)

    recipe_name = st.selectbox("Select a recipe to view details", recipes_df['name'])
    recipe_details = recipes_df[recipes_df['name'] == recipe_name]
    
    if not recipe_details.empty:
        st.write("### Ingredients:")
        st.write(recipe_details['ingredients'].values[0])
        st.write("### Instructions:")
        st.write(recipe_details['instructions'].values[0])
        st.write("### Calories:")
        st.write(recipe_details['calories'].values[0])
    
elif options == "Grocery Store":
    st.subheader("Grocery Store")
    st.dataframe(grocery_df)

    grocery_item = st.selectbox("Select a grocery item to view details", grocery_df['name'])
    grocery_details = grocery_df[grocery_df['name'] == grocery_item]
    
    if not grocery_details.empty:
        st.write("### Quantity:")
        st.write(grocery_details['quantity'].values[0])
        st.write("### Price:")
        st.write(grocery_details['price'].values[0])

elif options == "Cloud Kitchen":
    st.subheader("Cloud Kitchen Services")
    st.write("Explore our cloud kitchen services. Place your order for healthy meals prepared by our chefs.")
    st.write("For more information, contact us at cloudkitchen@example.com")

elif options == "Part-time Cooking Jobs":
    st.subheader("Part-time Cooking Jobs")
    st.write("We are looking for passionate part-time cooks and hotel management enthusiasts.")
    st.write("If you're interested, please send your resume to jobs@example.com")
