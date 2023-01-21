from fastapi import FastAPI

from models import AnnotationModel
from database import database, generate_integer_id


# TODO: Falta so adicionar o Mongo agora e fazer a função de Text Search (ler documentação da atividade)

app = FastAPI()


@app.get("/annotations", tags=["Annotation Endpoints"])
def list_annotations():
    return database


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
