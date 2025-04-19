import streamlit as st

# Function to convert length
def convert_length(value, from_unit, to_unit):
    if from_unit == "Meters" and to_unit == "Feet":
        return value * 3.28084
    elif from_unit == "Feet" and to_unit == "Meters":
        return value / 3.28084
    else:
        return value  # No conversion needed

# Streamlit app layout
st.title("Unit Converter App")

# User input
value = st.number_input("Enter the value to convert:", value=0.0)

# Select conversion category (only length)
from_unit = st.selectbox("Select input unit:", ["Meters", "Feet"])
to_unit = st.selectbox("Select output unit:", ["Meters", "Feet"])

if st.button("Convert"):
    if from_unit == to_unit:
        st.write("No conversion needed. The value remains the same.")
    else:
        result = convert_length(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")