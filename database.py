# References:

# https://www.mongodb.com/docs/drivers/pymongo/
# https://pymongo.readthedocs.io/en/stable/tutorial.html

from pymongo import MongoClient

client = MongoClient()

database = client["annotation_app"]
collection = database["annotations"]  # SEE OBS1


from models import AnnotationModel


# def fetch_all():

#     ...


# def fetch_one(annotation_id: int):
#     ...


def create(annotation: AnnotationModel):
    new_annotation_id = collection.insert_one({**annotation.dict()}).inserted_id
    return collection.find_one({"_id": new_annotation_id})


# def update(annotation_id: int, annotation: AnnotationModel):
#     ...


# def delete(annotation_id: int):
#     ...


# OBS1: collection is the relative as a table in a relational database
