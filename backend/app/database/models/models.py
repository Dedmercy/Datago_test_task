import enum
from datetime import datetime
from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, ForeignKey

from app.database.models.base import Base


class User(Base):
    """
        Account Entity
    """
    __tablename__ = "user_account"

    # Account data
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(256))

    # Personal data
    first_name: Mapped[str] = mapped_column(String(30))
    middle_name: Mapped[Optional[str]] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))

    # Contact info
    email: Mapped[str] = mapped_column(String(50), unique=True)
    phone: Mapped[str] = mapped_column(String(11), unique=True)

    account_transaction: Mapped[List["Transaction"]] = relationship(back_populates='transaction_account')


class TransactionCategory(enum.Enum):
    products = "products"
    restaurants = "restaurants"
    beauty = "beauty"
    electronics = "electronics"
    money_transfers = "Money transfers"


class Transaction(Base):
    __tablename__ = "transaction"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category: Mapped[TransactionCategory]
    money: Mapped[int]
    date: Mapped[datetime]

    account_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    transaction_account: Mapped["User"] = relationship(back_populates='account_transaction')


