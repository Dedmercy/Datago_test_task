from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, delete, update

from app.database.repositories.base_repo import BaseRepo
from app.database.models.models import User


class UserRepository(BaseRepo):
    """
        Repository for working with User table in database
    """

    def __init__(self):
        self.model = User

    async def create(self, new_data: dict, session: AsyncSession) -> User:
        query = insert(self.model).values(**new_data).returning(self.model)
        result = await session.execute(query)
        return result.scalars().first()

    async def get_all(self, session: AsyncSession) -> Sequence[User]:
        query = select(self.model).order_by(self.model.id)
        result = await session.execute(query)
        return result.scalars().all()

    async def get_by_username(self, username: str, session: AsyncSession) -> Optional[User]:
        query = select(self.model).where(
            self.model.username == username
        )
        result = await session.execute(query)
        return result.scalars().one_or_none()

    async def get_by_email(self, email: str, session: AsyncSession) -> Optional[User]:
        query = select(self.model).where(
            self.model.email == email
        )
        result = await session.execute(query)
        return result.scalars().one_or_none()

    async def get_by_id(self, id_: int, session: AsyncSession) -> Optional[User]:
        query = select(self.model).where(
            self.model.id == id_
        )
        result = await session.execute(query)
        return result.scalars().one_or_none()

    async def remove(self, id_: int, session: AsyncSession) -> Optional[User]:
        query = delete(self.model).where(
            self.model.id == id_
        ).returning(self.model)
        result = await session.execute(query)
        return result.scalars().one_or_none()

    async def update(self, id_: int, updated_data: dict, session: AsyncSession) -> Optional[User]:
        query = update(self.model).where(
            self.model.id == id_
        ).values(**updated_data).returning(self.model)
        result = await session.execute(query)
        return result.scalars().one_or_none()

