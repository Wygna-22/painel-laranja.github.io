import uuid
from datetime import date
from sqlalchemy import Date, ForeignKey
from sqlalchemy import Enum as SqlEnum, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.base import TimestampMixin
from app.models.colaborador import Colaborador
from app.models.tipo_historico import TipoHistorico

class Historico(TimestampMixin, Base):
    __tablename__ = "historicos"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    colaborador_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("colaboradores.id"),
        nullable=False,
    )

    data: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    tipo: Mapped[TipoHistorico] = mapped_column(
        SqlEnum(
            TipoHistorico,
            name="tipo_historico",
        ),
        nullable=False,
    )

    titulo: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    descricao: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    colaborador: Mapped[Colaborador] = relationship()