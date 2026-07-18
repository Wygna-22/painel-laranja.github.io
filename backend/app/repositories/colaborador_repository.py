from uuid import UUID
from sqlalchemy.orm import Session
from app.models.colaborador import Colaborador
from app.repositories.base import BaseRepository

class ColaboradorRepository(BaseRepository[Colaborador]):

    def __init__(self):
        super().__init__(Colaborador)

    def get_by_matricula(
        self,
        db: Session,
        matricula: str,
    ) -> Colaborador | None:
        return (
            db.query(Colaborador)
            .filter(Colaborador.matricula == matricula)
            .first()
        )

    def get_by_email(
        self,
        db: Session,
        email: str,
    ) -> Colaborador | None:
        return (
            db.query(Colaborador)
            .filter(Colaborador.email == email)
            .first()
        )

    def get_by_gestor(
        self,
        db: Session,
        gestor_id: UUID,
    ) -> list[Colaborador]:
        return (
            db.query(Colaborador)
            .filter(Colaborador.gestor_id == gestor_id)
            .all()
        )

colaborador_repository = ColaboradorRepository()