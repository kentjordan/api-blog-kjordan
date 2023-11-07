from pydantic import BaseModel, UUID4


class CreateBlog(BaseModel):
    title: str
    content: str | None
    images: list[str] | None
    user_id: UUID4
