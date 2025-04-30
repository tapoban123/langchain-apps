from pydantic import BaseModel, Field
from typing import Literal


class FeedbackSentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Sentiment of the feedback provided by the user."
    )
    user_feedback: str = Field(description="The actual feedback provided by the user.")


class FinalResponse(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Sentiment of the feedback provided by the user."
    )
    feedback_response: str = Field(description="The message for the user.")


class PosFeedbackResponse(FinalResponse):
    pass


class NegFeedbackResponse(FinalResponse):
    key_concerns: list[str] = Field(description="List of key concerns")
