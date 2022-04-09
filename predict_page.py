import streamlit as st
from learn_page import showLearn_page
import webbrowser
import pickle
import numpy as np

def load_model():
    with open('./model/saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

rf_grid = data["model"]



def showPredict_page(): 
    st.title("Diabetes Risk Survey") #Title of Page
    
    #Subheading 
    ####questions: Pregnancies, Glucose,BloodPressure, SkinThickness, BMI, DiabetesPedigreeFunction, Age
    st.write("""### Before we can start, we need some information from you. (If you have any questions regarding the form, visit our Learn About Diabetes page in the top left!)""")
    pregnancies = st.slider("How many pregnancies have you had (if applicable): ", 0, 50)
    BMI = st.number_input("Please enter your BMI to the best of your ability (kg/m^2): ", min_value=1.0, max_value=300.0)
    glucose = st.number_input("What is your fasting blood glucose level (mg/dL): ", min_value=20.0, max_value=300.0)
    blood_pressure = st.number_input("What is your blood pressure (mmHg): ", min_value=20.0, max_value=300.0)
    skin_thickness = st.slider("What is your tricep skin thickness (mm): ", 1, 50)
    glucose_level = st.number_input("How many of your parents had diabetes: ", 0, 2)
    grandparents = st.number_input("How many of your grandparents had diabetes: ", 0, 4)
    age = st.slider("Please enter your age: ", 1, 110)
    # learnMore = st.button("Learn More")
    # if learnMore:
    #     showLearn_page()
        
    #Calculation button 
    pedigree_function = 0.5
    button = st.button("Calculate Risk")
    if button: # under if statement will display results. 
        X = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, BMI, pedigree_function, age]])
        score = rf_grid.predict_proba(X)
        st.subheader("Your estimated risk of diabetes is" + max(score[0][0], score[0][1]))



