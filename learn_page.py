from re import L
import streamlit as st

def showLearn_page():
    st.title("Learn About Diabetes")
    url = "https://www.cdc.gov/diabetes/basics/diabetes.html"
    st.write("##### To learn more about diabetes, check out this [link](%s)" %url + " from the CDC. ")

    st.title("BMI (Body Mass Indicator)")
    url = "https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html"
    st.write("##### To learn more about your BMI, check out this [link](%s)" %url + " from the CDC. ")

    st.title("How to find Fasting Glucose Level")
    url = "https://www.mayoclinic.org/diseases-conditions/diabetes/diagnosis-treatment/drc-20371451#:~:text=A%20fasting%20blood%20sugar%20level,Oral%20glucose%20tolerance%20test."
    st.write("##### To learn more about your Glucose Level, check out this [link](%s)" %url + " from the Mayo Clinic. ")

    st.title("Blood Pressure")
    url = "https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings"
    st.write("##### To learn more your Blood Pressure, check out this [link](%s)" %url + " from the American Heart Association. ")

    st.title("Tricep Skin Thickness")
    url = "https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/skinfold-thickness"
    st.write("##### To learn more your Skin Thickness, check out this [link](%s)" %url + " from the Science Direct. ")


