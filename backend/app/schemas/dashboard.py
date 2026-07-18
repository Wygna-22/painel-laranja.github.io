from pydantic import BaseModel

class DashboardResponse(BaseModel):
    total_colaboradores: int
    ativos: int
    afastados: int
    desligados: int
    admissoes_mes: int