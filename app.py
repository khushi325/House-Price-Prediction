import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Project title
st.title("🏠 House Price Prediction System")

st.markdown("""
This application predicts the price of a house using a trained Random Forest Machine Learning model.
""") 

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Model",
        value="Random Forest"
    )

with col2:
    st.metric(
        label="Accuracy (R²)",
        value="87.59%"
    )

with col3:
    st.metric(
        label="Dataset Records",
        value="14,620"
    )

st.markdown("---")

# Sidebar

st.sidebar.title("🏠 Project Details")

st.sidebar.info("""
**Algorithm:** Random Forest Regressor

**Dataset:** House Price India

**Training Records:** 14,620

**Input Features:** 19

**Model Accuracy (R²):** 87.59%
""")
 
st.sidebar.markdown("---")

st.sidebar.success("Best Model Selected")

st.sidebar.write("✔ Random Forest")

st.sidebar.write("✔ Trained Successfully")

st.sidebar.write("✔ Ready for Prediction")

col1, col2 = st.columns(2)

with col1:

    bedrooms = st.number_input(
        "Number of Bedrooms",
        min_value=1,
        max_value=15,
        value=3
    )

    bathrooms = st.number_input(
        "Number of Bathrooms",
        min_value=1,
        max_value=10,
        value=2
    )

    living_area = st.number_input(
        "Living Area (sq ft)",
        value=1800
    )

    lot_area = st.number_input(
        "Lot Area (sq ft)",
        value=5000
    )

    floors = st.number_input(
        "Number of Floors",
        min_value=1,
        max_value=5,
        value=2
    )


house_area = st.number_input(
    "House Area (Without Basement)",
    value=1500
)

built_year = st.number_input(
    "Built Year",
    min_value=1900,
    max_value=2026,
    value=2005
)

latitude = st.number_input(
    "Latitude",
    value=28.60,
    format="%.4f"
)

living_area_renov = st.number_input(
    "Living Area After Renovation",
    value=1800
)

schools = st.number_input(
    "Number of Schools Nearby",
    min_value=0,
    value=2
)


with col2:

    waterfront = st.selectbox(
        "Waterfront Present",
        [0, 1]
    )

    views = st.slider(
        "Number of Views",
        0,
        4,
        1
    )

    condition = st.slider(
        "Condition of House",
        1,
        5,
        3
    )

    grade = st.slider(
        "Grade of House",
        1,
        13,
        7
    )

    basement = st.number_input(
        "Basement Area",
        value=500
    )

    renovation_year = st.number_input(
    "Renovation Year",
    min_value=0,
    max_value=2026,
    value=0
)

longitude = st.number_input(
    "Longitude",
    value=77.10,
    format="%.4f"
)

lot_area_renov = st.number_input(
    "Lot Area After Renovation",
    value=5000
)

airport_distance = st.number_input(
    "Distance From Airport (km)",
    value=15
)

# Predict house price

if st.button("Predict House Price"):

    input_data = pd.DataFrame([{
        "number of bedrooms": bedrooms,
        "number of bathrooms": bathrooms,
        "living area": living_area,
        "lot area": lot_area,
        "number of floors": floors,
        "waterfront present": waterfront,
        "number of views": views,
        "condition of the house": condition,
        "grade of the house": grade,
        "Area of the house(excluding basement)": house_area,
        "Area of the basement": basement,
        "Built Year": built_year,
        "Renovation Year": renovation_year,
        "Lattitude": latitude,
        "Longitude": longitude,
        "living_area_renov": living_area_renov,
        "lot_area_renov": lot_area_renov,
        "Number of schools nearby": schools,
        "Distance from the airport": airport_distance
    }])

    prediction = model.predict(input_data)

    st.markdown("---")

    st.success("Prediction Completed Successfully")

    st.metric(
       label="Estimated House Price",
       value=f"₹ {prediction[0]:,.2f}"
)

