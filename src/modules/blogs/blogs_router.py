from fastapi import APIRouter, Body
from models.blogs import CreateBlog
from .blogs_service import create_blog

router = APIRouter(prefix="/blogs")


@router.post("/")
def create(body: CreateBlog):
    return create_blog(body)
