from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import AnnotationModel
from database import generate_integer_id, fetch_all, fetch_one, create, update, delete


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
def list_annotations():
    response = fetch_all()
    return response


@app.get("/annotations/{annotation_id}", tags=["Annotation Endpoints"])
def retrieve_annotation(annotation_id: int):

    annotation = None

    for record in database:
        if record["id"] == annotation_id:
            annotation = record
            break

    if annotation is None:
        return {"message": "annotation not found"}

    return annotation


@app.post("/annotations", tags=["Annotation Endpoints"])
def create_annotation(annotation_fields: AnnotationModel):

    new_annotation = {
        "id": generate_integer_id(),
        "title": annotation_fields.title,
        "content": annotation_fields.content,
    }
    database.append(new_annotation)
    return new_annotation


@app.put("/annotations/{annotation_id}", tags=["Annotation Endpoints"])
def update_annotation(annotation_id: int, annotation_fields: AnnotationModel):

    # TODO: Fazer com que nao seja obrigatorio informar os 2 campos pra editar

    updated_annotation = None

    for record in database:
        if record["id"] == annotation_id:
            updated_annotation = record
            break

    if updated_annotation is None:
        return {"message": "annotation not found"}

    updated_annotation["title"] = annotation_fields.title
    updated_annotation["content"] = annotation_fields.content

    return updated_annotation


@app.delete("/annotations/{annotation_id}", tags=["Annotation Endpoints"])
def delete_annotation(annotation_id: int):

    annotation = None

    for record in database:
        if record["id"] == annotation_id:
            annotation = record
            break

    if annotation is None:
        return {"message": "annotation not found"}

    database.remove(annotation)
    return {"message": "annotation successfuly deleted"}
