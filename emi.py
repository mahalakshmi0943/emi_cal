# emi calculator applicaton
import streamlit as st

st.header("EMI Calculator App")
st.write("This is the app for EMI calculator")
#ctrl c to stop the streamlit server
principal = st.number_input("Enter the principal amount:")
rate_of_interest = st.number_input("Enter the rate of interest (in %):")
tenure = st.number_input("Enter the tenure (in years):")
if st.button("Calculate EMI"):
    monthly_interest_rate = rate_of_interest / (12 * 100)
    number_of_months = tenure * 12
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_months) / ((1 + monthly_interest_rate) ** number_of_months - 1)
    st.write(f"Your EMI is: {emi:.2f}")
