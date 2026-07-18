from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.ferias import Ferias
from app.repositories.ferias_repository import ferias_repository
from app.schemas.ferias import (
    FeriasCreate,
    FeriasUpdate,
)

class FeriasService:
    def create(
        self,
        db: Session,
        data: FeriasCreate,
    ) -> Ferias:

        if data.data_inicio > data.data_fim:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A data de início não pode ser maior que a data de fim.",
            )

        nova_ferias = Ferias(**data.model_dump())

        return ferias_repository.create(
            db,
            nova_ferias,
        )

    def get(
        self,
        db: Session,
        ferias_id: UUID,
    ) -> Ferias:

        ferias = ferias_repository.get(
            db,
            ferias_id,
        )

        if not ferias:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Registro de férias não encontrado.",
            )

        return ferias

    def list_all(
        self,
        db: Session,
    ) -> list[Ferias]:
        return ferias_repository.get_all(db)

    def list_by_colaborador(
        self,
        db: Session,
        colaborador_id: UUID,
    ) -> list[Ferias]:
        return ferias_repository.get_by_colaborador(
            db,
            colaborador_id,
        )

    def update(
        self,
        db: Session,
        ferias_id: UUID,
        data: FeriasUpdate,
    ) -> Ferias:

        ferias = self.get(
            db,
            ferias_id,
        )

        if (
            data.data_inicio is not None
            and data.data_fim is not None
            and data.data_inicio > data.data_fim
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A data de início não pode ser maior que a data de fim.",
            )

        return ferias_repository.update(
            db,
            ferias,
            data.model_dump(exclude_unset=True),
        )

    def delete(
        self,
        db: Session,
        ferias_id: UUID,
    ) -> None:

        ferias = self.get(
            db,
            ferias_id,
        )

        ferias_repository.delete(
            db,
            ferias,
        )

ferias_service = FeriasService()