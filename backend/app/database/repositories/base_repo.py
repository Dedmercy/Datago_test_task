from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from app.database.models.base import Base

PostgresModel = TypeVar("PostgresModel", bound=Base)


class BaseRepo(ABC):
    """
        Abstract class for work with database
    """
    model: Generic[PostgresModel]

    @abstractmethod
    async def create(self, *args, **kwargs):
        raise NotImplemented

    @abstractmethod
    async def get_all(self, *args, **kwargs):
        raise NotImplemented

    @abstractmethod
    async def get_by_id(self, *args, **kwargs):
        raise NotImplemented

    @abstractmethod
    async def update(self, *args, **kwargs):
        raise NotImplemented

    @abstractmethod
    async def remove(self, *args, **kwargs):
        raise NotImplemented
