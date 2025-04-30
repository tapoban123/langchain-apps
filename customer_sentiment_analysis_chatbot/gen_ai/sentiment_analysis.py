from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableBranch, RunnableLambda, RunnableParallel
from .my_enums import API_KEYS, LLM_MODELS
from gen_ai.custom_prompt_templates import (
    key_concerns_template,
    merge_neg_response,
    neg_template,
    pos_template,
    sentiment_analysis_template,
)
from gen_ai.custom_parsers import (
    pos_parser,
    json_parser,
    neg_parser,
    sentiment_parser,
    str_parser,
)


llm = ChatGoogleGenerativeAI(
    api_key=API_KEYS.GEMINI_API_KEY.value,
    model=LLM_MODELS.GEMINI_MODEL.value,
    temperature=0,
    max_retries=3,
)


# Chain to analyse feedback sentiment ->
sentiment_analysis_chain = sentiment_analysis_template | llm | sentiment_parser

pos_chain = pos_template | llm | pos_parser

neg_chain = RunnableParallel(
    {
        "feedback_response": neg_template | llm | str_parser,
        "key_concerns": key_concerns_template | llm | json_parser,
    }
)


branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", pos_chain),
    (
        lambda x: x.sentiment == "negative",
        neg_chain | merge_neg_response | llm | neg_parser,
    ),
    # default branch
    RunnableLambda(lambda x: x.sentiment == "Cannot find sentiment"),
)


final_chain = sentiment_analysis_chain | branch_chain

# sample_neg_feedback = "Got my meal pal today. It was a falafel salad. The falafel was dry and small, and it was just a bunch of dry lettuce. I couldn't eat it."

# sample_pos_feedback = "Pricing is fair and transparent - definitely value for money"


def get_response(feedback: str):
    result = final_chain.invoke({"user_feedback": feedback})
    return result.model_dump()


# print(get_response(sample_pos_feedback))
