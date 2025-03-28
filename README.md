🌍 Unit Converter App
Unit Converter Streamlit License

🚀 A simple and interactive Unit Converter App built with Streamlit. Convert Length, Weight, and Time units instantly with a clean and user-friendly interface.

✨ Features
📏 Convert Length: Kilometers ↔ Miles
⚖ Convert Weight: Kilograms ↔ Pounds
⏱ Convert Time: Seconds, Minutes, Hours, Days
🎯 Real-time Conversion
🖥 Simple & Interactive UI
📸 Preview
Unit Converter App

🛠 Installation
⿡ Clone the Repository
git clone https://github.com/AyeshaNadeem123/Unit_Converter
cd unit-converter-app
⿢ Install Dependencies
pip install streamlit
⿣ Run the App
streamlit run app.py
📝 Step-by-Step Guide
⿡ Importing Streamlit
import streamlit as st
Streamlit is a Python library used to build interactive web applications.
st is the alias for Streamlit, making it easier to call functions.
⿢ Setting Up the Title and Description
st.title("🌍Unit Converter App")
st.markdown("### Converts Length, Weight And Time Instantly")
st.write("Welcome! Select a category, enter a value and get the converted result in real-time")
st.title() adds the main heading of the app.
st.markdown() adds a subheading.
st.write() displays an introductory text.
⿣ Choosing a Category
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])
st.selectbox() creates a dropdown menu for users to select a conversion category:
📏 Length
⚖ Weight
⏱ Time
⿤ Function to Convert Units
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
            
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
    
    return 0  # Default return if no conversion is selected
The function convert_units() takes three inputs:
category (Length, Weight, or Time)
value (number to be converted)
unit (conversion type)
It performs the conversion based on the selected unit and returns the result.
⿥ Selecting the Conversion Type Based on Category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Miles to Kilometers","Kilometers to Miles"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("⏱ Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])
Depending on the selected category, another dropdown appears to choose the specific conversion unit.
st.selectbox() is used again to display different conversion options.
⿦ Taking User Input
value = st.number_input("Enter the value to convert")
st.number_input() allows users to input a number for conversion.
⿧ Performing Conversion When Button is Clicked
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
st.button("Convert") adds a button that triggers the conversion when clicked.
The convert_units() function is called with the user inputs.
st.success(f"The result is {result:.2f}") displays the final converted value.
🎯 Final Output
When you run this Streamlit app:

✅ It shows a title, description, and dropdown for selecting the conversion category.
✅ Based on the selected category, another dropdown appears for choosing a unit conversion.
✅ A number input box allows users to enter a value.
✅ When clicking "Convert", the app calculates and displays the converted result.
💡 How to Run This Code?

