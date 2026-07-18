from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.folga import Folga
from app.repositories.folga_repository import folga_repository
from app.schemas.folga import (
    FolgaCreate,
    FolgaUpdate,
)

class FolgaService:

    def create(
        self,
        db: Session,
        data: FolgaCreate,
    ) -> Folga:

        nova_folga = Folga(
            **data.model_dump()
        )

        return folga_repository.create(
            db,
            nova_folga,
        )

    def get(
        self,
        db: Session,
        folga_id: UUID,
    ) -> Folga:

        folga = folga_repository.get(
            db,
            folga_id,
        )

        if not folga:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Folga não encontrada.",
            )

        return folga

    def list_all(
        self,
        db: Session,
    ) -> list[Folga]:
        return folga_repository.get_all(db)

    def list_by_colaborador(
        self,
        db: Session,
        colaborador_id: UUID,
    ) -> list[Folga]:
        return folga_repository.get_by_colaborador(
            db,
            colaborador_id,
        )

    def update(
        self,
        db: Session,
        folga_id: UUID,
        data: FolgaUpdate,
    ) -> Folga:

        folga = self.get(
            db,
            folga_id,
        )

        return folga_repository.update(
            db,
            folga,
            data.model_dump(exclude_unset=True),
        )

    def delete(
        self,
        db: Session,
        folga_id: UUID,
    ) -> None:

        folga = self.get(
            db,
            folga_id,
        )

        folga_repository.delete(
            db,
            folga,
        )


folga_service = FolgaService()