from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.indicador import Indicador
from app.repositories.indicador_repository import indicador_repository
from app.schemas.indicador import (
    IndicadorCreate,
    IndicadorUpdate,
)


class IndicadorService:

    def create(
        self,
        db: Session,
        indicador: IndicadorCreate,
    ) -> Indicador:

        novo_indicador = Indicador(
            **indicador.model_dump()
        )

        return indicador_repository.create(
            db,
            novo_indicador,
        )

    def get(
        self,
        db: Session,
        indicador_id: UUID,
    ) -> Indicador:

        indicador = indicador_repository.get(
            db,
            indicador_id,
        )

        if not indicador:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Indicador não encontrado.",
            )

        return indicador

    def list_all(
        self,
        db: Session,
    ) -> list[Indicador]:

        return indicador_repository.get_all(db)

    def update(
        self,
        db: Session,
        indicador_id: UUID,
        data: IndicadorUpdate,
    ) -> Indicador:

        indicador = self.get(
            db,
            indicador_id,
        )

        return indicador_repository.update(
            db,
            indicador,
            data.model_dump(exclude_unset=True),
        )

    def delete(
        self,
        db: Session,
        indicador_id: UUID,
    ) -> None:

        indicador = self.get(
            db,
            indicador_id,
        )

        indicador_repository.delete(
            db,
            indicador,
        )


indicador_service = IndicadorService()