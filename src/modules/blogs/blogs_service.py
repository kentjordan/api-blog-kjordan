from database.pg import connection
from models.blogs import CreateBlog


def create_blog(body: CreateBlog):
    with connection.cursor() as cursor:
        cursor.execute(
            """
                INSERT INTO blogs(title, content, images, user_id) VALUES (%s, %s, %s, %s);
            """,
            (body.title, body.content, body.images, body.user_id))
        connection.commit()

    return {
        "msg": "Blog successfully created."
    }
