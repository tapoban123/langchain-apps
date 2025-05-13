from enum import Enum
from dotenv import load_dotenv
import os


load_dotenv()


class API_KEYS(Enum):
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
    
class LLM_MODELS(Enum):
    GEMINI_MODEL = "gemini-2.0-flash"