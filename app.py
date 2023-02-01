from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from typing import Optional

from models import AnnotationModel, AnnotationPatchModel
from database import fetch_all, fetch_one, create, update, delete


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/annotations", tags=["Annotation Endpoints"])
def list_annotations(query: Optional[str] = None):
    response = fetch_all(query)
    return response


@app.get("/annotations/{annotation_id}", tags=["Annotation Endpoints"])
def retrieve_annotation(annotation_id: int):
    return fetch_one(annotation_id)


@app.post(
    "/annotations", tags=["Annotation Endpoints"], status_code=status.HTTP_201_CREATED
)
def create_annotation(annotation: AnnotationModel):
    return create(annotation)


@app.patch("/annotations/{annotation_id}", tags=["Annotation Endpoints"])
def update_annotation(annotation_id: int, annotation_fields: AnnotationPatchModel):
    return update(annotation_id, annotation_fields)


@app.delete("/annotations/{annotation_id}", tags=["Annotation Endpoints"])
def delete_annotation(annotation_id: int):
    return delete(annotation_id)
