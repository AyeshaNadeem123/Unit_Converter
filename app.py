import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="wide")
st.title("Unit Converter App")
st.info("**Adjust Conversion Options:** Select the conversion category (Length, Weight, or Temperature) from the sidebar and choose the units you want to convert between.")

st.write("Convert units for Length, Weight, and Temperature easily.")

# Sidebar: Choose conversion category 
conversion_category = st.sidebar.selectbox("Select Conversion Category:", ["Length", "Weight", "Temperature"])

# --- Length Conversion ---
if conversion_category == "Length":
    st.header("Length Conversion")

    # Define available units and conversion factors (to meters)
    length_units = ["Meter", "Kilometer", "Foot"]
    conversion_to_meter = {
        "Meter": 1,
        "Kilometer": 1000,
        "Foot": 0.3048
    }

    input_value = st.number_input("Enter value:", value=1.0, key="length_value")
    from_unit = st.selectbox("From:", length_units, key="length_from")
    to_unit = st.selectbox("To:", length_units, key="length_to")

    # Convert input to meters then to target unit 
    value_in_meters = input_value * conversion_to_meter[from_unit]
    converted_value = value_in_meters / conversion_to_meter[to_unit]

    st.write(f"**{input_value} {from_unit}** is equal to **{converted_value:.4f} {to_unit}**.")

# --- Weight Conversion ---
elif conversion_category == "Weight":
    st.header("Weight Conversion")

    weight_units = ["Kilogram", "Gram", "Pound", "Ounce"]
    conversion_to_kg = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }

    input_value = st.number_input("Enter value:", value=1.0, key="weight_value")
    from_unit = st.selectbox("From:", weight_units, key="weight_from")
    to_unit = st.selectbox("To:", weight_units, key="weight_to")

    value_in_kg = input_value * conversion_to_kg[from_unit]
    converted_value = value_in_kg / conversion_to_kg[to_unit]

    st.write(f"**{input_value} {from_unit}** is equal to **{converted_value:.4f} {to_unit}**.")

# --- Temperature Conversion ---
elif conversion_category == "Temperature":
    st.header("Temperature Conversion")

    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    input_value = st.number_input("Enter temperature value:", value=0.0, key="temp_value")
    from_unit = st.selectbox("From:", temp_units, key="temp_from")
    to_unit = st.selectbox("To:", temp_units, key="temp_to")

    # Temperature conversion functions
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    def celsius_to_kelvin(c):
        return c + 273.15

    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    def kelvin_to_celsius(k):
        return k - 273.15

    # Convert input temperature to Celsius first
    if from_unit == "Celsius":
        temp_c = input_value
    elif from_unit == "Fahrenheit":
        temp_c = fahrenheit_to_celsius(input_value)
    else:  # Kelvin
        temp_c = kelvin_to_celsius(input_value)

    # Convert Celsius to target unit
    if to_unit == "Celsius":
        converted_temp = temp_c
    elif to_unit == "Fahrenheit":
        converted_temp = celsius_to_fahrenheit(temp_c)
    else:  # Kelvin
        converted_temp = celsius_to_kelvin(temp_c)

    st.write(f"**{input_value} {from_unit}** is equal to **{converted_temp:.2f} {to_unit}**.")

st.markdown("---")
st.caption("Built with Streamlit - a simple, offline Unit Converter App")
