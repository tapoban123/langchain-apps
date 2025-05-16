from pydantic import BaseModel, Field


class QuestionParser(BaseModel):
    question: str = Field(description="Question for the user.")
    options: list[str] = Field(
        description="Options from which the user need to choose their answer."
    )


class QuestionParserList(BaseModel):
    questions: list[QuestionParser]


class CareerInfo(BaseModel):
    career: str = Field(description="Suitable career of the user.")
    reason: str = Field(
        description="Reason of why this career is suitable for the user."
    )


class AptitudeParameters(BaseModel):
    logical_reasoning: int = Field(description="Score of logical_reasoning out of 10.")
    numerical_ability: int = Field(description="Score of numerical_ability out of 10.")
    verbal_ability: int = Field(description="Score of verbal_ability out of 10.")
    abstract_or_spatial_reasoning: int = Field(
        description="Score of abstract_or_spatial_reasoning out of 10."
    )
    mechanical_reasoning: int = Field(
        description="Score of mechanical_reasoning out of 10."
    )
    creativity: int = Field(description="Score of creativity out of 10.")
    attention_to_detail: int = Field(
        description="Score of attention_to_detail out of 10."
    )
    personality_and_interests_alignment: int = Field(
        description="Score of personality_and_interests_alignment out of 10."
    )


class CareersList(BaseModel):
    careers: list[CareerInfo] = Field(
        description="List containing the 3 most suitable careers of the user."
    )
    aptitude_parameters: AptitudeParameters = Field(description="Dictionary of aptitude parameters scored out of 10.")
