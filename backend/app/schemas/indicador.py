from uuid import UUID
from pydantic import BaseModel, ConfigDict

class IndicadorBase(BaseModel):
    user_id: UUID
    mes: int
    ano: int
    qtd_pessoas: int
    dias_atual: float
    dias_mes: float
    pontos: float
    ppc: float
    meta_ppc: float
    falta_meta_dia: float
    meta_mes: float
    esperado_atual: float
    falta_meta_mes: float

class IndicadorCreate(IndicadorBase):
    pass

class IndicadorUpdate(BaseModel):
    user_id: UUID | None = None
    mes: int | None = None
    ano: int | None = None
    qtd_pessoas: int | None = None
    dias_atual: float | None = None
    dias_mes: float | None = None
    pontos: float | None = None
    ppc: float | None = None
    meta_ppc: float | None = None
    falta_meta_dia: float | None = None
    meta_mes: float | None = None
    esperado_atual: float | None = None
    falta_meta_mes: float | None = None

class IndicadorResponse(IndicadorBase):
    id: UUID
    model_config = ConfigDict(
        from_attributes=True,
    )