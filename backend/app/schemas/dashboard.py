from pydantic import BaseModel

class SetorQuantidade(BaseModel):
    setor: str
    quantidade: int

class CidadeQuantidade(BaseModel):
    cidade: str
    quantidade: int

class DashboardResponse(BaseModel):
    total_colaboradores: int
    ativos: int
    afastados: int
    desligados: int
    admissoes_mes: int

    por_setor: list[SetorQuantidade]
    por_cidade: list[CidadeQuantidade]