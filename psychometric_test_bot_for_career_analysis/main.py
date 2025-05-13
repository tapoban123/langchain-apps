import streamlit as st


st.title("Psychometric Test")

submitted: str

with st.form("questions_form"):
    st.selectbox("What is the color of sky?", options=["Blue", "Black"])

    submitted = st.form_submit_button(label="Submit")
    
    
if submitted:
    st.write("Form submitted")
