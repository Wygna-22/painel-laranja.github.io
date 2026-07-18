from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dependencies.auth import get_current_user, require_role
from app.models.enums import UserRole
from app.models.user import User
from app.schemas.historico import (
    HistoricoCreate,
    HistoricoResponse,
    HistoricoUpdate,
)
from app.services.historico_service import historico_service

router = APIRouter(
    prefix="/historicos",
    tags=["Históricos"],
)

@router.post(
    "",
    response_model=HistoricoResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_historico(
    historico: HistoricoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    return historico_service.create(
        db,
        historico,
    )

@router.get(
    "",
    response_model=list[HistoricoResponse],
)
def list_historicos(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return historico_service.list_all(db)

@router.get(
    "/{historico_id}",
    response_model=HistoricoResponse,
)
def get_historico(
    historico_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return historico_service.get(
        db,
        historico_id,
    )

@router.get(
    "/colaborador/{colaborador_id}",
    response_model=list[HistoricoResponse],
)
def list_historico_colaborador(
    colaborador_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return historico_service.list_by_colaborador(
        db,
        colaborador_id,
    )

@router.put(
    "/{historico_id}",
    response_model=HistoricoResponse,
)
def update_historico(
    historico_id: UUID,
    data: HistoricoUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    return historico_service.update(
        db,
        historico_id,
        data,
    )

@router.delete(
    "/{historico_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_historico(
    historico_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN)),
):
    historico_service.delete(
        db,
        historico_id,
    )