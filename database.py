# References:

# https://www.mongodb.com/docs/drivers/pymongo/
# https://pymongo.readthedocs.io/en/stable/tutorial.html

from pymongo import MongoClient
from models import AnnotationModel, AnnotationPatchModel
from fastapi import HTTPException, status

client = MongoClient()

database = client["annotation_app"]
collection = database["annotations"]  # SEE OBS1


last_id_used = 0


def generate_integer_id():
    global last_id_used
    last_id_used += 1
    return last_id_used - 1


def fetch_all():
    return list(collection.find())


def fetch_one(annotation_id: int):
    result = collection.find_one({"_id": annotation_id})
    if result is not None:
        return result
    raise NOT_FOUND_EXCEPTION


def create(annotation: AnnotationModel):
    new_annotation_id = collection.insert_one(
        {"_id": generate_integer_id(), **annotation.dict()}
    ).inserted_id
    result = collection.find_one({"_id": new_annotation_id})
    print(result)
    return result


def update(annotation_id: int, annotation: AnnotationPatchModel):
    result = collection.find_one_and_update(
        {"_id": annotation_id}, {"$set": {**annotation.dict(exclude_unset=True)}}
    )
    if result is not None:
        return fetch_one(annotation_id)
    raise NOT_FOUND_EXCEPTION


def delete(annotation_id: int):
    success_message = {"message": "annotation successfuly deleted"}
    result = collection.find_one_and_delete({"_id": annotation_id})
    if result is not None:
        return success_message
    raise NOT_FOUND_EXCEPTION


NOT_FOUND_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="No annotation with the informed id"
)

# OBS1: collection is the relative as a table in a relational database
