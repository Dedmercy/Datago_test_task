from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.repositories.user_repo import UserRepository
from app.schemas.user import UserCreateSchema
from app.schemas.auth import ClaimSchema
from app.auth.hasher import Hasher
from app.auth.jwt import JWTAuth


class AuthService:
    """
        Class with business logic for authorisation users.
    """
    __user_repo: UserRepository
    __hasher: Hasher

    def __init__(self):
        self.__user_repo = UserRepository()
        self.__hasher = Hasher()

    async def registration(self, create_schema: UserCreateSchema, session: AsyncSession):
        """
            Registration a new user in our application.
        """
        schema_data: dict = jsonable_encoder(create_schema)

        # check uniqueness of username
        account_by_id = await self.__user_repo.get_by_username(schema_data['username'], session)

        if account_by_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Account with this username already exists'
            )

        # check uniqueness of email
        account_by_email = await self.__user_repo.get_by_email(schema_data['email'], session)

        if account_by_email:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Account with this email already exists'
            )

        # Get hashed password
        password = schema_data.pop('password')
        schema_data['hashed_password'] = Hasher.get_hashed_password(password)

        try:
            result = await self.__user_repo.create(schema_data, session)
            await session.commit()
        except Exception as e:
            await session.rollback()
            print(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Something goes wrong'
            )

        return result.as_dict()

    async def login(self, schema: OAuth2PasswordRequestForm, session: AsyncSession):
        """
            Authentication of an already existing user
        """
        account = await self.__user_repo.get_by_username(schema.username, session)

        if not account:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Account with this username not exists'
            )

        if self.__hasher.verify_password(schema.password, account.hashed_password):
            claims_data = ClaimSchema(
                id=account.id,
                username=account.username,
            )

            token = JWTAuth.create_access_token(claims_data)

            return {
                'access_token': token,
                'token_Type': 'bearer'
            }

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Wrong password'
        )
