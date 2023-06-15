from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import PostgresConnection
from app.schemas.user import UserCreateSchema, UserResponseSchema
from app.services.auth import AuthService

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@router.post("/registration", status_code=status.HTTP_201_CREATED, response_model=UserResponseSchema)
async def registration(schema: UserCreateSchema, session: AsyncSession = Depends(PostgresConnection.get_db)):
    result = await AuthService().registration(schema, session)
    return result


@router.post("/login")
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    result = await AuthService().login(form_data, session)
    return result
