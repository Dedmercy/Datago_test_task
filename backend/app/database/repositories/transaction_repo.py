from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete

from app.database.repositories.base_repo import BaseRepo
from app.database.models.models import Transaction


class TransactionRepository(BaseRepo):
    """
        Repository for working with transaction table in database
    """

    def __init__(self):
        self.model = Transaction

    async def create(self, data: dict, session: AsyncSession):
        query = insert(self.model).values(**data).returning(self.model)
        result = await session.execute(query)
        return result.scalars().one()

    async def get_all(self, session: AsyncSession):
        query = select(self.model).order_by(self.model.id)
        result = await session.execute(query)
        return result.scalars().all()

    async def get_by_id(self, *args, **kwargs):
        pass

    async def get_by_account_id(self, account_id: int, session: AsyncSession):
        query = select(self.model).where(
            self.model.account_id == account_id
        ).order_by(self.model.id)
        result = await session.execute(query)
        return result.scalars().all()

    async def get_by_account_and_category(self, account_id: int, category: str, session: AsyncSession):
        query = select(self.model).where(
            self.model.account_id == account_id,
            self.model.category == category
        ).order_by(self.model.id)
        result = await session.execute(query)
        return result.scalars().all()

    async def update(self, *args, **kwargs):
        pass

    async def remove(self, *args, **kwargs):
        pass
