import uuid
from datetime import date
from sqlalchemy import Date, ForeignKey
from sqlalchemy import Enum as SqlEnum, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.base import TimestampMixin
from app.models.colaborador import Colaborador
from app.models.status_folga import StatusFolga

class Folga(TimestampMixin, Base):
    __tablename__ = "folgas"

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

    status: Mapped[StatusFolga] = mapped_column(
        SqlEnum(
            StatusFolga,
            name="status_folga",
        ),
        default=StatusFolga.PENDENTE,
        nullable=False,
    )

    motivo: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    observacoes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    colaborador: Mapped[Colaborador] = relationship()