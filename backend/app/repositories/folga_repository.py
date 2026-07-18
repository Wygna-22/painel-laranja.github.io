from uuid import UUID
from sqlalchemy.orm import Session
from app.models.folga import Folga
from app.repositories.base import BaseRepository

class FolgaRepository(BaseRepository[Folga]):
    def __init__(self):
        super().__init__(Folga)

    def get_by_colaborador(
        self,
        db: Session,
        colaborador_id: UUID,
    ) -> list[Folga]:
        return (
            db.query(Folga)
            .filter(Folga.colaborador_id == colaborador_id)
            .all()
        )

folga_repository = FolgaRepository()