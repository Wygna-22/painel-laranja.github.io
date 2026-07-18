from datetime import date
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from app.models.status_folga import StatusFolga

class FolgaBase(BaseModel):
    colaborador_id: UUID
    data: date
    status: StatusFolga = StatusFolga.PENDENTE
    motivo: str
    observacoes: str | None = None

class FolgaCreate(FolgaBase):
    pass

class FolgaUpdate(BaseModel):
    data: date | None = None
    status: StatusFolga | None = None
    motivo: str | None = None
    observacoes: str | None = None

class FolgaResponse(FolgaBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)