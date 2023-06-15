from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData, TIMESTAMP


class Base(AsyncAttrs, DeclarativeBase):
    metadata = MetaData()

    type_annotation_map = {
        datetime: TIMESTAMP(timezone=True),
    }

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
