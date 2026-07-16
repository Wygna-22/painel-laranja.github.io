from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from database.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True
    )

    cargo: Mapped[str] = mapped_column(String(50))
    google_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )
    foto: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )
    ativo: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )