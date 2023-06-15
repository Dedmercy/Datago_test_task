from datetime import datetime

from pydantic import BaseModel


class TransactionBaseSchema(BaseModel):
    pass


class TransactionCreateSchema(TransactionBaseSchema):
    category: str
    money: int
