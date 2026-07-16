import uuid
from datetime import date

from sqlalchemy import Date, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .gestor import Gestor
    from .ferias import Ferias
    from .folga import Folga
    from .historico import Historico

class Colaborador(BaseModel):
    __tablename__ = "colaboradores"

    gestor_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("gestores.id"),
        nullable=False
    )

    nome: Mapped[str] = mapped_column(String(150), nullable=False)

    matricula: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    telefone: Mapped[str | None] = mapped_column(String(20))

    cidade: Mapped[str] = mapped_column(String(100))

    estado: Mapped[str] = mapped_column(String(2))

    locacao: Mapped[str] = mapped_column(String(100))

    placa_veiculo: Mapped[str | None] = mapped_column(String(10))

    dia_cmc: Mapped[date | None] = mapped_column(Date)

    data_admissao: Mapped[date] = mapped_column(Date)

    data_demissao: Mapped[date | None] = mapped_column(Date)

    observacao: Mapped[str | None] = mapped_column(Text)

    status: Mapped[str] = mapped_column(
        String(30),
        default="ATIVO"
    )

    gestor: Mapped["Gestor"] = relationship(
        back_populates="colaboradores"
    )

    ferias: Mapped[list["Ferias"]] = relationship(
        back_populates="colaborador",
        cascade="all, delete-orphan"
    )

    folgas: Mapped[list["Folga"]] = relationship(
        back_populates="colaborador",
        cascade="all, delete-orphan"
    )

    historico: Mapped[list["Historico"]] = relationship(
        back_populates="colaborador",
        cascade="all, delete-orphan"
    )