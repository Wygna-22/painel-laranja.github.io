from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dependencies.auth import get_current_user, require_role
from app.models.enums import UserRole
from app.models.user import User
from app.schemas.ferias import (
    FeriasCreate,
    FeriasResponse,
    FeriasUpdate,
)
from app.services.ferias_service import ferias_service

router = APIRouter(
    prefix="/ferias",
    tags=["Férias"],
)


@router.post(
    "",
    response_model=FeriasResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_ferias(
    ferias: FeriasCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    return ferias_service.create(
        db,
        ferias,
    )


@router.get(
    "",
    response_model=list[FeriasResponse],
)
def list_ferias(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ferias_service.list_all(db)


@router.get(
    "/{ferias_id}",
    response_model=FeriasResponse,
)
def get_ferias(
    ferias_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ferias_service.get(
        db,
        ferias_id,
    )


@router.get(
    "/colaborador/{colaborador_id}",
    response_model=list[FeriasResponse],
)
def list_ferias_by_colaborador(
    colaborador_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ferias_service.list_by_colaborador(
        db,
        colaborador_id,
    )


@router.put(
    "/{ferias_id}",
    response_model=FeriasResponse,
)
def update_ferias(
    ferias_id: UUID,
    data: FeriasUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    return ferias_service.update(
        db,
        ferias_id,
        data,
    )


@router.delete(
    "/{ferias_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_ferias(
    ferias_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    ferias_service.delete(
        db,
        ferias_id,
    )