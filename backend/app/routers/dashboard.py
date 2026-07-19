from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dependencies.auth import (
    get_current_user,
    require_roles,
)
from app.models.enums import UserRole
from app.models.user import User
from app.schemas.dashboard import DashboardResponse
from app.services.dashboard_service import dashboard_service

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)

@router.get(
    "",
    response_model=DashboardResponse,
    summary="Dashboard Geral",
)
def get_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles(
            UserRole.ADMIN,
            UserRole.GESTOR,
        )
    ),
):
    return dashboard_service.get_dashboard(db)