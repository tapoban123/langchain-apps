import streamlit as st
from questions_gen.ai_generator import generate_questions


st.title("Psychometric Test")

submitted: str

question_one = {
    "question": "",
    "options": "",
    "user_answer": "",
}


if "questions" not in st.session_state:
    st.session_state.questions = []


with st.status(label="Generating questions"):
    if len(st.session_state.questions) == 0:
        questions_json = generate_questions()
        print(questions_json)
        st.session_state.questions = questions_json

with st.form("questions_form"):
    for question in st.session_state.questions:
        st.selectbox(question["question"], options=question["options"])

    submitted = st.form_submit_button(label="Submit")


if submitted:
    st.write("Form submitted")
