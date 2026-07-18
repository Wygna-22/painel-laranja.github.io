from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.colaborador import Colaborador
from app.repositories.colaborador_repository import colaborador_repository
from app.schemas.colaborador import (
    ColaboradorCreate,
    ColaboradorUpdate,
)

class ColaboradorService:

    def create(
        self,
        db: Session,
        colaborador: ColaboradorCreate,
    ) -> Colaborador:

        if colaborador_repository.get_by_matricula(
            db,
            colaborador.matricula,
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Matrícula já cadastrada.",
            )

        if (
            colaborador.email
            and colaborador_repository.get_by_email(
                db,
                colaborador.email,
            )
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="E-mail já cadastrado.",
            )

        novo_colaborador = Colaborador(
            **colaborador.model_dump()
        )

        return colaborador_repository.create(
            db,
            novo_colaborador,
        )

    def get(
        self,
        db: Session,
        colaborador_id: UUID,
    ) -> Colaborador:

        colaborador = colaborador_repository.get(
            db,
            colaborador_id,
        )

        if not colaborador:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Colaborador não encontrado.",
            )

        return colaborador
    
    def list_all(
        self,
        db: Session,
    ) -> list[Colaborador]:
        return colaborador_repository.get_all(db)
    
    def list_by_gestor(
        self,
        db: Session,
        gestor_id: UUID,
    ) -> list[Colaborador]:
        return colaborador_repository.get_by_gestor(
            db,
            gestor_id,
        )
    
    def update(
        self,
        db: Session,
        colaborador_id: UUID,
        data: ColaboradorUpdate,
    ) -> Colaborador:

        colaborador = self.get(
            db,
            colaborador_id,
        )

        return colaborador_repository.update(
            db,
            colaborador,
            data.model_dump(exclude_unset=True),
        )
    
    def delete(
        self,
        db: Session,
        colaborador_id: UUID,
    ) -> None:

        colaborador = self.get(
            db,
            colaborador_id,
        )

        colaborador_repository.delete(
            db,
            colaborador,
        )


colaborador_service = ColaboradorService()