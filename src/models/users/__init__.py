from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    country: str
    city: str
