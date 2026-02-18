import streamlit as st
from cal import *

st.header("Simple Calculator App")
st.write("This is the app for calculator")
#ctrl c to stop the streamlit server
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
operation = st.selectbox("Choose an operation:", ["+", "-", "*", "/", "**", "%", "//"]) 

if st.button("Calculate"):
    if operation == '+':
        st.write(f"Result: {add(num1, num2)}")
    elif operation == '-':
        st.write(f"Result: {subtract(num1, num2)}")
    elif operation == '*':
        st.write(f"Result: {multiply(num1, num2)}")
    elif operation == '/':
        st.write(f"Result: {divide(num1, num2)}")
    elif operation == '**':
        st.write(f"Result: {power(num1, num2)}")
    elif operation == '%':
        st.write(f"Result: {modulus(num1, num2)}")
    elif operation == '//':
        st.write(f"Result: {floor_division(num1, num2)}")
    
   
