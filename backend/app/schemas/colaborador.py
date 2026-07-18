from datetime import date
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from app.models.status_colaborador import StatusColaborador

class ColaboradorBase(BaseModel):
    nome: str
    matricula: str
    email: str | None = None
    telefone: str | None = None
    cargo: str
    setor: str
    cidade: str
    data_admissao: date
    status: StatusColaborador = StatusColaborador.ATIVO
    foto_url: str | None = None
    observacoes: str | None = None
    gestor_id: UUID | None = None

class ColaboradorCreate(ColaboradorBase):
    pass

class ColaboradorUpdate(BaseModel):
    nome: str | None = None
    matricula: str | None = None
    email: str | None = None
    telefone: str | None = None
    cargo: str | None = None
    setor: str | None = None
    cidade: str | None = None
    data_admissao: date | None = None
    status: StatusColaborador | None = None
    foto_url: str | None = None
    observacoes: str | None = None
    gestor_id: UUID | None = None

class ColaboradorResponse(ColaboradorBase):
    id: UUID

    model_config = ConfigDict(
        from_attributes=True,
    )