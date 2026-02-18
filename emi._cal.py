import streamlit as st
st.header("EMI calculator app")
st.write("This is the app for EMI calculator")

principal=st.number_input("enter principal amoount:")
interest=st.number_input('enter interest rate:')
tenure=st.number_input("enter tenure in years:")
if st.button("EMI"):
    i=principal*tenure*interest/100
    st.write(i)
    st.write("calculated")

    