import uuid
from datetime import date
from sqlalchemy import Date, ForeignKey
from sqlalchemy import Enum as SqlEnum, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.base import TimestampMixin
from app.models.colaborador import Colaborador
from app.models.status_ferias import StatusFerias

class Ferias(TimestampMixin, Base):
    __tablename__ = "ferias"

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

    data_inicio: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    data_fim: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[StatusFerias] = mapped_column(
        SqlEnum(
            StatusFerias,
            name="status_ferias",
        ),
        default=StatusFerias.PENDENTE,
        nullable=False,
    )

    observacoes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    colaborador: Mapped[Colaborador] = relationship()