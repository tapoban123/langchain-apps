from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser

from enums import API_KEYS, LLM_MODELS

llm = ChatGoogleGenerativeAI(
    google_api_key=API_KEYS.GEMINI_API_KEY.value,
    model=LLM_MODELS.GEMINI_MODEL.value,
    temperature=0.5,
)

result = llm.invoke("Why is the sky blue?")

print(result.content)
