import uuid

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .colaborador import Colaborador

class Gestor(BaseModel):
    __tablename__ = "gestores"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    nome: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    setor: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    cargo: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    telefone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    user: Mapped["User"] = relationship(
        back_populates="gestor"
    )

    colaboradores: Mapped[list["Colaborador"]] = relationship(
        back_populates="gestor",
        cascade="all, delete-orphan"
    )