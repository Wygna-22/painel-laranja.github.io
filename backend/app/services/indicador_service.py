from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.enums import UserRole
from app.models.indicador import Indicador
from app.models.user import User
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
    ):

        usuario = db.get(
            User,
            indicador.user_id,
        )

        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuário não encontrado.",
            )

        if usuario.perfil != UserRole.GESTOR:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="O usuário informado não é um gestor.",
            )

        indicador_existente = indicador_repository.get_by_user_mes_ano(
            db,
            indicador.user_id,
            indicador.mes,
            indicador.ano,
        )

        if indicador_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Já existe um indicador para este gestor neste mês.",
            )

        novo_indicador = Indicador(
            **indicador.model_dump()
        )

        indicador_criado = indicador_repository.create(
            db,
            novo_indicador,
        )

        return {
            **indicador_criado.__dict__,
            "gestor": usuario.nome,
        }

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
    ):
        return indicador_repository.get_all_with_gestor(db)

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

        if data.user_id is not None:

            usuario = db.get(
                User,
                data.user_id,
            )

            if not usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuário não encontrado.",
                )

            if usuario.perfil != UserRole.GESTOR:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="O usuário informado não é um gestor.",
                )

            mes = data.mes if data.mes is not None else indicador.mes
            ano = data.ano if data.ano is not None else indicador.ano

            existente = indicador_repository.get_by_user_mes_ano(
                db,
                data.user_id,
                mes,
                ano,
            )

            if existente and existente.id != indicador.id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Já existe um indicador para este gestor neste mês.",
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