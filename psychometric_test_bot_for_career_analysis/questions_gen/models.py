from pydantic import BaseModel, Field


class QuestionParser(BaseModel):
    question: str = Field(description="Question for the user.")
    options: list[str] = Field(
        description="Options from which the user need to choose their answer."
    )


class QuestionParserList(BaseModel):
    questions: list[QuestionParser]


class CareersList(BaseModel):
    careers: list[str] = Field(description="List containing the 3 most suitable careers of the user.")