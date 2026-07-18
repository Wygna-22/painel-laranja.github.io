from sqlalchemy.orm import Session

from app.repositories.dashboard_repository import (
    dashboard_repository,
)

class DashboardService:
    def get_dashboard(
        self,
        db: Session,
    ):
        cards = dashboard_repository.get_cards(db)

        por_setor = (
            dashboard_repository.get_colaboradores_por_setor(db)
        )

        por_cidade = (
            dashboard_repository.get_colaboradores_por_cidade(db)
        )

        return {
            **cards,
            "por_setor": por_setor,
            "por_cidade": por_cidade,
        }

dashboard_service = DashboardService()