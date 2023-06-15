from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.user import UserService
from app.schemas.user import UserResponseSchema
from app.database.connection import PostgresConnection
from app.auth.jwt import JWTAuth

router = APIRouter(
    prefix='/account',
    tags=["Account"]
)


@router.get('/me', response_model=UserResponseSchema)
async def get_all_accounts(
        session: AsyncSession = Depends(PostgresConnection.get_db),
        auth: dict = Depends(JWTAuth.verify_access_token)
):
    result = await UserService().get_current_user(auth, session)
    return result
