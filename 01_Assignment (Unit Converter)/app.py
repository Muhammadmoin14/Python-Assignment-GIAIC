import streamlit as st 

st.title('Unit Converter App') 
st.write('Welcome to the Unit Converter App.This is a unit converter assignment which is given by Sir Zia Khan ')

Category_Selected = st.selectbox('Select Category', ['Length', 'Temperature', 'Mass', 'Volume'])  

def Unit_Selction():
    if Category_Selected == 'Length':
        unit_from = st.selectbox('Select From Unit', ['Meter', 'Kilometer', 'Centimeter', 'Millimeter'])
        unit_to = st.selectbox('Select To Unit', ['Meter', 'Kilometer', 'Centimeter', 'Millimeter'])

    elif Category_Selected == 'Temperature':
        unit_from = st.selectbox('Select From Unit', ['Celsius', 'Fahrenheit', 'Kelvin'])
        unit_to = st.selectbox('Select To Unit', ['Celsius', 'Fahrenheit', 'Kelvin'])
    elif Category_Selected == 'Mass':
        unit_from = st.selectbox('Select From Unit', ['Kilogram', 'Gram', 'Milligram', 'Pound'])
        unit_to = st.selectbox('Select To Unit', ['Kilogram', 'Gram', 'Milligram', 'Pound'])
    elif Category_Selected == 'Volume':
        unit_from = st.selectbox('Select From Unit', ['Liter', 'Milliliter', 'Gallon'])
        unit_to = st.selectbox('Select To Unit', ['Liter', 'Milliliter', 'Gallon'])
    return unit_from, unit_to

unit_from, unit_to = Unit_Selction()
st.write(f'You have selected {Category_Selected} category and {unit_from} to {unit_to} conversion')
value = st.text_input('Enter Value')

def Conversion (Category_Selected, value , unit_from, unit_to):
    try :
        value = float(value)
    except:
        return 'Invalid Input'
    
    # If the units are the same, return the value
    if unit_from == unit_to:
        return value
    
    if Category_Selected == 'Length':
        if unit_from == 'Meter' and unit_to == 'Kilometer':
            return value / 1000
        elif unit_from == 'Meter' and unit_to == 'Centimeter':
            return value * 100
        elif unit_from == 'Meter' and unit_to == 'Millimeter':
            return value * 1000
        elif unit_from == 'Kilometer' and unit_to == 'Meter':
            return value * 1000
        elif unit_from == 'Kilometer' and unit_to == 'Centimeter':
            return value * 100000
        elif unit_from == 'Kilometer' and unit_to == 'Millimeter':
            return value * 1000000
        elif unit_from == 'Centimeter' and unit_to == 'Meter':
            return value / 100
        elif unit_from == 'Centimeter' and unit_to == 'Kilometer':
            return value / 100000
        elif unit_from == 'Centimeter' and unit_to == 'Millimeter':
            return value * 10
        elif unit_from == 'Millimeter' and unit_to == 'Meter':
            return value / 1000
        elif unit_from == 'Millimeter' and unit_to == 'Kilometer':
            return value / 1000000
        elif unit_from == 'Millimeter' and unit_to == 'Centimeter':
            return value / 10
    elif Category_Selected == 'Temperature':
        if unit_from == 'Celsius' and unit_to == 'Fahrenheit':
            return (value * 9/5) + 32
        elif unit_from == 'Celsius' and unit_to == 'Kelvin':
            return value + 273.15
        elif unit_from == 'Fahrenheit' and unit_to == 'Celsius':
            return (value - 32) * 5/9
        elif unit_from == 'Fahrenheit' and unit_to == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
        elif unit_from == 'Kelvin' and unit_to == 'Celsius':
            return value - 273.15
        elif unit_from == 'Kelvin' and unit_to == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    elif Category_Selected == 'Mass':
        if unit_from == 'Kilogram' and unit_to == 'Gram':
            return value * 1000
        elif unit_from == 'Kilogram' and unit_to == 'Milligram':
            return value * 1000000
        elif unit_from == 'Kilogram' and unit_to == 'Pound':
            return value * 2.20462
        elif unit_from == 'Gram' and unit_to == 'Kilogram':
            return value / 1000
        elif unit_from == 'Gram' and unit_to == 'Milligram':
            return value * 1000
        elif unit_from == 'Gram' and unit_to == 'Pound':
            return value / 453.592
        elif unit_from == 'Milligram' and unit_to == 'Kilogram':
            return value / 1000000
        elif unit_from == 'Milligram' and unit_to == 'Gram':
            return value / 1000
        elif unit_from == 'Milligram' and unit_to == 'Pound':
            return value / 453592
        elif unit_from == 'Pound' and unit_to == 'Kilogram':
            return value / 2.20462
        elif unit_from == 'Pound' and unit_to == 'Gram':
            return value * 453.592
        elif unit_from == 'Pound' and unit_to == 'Milligram':
            return value * 453592
    elif Category_Selected == 'Volume':
        if unit_from == 'Liter' and unit_to == 'Milliliter':
            return value * 1000
        elif unit_from == 'Liter' and unit_to == 'Gallon':
            return value / 3.78541
        elif unit_from == 'Milliliter' and unit_to == 'Liter':
            return value / 1000
        elif unit_from == 'Milliliter' and unit_to == 'Gallon':
            return value / 3785.41
        elif unit_from == 'Gallon' and unit_to == 'Liter':
            return value * 3.78541
        elif unit_from == 'Gallon' and unit_to == 'Milliliter':
            return value * 3785.41
    
    # If no conversion was found, return a message
    return f"Conversion from {unit_from} to {unit_to} is not supported"

if st.button('Convert'):
    result = Conversion(Category_Selected, value, unit_from, unit_to)
    st.success(f"Converted Value is {result}")