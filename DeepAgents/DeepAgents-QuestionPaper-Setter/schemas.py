from pydantic import BaseModel, Field
from typing import Literal


class MultipleChoiceQuestion(BaseModel):
    """
    Multiple Choise Question Format
    """

    question: str = Field(description="Question")
    A: str = Field(description="Choice A")
    B: str = Field(description="Choice B")
    C: str = Field(description= "Choice C")
    D: str = Field(description="Choice D")

    answer: Literal["A", "B", "C", "D"] = Field(description="Answer")

    explaination: str = Field(description="Explaination to answer")

class SubAgentReposne(BaseModel):
    """
    SubAgent response format
    """

    mcqs: list[MultipleChoiceQuestion] = Field(
    min_length=1,
    description="List of Multiple Choice Questions"
    )

    topic: str = Field(description="Topic Name")



    