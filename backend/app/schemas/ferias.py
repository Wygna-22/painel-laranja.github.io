from datetime import date
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from app.models.status_ferias import StatusFerias

class FeriasBase(BaseModel):
    colaborador_id: UUID
    data_inicio: date
    data_fim: date
    status: StatusFerias = StatusFerias.PENDENTE
    observacoes: str | None = None

class FeriasCreate(FeriasBase):
    pass

class FeriasUpdate(BaseModel):
    colaborador_id: UUID | None = None
    data_inicio: date | None = None
    data_fim: date | None = None
    status: StatusFerias | None = None
    observacoes: str | None = None

class FeriasResponse(FeriasBase):
    id: UUID

    model_config = ConfigDict(
        from_attributes=True,
    )