import streamlit as st
from questions_gen.ai_generator import generate_questions, process_response


st.title("Psychometric Test")

submitted: str

question_numbers = [
    "question_one",
    "question_two",
    "question_three",
    "question_four",
    "question_five",
    "question_six",
    "question_seven",
    "question_eight",
    "question_nine",
    "question_ten",
]

user_answers_dict = {
    "question": "",
    "options": "",
    "user_answer": "",
}

session_vars = [
    "questions",
    "question_answers",
    "questions_count",
    "careers",
]

for var in session_vars:
    if var not in st.session_state:
        print("Declaring session states")
        st.session_state[var] = None

if st.session_state["question_answers"] is None:
    st.session_state["question_answers"] = {
        key: user_answers_dict.copy() for key in question_numbers
    }

if st.session_state["questions_count"] is None:
    st.session_state["questions_count"] = 0

with st.status(label="Generating questions"):
    if st.session_state.questions is None:
        questions_json = generate_questions()
        print("Generating questions.")
        st.session_state.questions = questions_json

        count = 0
        for question in st.session_state.questions:
            st.session_state["question_answers"][question_numbers[count]][
                "question"
            ] = question["question"]

            st.session_state["question_answers"][question_numbers[count]]["options"] = (
                question["options"]
            )

            count += 1


with st.form("questions_form"):
    count = 0
    for question in st.session_state.questions:
        st.session_state["question_answers"][question_numbers[count]]["user_answer"] = (
            st.selectbox(
                question["question"],
                options=question["options"],
            )
        )

        count += 1

    submitted = st.form_submit_button(label="Submit")


if submitted:
    st.write("Form submitted")

    with st.status(label="Analyzing your responses..."):
        st.session_state.careers = process_response(st.session_state["question_answers"])

    
    # st.write(st.session_state.careers)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Most suitable career options for you are:")
        
        for career in st.session_state.careers["careers"]:
            career_val = career["career"]
            reason = career["reason"]
            with st.expander(career_val):
                st.write(f"\t* {reason}")
            # st.markdown(f"* {career.get("career")}")
            
            
    with col2:
        st.subheader("Your aptitude parameters(Out of 10):")
        st.write(st.session_state.careers["aptitude_parameters"])
        
