import streamlit as st

# Function to display recipes
def show_recipes():
    st.header("Food Recipes")
    recipes = {
        "Spaghetti Carbonara": {
            "Ingredients": ["Spaghetti", "Eggs", "Parmesan cheese", "Pancetta", "Black pepper"],
            "Instructions": "Cook spaghetti. In a separate bowl, mix eggs and cheese. Fry pancetta until crispy. Combine everything and add black pepper."
        },
        "Chicken Curry": {
            "Ingredients": ["Chicken", "Onions", "Tomatoes", "Garlic", "Spices", "Coconut milk"],
            "Instructions": "Sauté onions and garlic. Add chicken and brown it. Add tomatoes and spices, cook until fragrant. Add coconut milk and simmer until chicken is cooked."
        }
    }

    for recipe, details in recipes.items():
        st.subheader(recipe)
        st.write("**Ingredients:**")
        st.write(", ".join(details["Ingredients"]))
        st.write("**Instructions:**")
        st.write(details["Instructions"])

# Function to display grocery store URLs
def show_grocery_stores():
    st.header("Grocery Stores")
    grocery_stores = {
        "Local Grocery Store": "https://localgrocerystore.com",
        "Organic Food Market": "https://organicfoodmarket.com"
    }

    for store, url in grocery_stores.items():
        st.markdown(f"[{store}]({url})")

# Function to display cloud kitchen URLs
def show_cloud_kitchens():
    st.header("Cloud Kitchens")
    cloud_kitchens = {
        "Kitchen Hub": "https://kitchenhub.com",
        "CloudEats": "https://cloudeats.com"
    }

    for kitchen, url in cloud_kitchens.items():
        st.markdown(f"[{kitchen}]({url})")

# Function to display part-time job platform URLs
def show_part_time_jobs():
    st.header("Part-Time Job Opportunities")
    job_platforms = {
        "CookUp": "https://cookup.com",
        "Hotel Management Jobs": "https://hotelmanagementjobs.com"
    }

    for platform, url in job_platforms.items():
        st.markdown(f"[{platform}]({url})")

# Streamlit navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Recipes", "Grocery Stores", "Cloud Kitchens", "Part-Time Jobs"])

if options == "Recipes":
    show_recipes()
elif options == "Grocery Stores":
    show_grocery_stores()
elif options == "Cloud Kitchens":
    show_cloud_kitchens()
elif options == "Part-Time Jobs":
    show_part_time_jobs()
