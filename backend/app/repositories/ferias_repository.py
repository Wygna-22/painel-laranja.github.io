from uuid import UUID
from sqlalchemy.orm import Session
from app.models.ferias import Ferias
from app.repositories.base import BaseRepository

class FeriasRepository(BaseRepository[Ferias]):

    def __init__(self):
        super().__init__(Ferias)

    def get_by_colaborador(
        self,
        db: Session,
        colaborador_id: UUID,
    ) -> list[Ferias]:
        return (
            db.query(Ferias)
            .filter(Ferias.colaborador_id == colaborador_id)
            .all()
        )

ferias_repository = FeriasRepository()