from langchain_core.output_parsers import (
    PydanticOutputParser,
    StrOutputParser,
    JsonOutputParser,
)
from gen_ai.parser_models import FeedbackSentiment, NegFeedbackResponse, PosFeedbackResponse


str_parser = StrOutputParser()
json_parser = JsonOutputParser()
sentiment_parser = PydanticOutputParser(pydantic_object=FeedbackSentiment)
neg_parser = PydanticOutputParser(pydantic_object=NegFeedbackResponse)
pos_parser = PydanticOutputParser(pydantic_object=PosFeedbackResponse)
