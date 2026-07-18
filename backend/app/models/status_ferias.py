from enum import Enum

class StatusFerias(str, Enum):
    PENDENTE = "PENDENTE"
    APROVADA = "APROVADA"
    REJEITADA = "REJEITADA"
    CONCLUIDA = "CONCLUIDA"