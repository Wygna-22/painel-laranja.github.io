from sqlalchemy.orm import Session
from app.repositories.dashboard_repository import (
    dashboard_repository,
)

class DashboardService:

    def get_dashboard(
        self,
        db: Session,
    ):
        return dashboard_repository.get_indicators(
            db
        )

dashboard_service = DashboardService()