import streamlit as st

# Sample data for nutritional foods
recipes = {
    "Grilled Chicken Salad": {
        "ingredients": ["Chicken Breast", "Mixed Greens", "Cherry Tomatoes", "Cucumber", "Olive Oil", "Lemon Juice"],
        "nutrition": {
            "calories": 350,
            "protein": 40,
            "carbs": 15,
            "fat": 15
        },
        "instructions": "1. Grill the chicken until cooked through.\n2. Chop the vegetables.\n3. Toss everything in a bowl and drizzle with olive oil and lemon juice.",
        "video_link": "https://www.youtube.com/watch?v=example1"
    },
    "Protein Smoothie": {
        "ingredients": ["Banana", "Protein Powder", "Almond Milk", "Spinach", "Peanut Butter"],
        "nutrition": {
            "calories": 300,
            "protein": 30,
            "carbs": 40,
            "fat": 10
        },
        "instructions": "1. Combine all ingredients in a blender.\n2. Blend until smooth.",
        "video_link": "https://www.youtube.com/watch?v=example2"
    },
    "Quinoa and Black Beans": {
        "ingredients": ["Quinoa", "Black Beans", "Corn", "Red Pepper", "Lime", "Cilantro"],
        "nutrition": {
            "calories": 450,
            "protein": 15,
            "carbs": 70,
            "fat": 10
        },
        "instructions": "1. Cook quinoa according to package instructions.\n2. Mix in black beans, corn, and diced red pepper.\n3. Squeeze lime juice and add cilantro.",
        "video_link": "https://www.youtube.com/watch?v=example3"
    }
}

# Grocery store link
grocery_store_link = "https://www.examplegrocerystore.com"

# Cloud kitchen link
cloud_kitchen_link = "https://www.examplecloudkitchen.com"

# Cooking classes link
cooking_classes_link = "https://www.examplecookingclasses.com"

# Streamlit app
st.title("Nutritional Recipes for Gym Enthusiasts")

st.sidebar.header("Choose a Recipe")
recipe_choice = st.sidebar.selectbox("Select a Recipe", list(recipes.keys()))

st.subheader(recipe_choice)

# Display selected recipe details
selected_recipe = recipes[recipe_choice]
st.write("### Ingredients:")
for ingredient in selected_recipe["ingredients"]:
    st.write(f"- {ingredient}")

st.write("### Nutrition Facts:")
st.write(f"- Calories: {selected_recipe['nutrition']['calories']}")
st.write(f"- Protein: {selected_recipe['nutrition']['protein']}g")
st.write(f"- Carbohydrates: {selected_recipe['nutrition']['carbs']}g")
st.write(f"- Fat: {selected_recipe['nutrition']['fat']}g")

st.write("### Instructions:")
st.write(selected_recipe["instructions"])

# Display video tutorial link
st.write("### Video Tutorial:")
st.write(f"[Watch how to make {recipe_choice}]({selected_recipe['video_link']})")

# Links to grocery store, cloud kitchen, and cooking classes
st.write("### Grocery Store")
st.write(f"[Shop here]({grocery_store_link}) for ingredients.")

st.write("### Cloud Kitchen")
st.write(f"[Order from our cloud kitchen]({cloud_kitchen_link}) for meal prep.")

st.write("### Cooking Classes")
st.write(f"[Join cooking classes]({cooking_classes_link}) to learn more cooking skills.")

