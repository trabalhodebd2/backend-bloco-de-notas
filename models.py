from pydantic import BaseModel, Field
from typing import Optional


class AnnotationModel(BaseModel):
    title: str = Field(...)
    content: str = Field(...)


class AnnotationPatchModel(BaseModel):
    title: Optional[str]
    content: Optional[str]
