from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.historico import Historico
from app.repositories.historico_repository import historico_repository
from app.schemas.historico import (
    HistoricoCreate,
    HistoricoUpdate,
)

class HistoricoService:
    def create(
        self,
        db: Session,
        data: HistoricoCreate,
    ) -> Historico:

        novo_historico = Historico(
            **data.model_dump()
        )

        return historico_repository.create(
            db,
            novo_historico,
        )

    def get(
        self,
        db: Session,
        historico_id: UUID,
    ) -> Historico:

        historico = historico_repository.get(
            db,
            historico_id,
        )

        if not historico:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Histórico não encontrado.",
            )

        return historico

    def list_all(
        self,
        db: Session,
    ) -> list[Historico]:
        return historico_repository.get_all(db)

    def list_by_colaborador(
        self,
        db: Session,
        colaborador_id: UUID,
    ) -> list[Historico]:
        return historico_repository.get_by_colaborador(
            db,
            colaborador_id,
        )

    def update(
        self,
        db: Session,
        historico_id: UUID,
        data: HistoricoUpdate,
    ) -> Historico:

        historico = self.get(
            db,
            historico_id,
        )

        return historico_repository.update(
            db,
            historico,
            data.model_dump(exclude_unset=True),
        )

    def delete(
        self,
        db: Session,
        historico_id: UUID,
    ) -> None:

        historico = self.get(
            db,
            historico_id,
        )

        historico_repository.delete(
            db,
            historico,
        )


historico_service = HistoricoService()