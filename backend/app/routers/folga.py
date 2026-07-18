from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dependencies.auth import get_current_user, require_role
from app.models.enums import UserRole
from app.models.user import User
from app.schemas.folga import (
    FolgaCreate,
    FolgaResponse,
    FolgaUpdate,
)
from app.services.folga_service import folga_service

router = APIRouter(
    prefix="/folgas",
    tags=["Folgas"],
)

@router.post(
    "",
    response_model=FolgaResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_folga(
    folga: FolgaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    return folga_service.create(
        db,
        folga,
    )

@router.get(
    "",
    response_model=list[FolgaResponse],
)
def list_folgas(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return folga_service.list_all(db)

@router.get(
    "/{folga_id}",
    response_model=FolgaResponse,
)
def get_folga(
    folga_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return folga_service.get(
        db,
        folga_id,
    )

@router.get(
    "/colaborador/{colaborador_id}",
    response_model=list[FolgaResponse],
)
def list_folgas_by_colaborador(
    colaborador_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return folga_service.list_by_colaborador(
        db,
        colaborador_id,
    )

@router.put(
    "/{folga_id}",
    response_model=FolgaResponse,
)
def update_folga(
    folga_id: UUID,
    data: FolgaUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    return folga_service.update(
        db,
        folga_id,
        data,
    )

@router.delete(
    "/{folga_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_folga(
    folga_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    folga_service.delete(
        db,
        folga_id,
    )