import uuid
from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .colaborador import Colaborador

class Ferias(BaseModel):
    __tablename__ = "ferias"

    colaborador_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("colaboradores.id"),
        nullable=False
    )

    data_inicio: Mapped[date] = mapped_column(Date)

    data_fim: Mapped[date] = mapped_column(Date)

    dias: Mapped[int] = mapped_column(Integer)

    status: Mapped[str] = mapped_column(
        String(30),
        default="PROGRAMADA"
    )

    observacao: Mapped[str | None] = mapped_column(Text)

    colaborador: Mapped["Colaborador"] = relationship(
        back_populates="ferias"
    )