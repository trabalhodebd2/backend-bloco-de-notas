# database = []

database = [
    {
        "id": 0,
        "title": "Anotação4 editado hehehe ta ligado",
        "content": "Uma anotação foda",
    },
    {
        "id": 1,
        "title": "Anotação4 editado hehehe ta ligado",
        "content": "Uma anotação foda",
    },
]


def generate_integer_id():
    """
    If the database has no records, it returns 0. Otherwise it returns
    the last record's id number plus 1
    """

    database_sorted_by_id = sorted(database, key=lambda record: record["id"])
    last_id = database_sorted_by_id[-1]["id"] if database_sorted_by_id else None
    return 0 if last_id is None else last_id + 1
