from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    pass


class UserCreateSchema(UserBaseSchema):
    username: str
    password: str

    first_name: str
    middle_name: Optional[str]
    last_name: str

    email: EmailStr
    phone: str


class AccountSchema(UserBaseSchema):
    id: int
    ...


class UserResponseSchema(UserBaseSchema):
    id: str
    username: str
    first_name: str
    middle_name: Optional[str]
    last_name: str

    email: str
    phone: str
