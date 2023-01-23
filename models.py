from pydantic import BaseModel, Field


class AnnotationModel(BaseModel):
    title: str = Field(...)
    content: str = Field(...)


if __name__ == "__main__":
    a = AnnotationModel(title="Teste", content="Teste")
    a["id"] = 1
    print(a)
