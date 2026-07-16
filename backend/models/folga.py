import uuid
from datetime import date

from sqlalchemy import Date, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .colaborador import Colaborador

class Folga(BaseModel):
    __tablename__ = "folgas"

    colaborador_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("colaboradores.id"),
        nullable=False
    )

    data_folga: Mapped[date] = mapped_column(Date)

    motivo: Mapped[str] = mapped_column(String(150))

    observacao: Mapped[str | None] = mapped_column(Text)

    colaborador: Mapped["Colaborador"] = relationship(
        back_populates="folgas"
    )