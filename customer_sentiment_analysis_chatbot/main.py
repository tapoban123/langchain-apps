import streamlit as st
from gen_ai.sentiment_analysis import get_response

st.title("Customer Sentiment Analysis Chatbot")

user_feedback = "user_feedback"
llm_response = "llm_response"

session_vars = [user_feedback, llm_response]

for var in session_vars:
    if var not in st.session_state:
        st.session_state[var] = None


st.session_state[user_feedback] = st.text_area(
    "Enter user feedback",
    placeholder="e.g: Their staff is not only friendly but also highly skilled.",
)

get_response = st.button(label="Analyze")

if get_response:
    if st.session_state[user_feedback] is not None:
        st.markdown(st.session_state[user_feedback])
