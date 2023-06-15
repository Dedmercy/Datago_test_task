from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.jwt import JWTAuth
from app.schemas.transaction import TransactionCreateSchema
from app.database.connection import PostgresConnection
from app.services.transaction import TransactionService

router = APIRouter(
    prefix="/tracking",
    tags=["Tracking your money"]
)


@router.post('/add', status_code=status.HTTP_201_CREATED)
async def add_transaction(
        schema: TransactionCreateSchema,
        auth: dict = Depends(JWTAuth.verify_access_token),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    result = await TransactionService().add_transaction(auth, schema, session)
    return result


@router.get('/all')
async def get_all_transaction(
        auth: dict = Depends(JWTAuth.verify_access_token),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    result = await TransactionService().get_all_transactions(auth, session)
    return result


@router.post('/category')
async def get_transactions_by_category(
        category: str,
        auth: dict = Depends(JWTAuth.verify_access_token),
        session: AsyncSession = Depends(PostgresConnection.get_db)
):
    result = await TransactionService().get_transactions_by_category(category, auth, session)
    return result
