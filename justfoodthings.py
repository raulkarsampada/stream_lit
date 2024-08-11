import streamlit as st
import pandas as pd

recipes_data = {
    'Recipe': ['Protein Smoothie', 'Quinoa Salad', 'Chicken Stir-Fry'],
    'Ingredients': [
        'Protein powder, Banana, Almond milk, Spinach',
        'Quinoa, Chickpeas, Bell peppers, Olive oil, Lemon juice',
        'Chicken breast, Broccoli, Soy sauce, Garlic, Ginger'
    ],
    'Instructions': [
        'Blend all ingredients until smooth.',
        'Mix all ingredients in a bowl and dress with olive oil and lemon juice.',
        'Stir-fry chicken with garlic and ginger, add broccoli and soy sauce.'
    ],
    'Calories': [250, 400, 350]
}

grocery_data = {
    'Item': ['Protein powder', 'Banana', 'Quinoa', 'Chickpeas', 'Bell peppers', 'Chicken breast', 'Broccoli'],
    'Quantity': ['1 lb', '5 pieces', '500 g', '400 g', '3 pieces', '1 kg', '1 bunch'],
    'Price': [25.0, 1.0, 7.0, 3.0, 2.5, 10.0, 3.5]
}

recipes_df = pd.DataFrame(recipes_data)
grocery_df = pd.DataFrame(grocery_data)

st.title('Healthy Living Platform')

st.sidebar.title('Navigation')
option = st.sidebar.selectbox('Select a section:', ['Home', 'Recipes', 'Grocery Store', 'Cloud Kitchen', 'Part-Time Opportunities'])

if option == 'Home':
    st.write('Welcome to the Healthy Living Platform. Explore recipes, grocery items, and opportunities for part-time work in the food industry.')

elif option == 'Recipes':
    st.write('### Recipes for Gym Enthusiasts')
    st.dataframe(recipes_df)

elif option == 'Grocery Store':
    st.write('### Grocery Store')
    st.dataframe(grocery_df)

elif option == 'Cloud Kitchen':
    st.write('### Cloud Kitchen Services')
    st.write('Explore cloud kitchen services and partnerships. For more details, contact us directly.')

elif option == 'Part-Time Opportunities':
    st.write('### Part-Time Opportunities')
    st.write('If you love cooking or are interested in hotel management, check out these opportunities:')
    st.write('- Cook at local restaurants')
    st.write('- Work as a kitchen assistant')
    st.write('- Explore hotel management internships')
    st.write('Visit our careers page for more details.')
