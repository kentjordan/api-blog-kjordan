from uuid import UUID


def is_uuid_valid(id: str):

    try:
        validated = UUID(id, version=4)
        return validated
    except ValueError:
        return False
