from sqlalchemy.ext.asyncio import AsyncSession

from app.database.repositories.user_repo import UserRepository


class UserService:
    """
        Class with business logic for work with users data.
    """

    def __init__(self):
        self.__repository = UserRepository()

    async def get_current_user(self, auth: dict, session: AsyncSession):
        current_user = await self.__repository.get_by_username(auth['username'], session)

        return current_user.as_dict()
