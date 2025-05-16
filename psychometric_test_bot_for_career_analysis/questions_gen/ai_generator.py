from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from .models import QuestionParserList, CareersList
from pydantic import BaseModel

from enums import API_KEYS, LLM_MODELS


def get_llm():
    llm = ChatGoogleGenerativeAI(
        google_api_key=API_KEYS.GEMINI_API_KEY.value,
        model=LLM_MODELS.GEMINI_MODEL.value,
        temperature=0.5,
    )

    return llm


def generate_questions():
    llm = get_llm()
    pydantic_parser = PydanticOutputParser(pydantic_object=QuestionParserList)

    template = PromptTemplate(
        template="Generate 10 psychometric test questions designed to evaluate a user's personality, interests, and cognitive strengths. The questions should help in identifying the most suitable career paths for the user based on their responses. Avoid technical jargon and keep the questions simple, relatable, and diverse in focus (e.g., logical thinking, creativity, social preference, risk tolerance, etc.).\n{format_instructions}",
        partial_variables={
            "format_instructions": pydantic_parser.get_format_instructions()
        },
    )

    chain = template | llm | pydantic_parser

    result: BaseModel = chain.invoke({})

    # print(result.model_dump()["questions"])
    return result.model_dump()["questions"]


def process_response(user_response: dict):
    llm = get_llm()

    career_parser = PydanticOutputParser(pydantic_object=CareersList)

    template = """
    You are a career guidance expert. You will be given a dictionary where each entry contains:
    1. A question related to the user's personality or interests,
    2. A list of options the user could choose from,
    3. The user's selected answer.
    
    Analyze the user's responses to score their aptitude across the following key areas (score out of 10 for each):

    1. Logical Reasoning
    2. Numerical Ability
    3. Verbal Ability
    4. Abstract/Spatial Reasoning
    5. Mechanical Reasoning
    6. Creativity
    7. Attention to Detail
    8. Personality & Interests Alignment
    After scoring, suggest 3 most suitable career paths for the user based on their overall aptitude and psychometric profile. Include a short reason for each career choice. Make sure your response is personalized, insightful, and easy to understand.
    Here is the dictionary:\n{user_answers}\n{format_instructions}
    """

    prompt_template = PromptTemplate(
        template=template,
        input_variables=["user_answers"],
        partial_variables={
            "format_instructions": career_parser.get_format_instructions()
        },
    )

    chain = prompt_template | llm | career_parser

    result: BaseModel = chain.invoke({"user_answers": user_response})

    return result.model_dump()


# generate_questions()
