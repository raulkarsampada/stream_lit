import streamlit as st

# Function to display the Home page
def home():
    st.title("Welcome to Foodies' Hub")
    st.write("Your one-stop solution for recipes, groceries, cloud kitchens, and part-time work opportunities.")

# Function to display the Recipes page
def recipes():
    st.title("Food Recipes")
    st.write("Here are some delicious recipes for you to try!")
    
    recipe_list = {
        "Spaghetti Carbonara": "https://www.allrecipes.com/recipe/11973/spaghetti-carbonara-ii/",
        "Chicken Curry": "https://www.bbcgoodfood.com/recipes/chicken-curry",
        "Vegetarian Pizza": "https://www.simplyrecipes.com/recipes/vegetarian_pizza/",
    }

    for recipe, url in recipe_list.items():
        st.markdown(f"[{recipe}]({url})")

# Function to display the Grocery Stores page
def grocery_stores():
    st.title("Grocery Stores")
    st.write("Find the best grocery stores near you.")
    
    grocery_list = {
        "Amazon Fresh": "https://www.amazon.com/alm/storefront?almBrandId=QW1hem9uIEZyZXNo",
        "Walmart Grocery": "https://grocery.walmart.com/",
        "Instacart": "https://www.instacart.com/",
    }

    for store, url in grocery_list.items():
        st.markdown(f"[{store}]({url})")

# Function to display the Cloud Kitchens page
def cloud_kitchens():
    st.title("Cloud Kitchens")
    st.write("Explore cloud kitchens for quick and delicious meals.")
    
    kitchen_list = {
        "Reef Kitchens": "https://reeftechnology.com/kitchens",
        "Ghost Kitchen Brands": "https://www.ghostkitchenbrands.com/",
        "Kitopi": "https://www.kitopi.com/",
    }

    for kitchen, url in kitchen_list.items():
        st.markdown(f"[{kitchen}]({url})")

# Function to display the Job Opportunities page
def job_opportunities():
    st.title("Part-time Work Opportunities")
    st.write("Apply for part-time work opportunities in cooking and hotel management.")
    
    job_list = {
        "Indeed": "https://www.indeed.com/q-Part-Time-Cooking-jobs.html",
        "Glassdoor": "https://www.glassdoor.com/Job/part-time-hotel-management-jobs-SRCH_KO0,28.htm",
        "LinkedIn": "https://www.linkedin.com/jobs/part-time-hotel-management-jobs/",
    }

    for job, url in job_list.items():
        st.markdown(f"[{job}]({url})")

# Navigation
st.sidebar.title("Navigation")
pages = {
    "Home": home,
    "Recipes": recipes,
    "Grocery Stores": grocery_stores,
    "Cloud Kitchens": cloud_kitchens,
    "Job Opportunities": job_opportunities
}

selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
pages[selection]()

