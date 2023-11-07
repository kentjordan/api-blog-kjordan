from database.pg import connection
from models.users import CreateUser


def create_user(body: CreateUser):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO users(email, password, first_name, last_name, country, city)
            VALUES (%s, %s, %s, %s, %s, %s);
            """, (body.email, body.password,
                  body.first_name, body.last_name,
                  body.country, body.city))
        connection.commit()

    return {
        "msg": "User successfully created."
    }


def delete_user_by_id(id: str):
    if id:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id = %s::UUID;",
                           (id,))
            connection.commit()
        return {
            "msg": "User successfully deleted."
        }
    return {
        "msg": "Invalid type of provided ID"
    }
