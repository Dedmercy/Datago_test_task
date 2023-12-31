import os

from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv('backend/app/.env')


class Settings(BaseModel):
    """
        Project configuration class.
    """

    # Postgres
    postgres_username: str
    postgres_password: str
    postgres_database: str
    postgres_host: str
    postgres_port: str

    # JWT
    jwt_secret: str
    jwt_algorithm: str
    jwt_durability: str

    class Config:
        frozen = True


def get_config() -> Settings:
    """
        Get a config instance.
    """
    __config_params = {param: os.environ.get(param.upper()) for param in Settings.__fields__}

    return Settings(**__config_params)


settings = get_config()
