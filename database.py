from models import AnnotationModel

# MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.AnnotationApp
collection = database.annotation
# collection is the relative as a table in a relational database


def generate_integer_id():
    """
    If the database has no records, it returns 0. Otherwise it returns
    the last record's id number plus 1
    """

    database_sorted_by_id = sorted(database, key=lambda record: record["id"])
    last_id = database_sorted_by_id[-1]["id"] if database_sorted_by_id else None
    return 0 if last_id is None else last_id + 1


def fetch_all():

    annotations = []
    cursor = collection.find({})

    for document in cursor:
        annotations.append(AnnotationModel(**document))  # dictionary unpacking

    return document


def fetch_one(annotation_id: int):
    document = collection.find_one({"id": annotation_id})
    return document


def create(annotation: AnnotationModel):
    annotation.id = generate_integer_id()
    collection.insert_one(annotation)
    return annotation


def update(annotation_id: int, annotation: AnnotationModel):
    title, content = annotation.title, annotation.content
    collection.update_one(
        {"id": annotation_id},
        {"$set": {"title": title, "content": content}},
    )
    return fetch_one(annotation_id)


def delete(annotation_id: int):
    collection.delete_one({"id": annotation_id})
    return True
