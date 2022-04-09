import streamlit as st
from learn_page import showLearn_page
from predict_page import showPredict_page

webpage = st.sidebar.selectbox("Diabetes", ("Learn", "Risk Calculator"))
if webpage == "Risk Calculator":
    showPredict_page()
elif webpage == "Learn":
    showLearn_page()

