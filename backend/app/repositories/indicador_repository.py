from app.models.indicador import Indicador
from app.repositories.base import BaseRepository

class IndicadorRepository(BaseRepository[Indicador]):
    def __init__(self):
        super().__init__(Indicador)

indicador_repository = IndicadorRepository()