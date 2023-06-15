from pydantic import BaseModel


class ClaimSchema(BaseModel):
    id: int
    username: str
