from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dependencies.auth import get_current_user, require_role
from app.models.enums import UserRole
from app.models.user import User
from app.schemas.colaborador import (
    ColaboradorCreate,
    ColaboradorResponse,
    ColaboradorUpdate,
)
from app.services.colaborador_service import colaborador_service

router = APIRouter(
    prefix="/colaboradores",
    tags=["Colaboradores"],
)

@router.post(
    "",
    response_model=ColaboradorResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_colaborador(
    colaborador: ColaboradorCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    return colaborador_service.create(
        db,
        colaborador,
    )

@router.get(
    "",
    response_model=list[ColaboradorResponse],
)
def list_colaboradores(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return colaborador_service.list_all(db)

@router.get(
    "/{colaborador_id}",
    response_model=ColaboradorResponse,
)
def get_colaborador(
    colaborador_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return colaborador_service.get(
        db,
        colaborador_id,
    )

@router.put(
    "/{colaborador_id}",
    response_model=ColaboradorResponse,
)
def update_colaborador(
    colaborador_id: UUID,
    data: ColaboradorUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    return colaborador_service.update(
        db,
        colaborador_id,
        data,
    )

@router.delete(
    "/{colaborador_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_colaborador(
    colaborador_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    colaborador_service.delete(
        db,
        colaborador_id,
    )