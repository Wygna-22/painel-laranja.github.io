from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.enums import UserRole
from app.models.user import User
from app.repositories.gestor_repository import gestor_repository
from app.schemas.gestor import (
    GestorCreate,
    GestorUpdate,
)
from app.core.security import hash_password

# IMPORTAR AQUI SUA FUNÇÃO DE HASH
# Exemplo:
# from app.core.security import hash_password


class GestorService:

    def get_all(self, db: Session):
        return gestor_repository.get_all(db)

    def get_by_id(self, db: Session, gestor_id):
        return gestor_repository.get(db, gestor_id)

    def create(
        self,
        db: Session,
        gestor: GestorCreate,
    ):

        existente = gestor_repository.get_by_email(
            db,
            gestor.email,
        )

        if existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Já existe um gestor com este e-mail.",
            )

        novo_gestor = User(
            nome=gestor.nome,
            email=gestor.email,

            # ALTERAR AQUI PARA SUA FUNÇÃO DE HASH
            senha_hash=hash_password(gestor.senha),

            perfil=UserRole.GESTOR,
            ativo=True,
        )

        return gestor_repository.create(
            db,
            novo_gestor,
        )

    def update(
        self,
        db: Session,
        gestor_id,
        gestor: GestorUpdate,
    ):

        gestor_db = gestor_repository.get(
            db,
            gestor_id,
        )

        if not gestor_db:
            return None

        dados = gestor.model_dump(
            exclude_unset=True
        )

        if "senha" in dados:
            dados["senha_hash"] = hash_password(
                dados.pop("senha")
            )

        return gestor_repository.update(
            db,
            gestor_db,
            dados,
        )

    def delete(
        self,
        db: Session,
        gestor_id,
    ):
        gestor = gestor_repository.get(
            db,
            gestor_id,
        )

        if not gestor:
            return False

        gestor_repository.delete(
            db,
            gestor,
        )
        return True

gestor_service = GestorService()