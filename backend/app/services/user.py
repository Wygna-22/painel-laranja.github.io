from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user import user_repository
from app.schemas.user import UserCreate
from app.core.security import (
    hash_password,
    verify_password,
)

class UserService:
    def create_user(self, db: Session, user: UserCreate) -> User:
        # Verifica se o e-mail já existe
        existing_user = user_repository.get_by_email(db, user.email)

        if existing_user:
            raise ValueError("Já existe um usuário com este e-mail.")

        # Criptografa a senha
        senha_hash = hash_password(user.senha)

        # Cria o objeto
        novo_usuario = User(
            nome=user.nome,
            email=user.email,
            senha_hash=senha_hash,
            perfil=user.perfil,
        )

        return user_repository.create(db, novo_usuario)

    def authenticate(self, db: Session, email: str, senha: str):
        usuario = user_repository.get_by_email(db, email)

        if not usuario:
            return None

        if not verify_password(
            senha,
            usuario.senha_hash,
        ):
            return None

        return usuario
    
    def get_all_gestores(self, db: Session):
        return self.repository.get_all_gestores(db)


    def get_gestor(self, db: Session, gestor_id):
        return self.repository.get_gestor(db, gestor_id)

user_service = UserService()