from sqlalchemy.orm import Session

from app.core.jwt import create_access_token
from app.schemas.auth import Token
from app.services.user import user_service

class AuthService:
    def login(self, db: Session, email: str, senha: str) -> Token:
        user = user_service.authenticate(db, email, senha)

        if not user:
            raise ValueError("E-mail ou senha inválidos.")

        token = create_access_token(
            {
                "sub": str(user.id),
                "perfil": user.perfil.value,
            }
        )

        return Token(access_token=token)

auth_service = AuthService()