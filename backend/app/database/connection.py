from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)

from app.config import settings

DATABASE_URL = f'postgresql+asyncpg://{settings.postgres_username}:' \
               f'{settings.postgres_password}@{settings.postgres_host}:' \
               f'{settings.postgres_port}/{settings.postgres_database}'


class PostgresConnection:
    """
        PostgreSQL`s connection class
    """
    engine = create_async_engine(DATABASE_URL)
    local_session = async_sessionmaker(engine, expire_on_commit=False)

    @classmethod
    async def get_db(cls):
        async with cls.local_session() as session:
            yield session

        # session: AsyncSession = cls.local_session()
        #
        # try:
        #     await yield session
        #     await session.commit()
        # except Exception:
        #     await session.rollback()
        # finally:
        #     await session.close()

