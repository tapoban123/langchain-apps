import streamlit as st
from gen_ai.sentiment_analysis import generate_content

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
    key="feedback",
)


get_response = st.button(label="Analyze")

if get_response:
    if st.session_state[user_feedback] is not None:
        response = generate_content(st.session_state[user_feedback])
        st.markdown("### User Feedback:")
        st.write(st.session_state[user_feedback])
        st.session_state[user_feedback] = ""

        st.divider()

        if response.get("sentiment") == "positive":
            st.markdown(f"### Message")
            st.markdown(response.get("feedback_response"))

        else:
            st.markdown(f"### Message for the user:")
            st.markdown(response.get("feedback_response"))

            st.divider()

            st.markdown(f"\n\n### Key Concerns:")

            concern_count = 1
            for concern in response.get("key_concerns"):
                st.markdown(f"{concern_count}. {concern}")
                concern_count += 1
