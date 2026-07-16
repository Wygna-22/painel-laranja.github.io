import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .colaborador import Colaborador

class Historico(BaseModel):
    __tablename__ = "historico"

    colaborador_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("colaboradores.id"),
        nullable=False
    )

    tipo: Mapped[str] = mapped_column(String(50))

    titulo: Mapped[str] = mapped_column(String(150))

    descricao: Mapped[str] = mapped_column(Text)

    usuario_responsavel: Mapped[str] = mapped_column(String(150))

    data_evento: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    colaborador: Mapped["Colaborador"] = relationship(
        back_populates="historico"
    )