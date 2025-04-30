from langchain.prompts import PromptTemplate
from gen_ai.custom_parsers import json_parser, pydantic_parser, neg_parser, pos_parser

sentiment_analysis_template = PromptTemplate(
    template="Evaluate the sentiment in the {user_feedback} regarding our product.\n{format_instructions}",
    input_variables=["user_feedback"],
    partial_variables={
        "format_instructions": pydantic_parser.get_format_instructions()
    },
)


key_concerns_template = PromptTemplate(
    template="Summarize the key concerns from the {user_feedback}.\n{format_instructions}",
    input_variables=["user_feedback"],
    partial_variables={"format_instructions": json_parser.get_format_instructions()},
)

pos_template = PromptTemplate(
    template="Provide a short and simple message for the positive feedback provided by the user.\n{user_feedback}\n{format_instructions}",
    input_variables=["user_feedback"],
    partial_variables={"format_instructions": pos_parser.get_format_instructions()},
)

neg_template = PromptTemplate(
    template="Provide a short and simple message for the negative feedback provided by the user.\n{user_feedback}",
    input_variables=["user_feedback"],
)

merge_neg_response = PromptTemplate(
    template="Merge the {feedback_response} and {key_concerns} into one single message.\n{format_instructions}",
    input_variables=["feedback_response", "key_concerns"],
    partial_variables={"format_instructions": neg_parser.get_format_instructions()},
)
