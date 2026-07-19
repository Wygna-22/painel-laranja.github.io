from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.jwt import decode_access_token
from app.repositories.user import user_repository
from app.models.enums import UserRole

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Token inválido.",
        )

    user_id = payload.get("sub")

    user = user_repository.get_by_id(
        db,
        user_id,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Usuário não encontrado.",
        )

    return user

def require_role(role: UserRole):
    def role_checker(
        current_user=Depends(get_current_user),
    ):
        if current_user.perfil != role:
            raise HTTPException(
                status_code=403,
                detail="Você não possui permissão para acessar este recurso.",
            )
        return current_user

    return role_checker

def require_roles(*roles: UserRole):
    def role_checker(
        current_user=Depends(get_current_user),
    ):
        if current_user.perfil not in roles:
            raise HTTPException(
                status_code=403,
                detail="Você não possui permissão para acessar este recurso.",
            )
        return current_user

    return role_checker