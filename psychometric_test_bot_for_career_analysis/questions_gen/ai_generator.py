from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from .models import QuestionParserList
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


# generate_questions()
