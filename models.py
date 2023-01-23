from pydantic import BaseModel, Field


class AnnotationModel(BaseModel):
    title: str = Field(...)
    content: str = Field(...)
