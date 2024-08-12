import streamlit as st

st.set_page_config(page_title="Food lab", page_icon="🍲")

def home():
    st.title("Welcome to FoodLab!")
    st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freethephd.com%2F2017%2F03%2F27%2Feating-scientific-impact-the-food-lab%2F&psig=AOvVaw0F9uZG1lkaJONSlV4ksqSl&ust=1723528372447000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCMjK6tjh7ocDFQAAAAAdAAAAABAE", use_column_width=True)
    st.markdown("""
    **Foodie Hub** is your one-stop solution for delicious recipes, grocery stores, cloud kitchens, and a platform for aspiring chefs and hotel management enthusiasts. 
    Use the navigation on the left to explore more!
    """)

def recipes():
    st.title("Recipe of the Day")
    st.header("Spaghetti Carbonara")
    st.image("https://images.unsplash.com/photo-1525351484163-7529414344d8", use_column_width=True)
    st.markdown("""
    **Ingredients:**
    - 200g Spaghetti
    - 100g Pancetta
    - 2 Large Eggs
    - 50g Pecorino Cheese
    - Freshly Ground Black Pepper
    - Salt

    **Instructions:**
    1. Cook the spaghetti in salted boiling water.
    2. Fry the pancetta in a hot pan until crispy.
    3. Beat the eggs with cheese and pepper.
    4. Drain the pasta and mix with the pancetta and egg mixture.
    5. Serve immediately with extra cheese and pepper on top.
    """)
    st.markdown("[Find More Recipes](https://www.allrecipes.com/)")

def kitchen_resources():
    st.title("Grocery Stores & Cloud Kitchens")
    st.header("Grocery Stores")
    st.markdown("""
    - [Walmart](https://www.walmart.com/)
    - [Kroger](https://www.kroger.com/)
    - [Whole Foods](https://www.wholefoodsmarket.com/)
    """)
    
    st.header("Cloud Kitchens")
    st.markdown("""
    - [CloudKitchens](https://www.cloudkitchens.com/)
    - [Reef Technology](https://reeftechnology.com/)
    - [Kitchen United](https://www.kitchenunited.com/)
    """)

def part_time_workers():
    st.title("Part-Time Work Opportunities")
    st.markdown("""
    **Love to Cook or into Hotel Management?**
    Apply now to kickstart your career!
    - [Indeed](https://www.indeed.com/q-Part-Time-Chef-jobs.html)
    - [LinkedIn](https://www.linkedin.com/jobs/part-time-chef-jobs/)
    - [Hcareers](https://www.hcareers.com/)
    """)

menu = ["Home", "Recipes", "Grocery Stores & Cloud Kitchens", "Part-Time Work Opportunities"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    home()
elif choice == "Recipes":
    recipes()
elif choice == "Grocery Stores & Cloud Kitchens":
    kitchen_resources()
elif choice == "Part-Time Work Opportunities":
    part_time_workers()

st.sidebar.markdown("---")
st.sidebar.markdown("© 2024 Foodie Hub")
