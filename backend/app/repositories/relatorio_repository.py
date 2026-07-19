from sqlalchemy.orm import Session
from app.models.colaborador import Colaborador
from app.repositories.base import BaseRepository

class RelatorioRepository(BaseRepository[Colaborador]):

    def __init__(self):
        super().__init__(Colaborador)

    def listar_colaboradores(
        self,
        db: Session,
    ) -> list[Colaborador]:

        return (
            db.query(Colaborador)
            .order_by(Colaborador.nome)
            .all()
        )

relatorio_repository = RelatorioRepository()