from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

from enums import API_KEYS, LLM_MODELS

llm = ChatGoogleGenerativeAI(
    google_api_key=API_KEYS.GEMINI_API_KEY.value,
    model=LLM_MODELS.GEMINI_MODEL.value,
    temperature=0.5,
)


class QuestionParser(BaseModel):
    question: str = Field(description="Question for the user.")
    options: list[str] = Field(
        description="Options from which the user need to choose their answer."
    )


class QuestionParserList(BaseModel):
    questions: list[QuestionParser]


pydantic_parser = PydanticOutputParser(pydantic_object=QuestionParserList)

template = PromptTemplate(
    template="Generate 10 psychometric questions from which the most suitable careers for the user can be decided.\n{format_instructions}",
    partial_variables={
        "format_instructions": pydantic_parser.get_format_instructions()
    },
)

prompt = template.invoke({})

result = llm.invoke(prompt)

print(result.content)
