from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import LoginRequest, Token
from app.services.auth import auth_service

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post(
    "/login",
    response_model=Token,
)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db),
):
    try:
        return auth_service.login(
            db,
            credentials.email,
            credentials.senha,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )