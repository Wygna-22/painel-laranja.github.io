from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .gestor import Gestor

class User(BaseModel):
    __tablename__ = "users"

    nome: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        String(30),
        default="gestor"
    )

    google_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    gestor: Mapped["Gestor"] = relationship(
        back_populates="user",
        uselist=False
    )