from uuid import UUID
from sqlalchemy.orm import Session
from app.models.historico import Historico
from app.repositories.base import BaseRepository

class HistoricoRepository(BaseRepository[Historico]):
    def __init__(self):
        super().__init__(Historico)

    def get_by_colaborador(
        self,
        db: Session,
        colaborador_id: UUID,
    ) -> list[Historico]:
        return (
            db.query(Historico)
            .filter(
                Historico.colaborador_id == colaborador_id
            )
            .order_by(Historico.data.desc())
            .all()
        )

historico_repository = HistoricoRepository()