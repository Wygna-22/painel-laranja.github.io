from datetime import date
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from app.models.tipo_historico import TipoHistorico

class HistoricoBase(BaseModel):
    colaborador_id: UUID
    data: date
    tipo: TipoHistorico
    titulo: str
    descricao: str | None = None

class HistoricoCreate(HistoricoBase):
    pass

class HistoricoUpdate(BaseModel):
    data: date | None = None
    tipo: TipoHistorico | None = None
    titulo: str | None = None
    descricao: str | None = None

class HistoricoResponse(HistoricoBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)