from pydantic import BaseModel, Field


class QuestionParser(BaseModel):
    question: str = Field(description="Question for the user.")
    options: list[str] = Field(
        description="Options from which the user need to choose their answer."
    )


class QuestionParserList(BaseModel):
    questions: list[QuestionParser]
