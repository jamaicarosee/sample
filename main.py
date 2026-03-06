import streamlit as st

st.title("My First Streamlit App")

st.write("Simple Addition Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

if st.button("Add"):
    result = num1 + num2
    st.success(f"Result: {result}")