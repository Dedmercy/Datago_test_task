from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder

from app.database.repositories.transaction_repo import TransactionRepository
from app.schemas.transaction import TransactionCreateSchema
from app.database.models.models import TransactionCategory


class TransactionService:
    """
        Class with business logic for work with user`s transactions data.
    """

    __transaction_repo: TransactionRepository

    def __init__(self):
        self.__transaction_repo = TransactionRepository()

    async def add_transaction(self, auth: dict, schema: TransactionCreateSchema, session: AsyncSession):
        data = jsonable_encoder(schema)

        if data['category'] not in [member.value for member in TransactionCategory]:
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Wrong category"
            )

        data['date'] = datetime.now()
        data['account_id'] = auth['id']

        try:
            result = await self.__transaction_repo.create(data, session)
            await session.commit()
        except Exception:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Somethings goes wrong'
            )

        return result.as_dict()

    async def get_all_transactions(self, auth: dict, session: AsyncSession):
        result = await self.__transaction_repo.get_by_account_id(auth['id'], session)
        if not result:
            return {'message': 'You did`t record any money transactions'}
        return [transaction.as_dict() for transaction in result]

    async def get_transactions_by_category(self, category: str, auth:dict, session: AsyncSession):
        if category not in [member.value for member in TransactionCategory]:
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Wrong category"
            )

        result = await self.__transaction_repo.get_by_account_and_category(auth['id'], category, session)

        if not result:
            return {'message': 'You did`t record any money transactions with this category'}

        return [transaction.as_dict() for transaction in result]
