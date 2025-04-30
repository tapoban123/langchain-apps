from langchain.prompts import PromptTemplate
from .custom_parsers import *

sentiment_analysis_template = PromptTemplate(
    template="Evaluate the sentiment in the {user_feedback} regarding our product.\n{format_instructions}",
    input_variables=["user_feedback"],
    partial_variables={
        "format_instructions": sentiment_parser.get_format_instructions()
    },
)


key_concerns_template = PromptTemplate(
    template="Summarize the key concerns from the {user_feedback}.\n{format_instructions}",
    input_variables=["user_feedback"],
    partial_variables={"format_instructions": json_parser.get_format_instructions()},
)

pos_template = PromptTemplate(
    template="""Provide a short and simple message for the positive feedback provided by the user.\n{user_feedback}
    Examples:
    Case: Compliments on products or services
    Response: “Thank you for your wonderful feedback on [product/service]! We're so glad it met your expectations and hope to welcome you back for more!”
    \n{format_instructions}""",
    input_variables=["user_feedback"],
    partial_variables={"format_instructions": pos_parser.get_format_instructions()},
)

neg_template = PromptTemplate(
    template="""Provide a short and simple message for the negative feedback provided by the user.
    Examples:
    Review: "I went to buy a specific product at this store, but they were out of stock. I'm disappointed that they don't keep their inventory up-to-date."

    Response: "Dear customer, I apologize for the inconvenience of us being out of stock of the product you were looking for. We do our best to keep our inventory up-to-date, but sometimes we experience unexpected demand or supply chain disruptions. I've shared your feedback with our inventory management team, and they will be looking for ways to improve our forecasting accuracy."
    
    Review: "I was shocked at how expensive the prices were at this store. I feel like I was overcharged for what I bought."

    Response: "Dear customer, I understand your concern. We strive to offer fair and competitive pricing, but we also recognize that everyone has different budgets. If you'd like to discuss your purchase in more detail, please feel free to contact me directly. I may be able to offer you a discount or refund."
    \n{user_feedback}""",
    input_variables=["user_feedback"],
)

merge_neg_response = PromptTemplate(
    template="Merge the {feedback_response} and {key_concerns} into one single message.\n{format_instructions}",
    input_variables=["feedback_response", "key_concerns"],
    partial_variables={"format_instructions": neg_parser.get_format_instructions()},
)
