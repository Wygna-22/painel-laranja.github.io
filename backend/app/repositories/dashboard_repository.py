from datetime import date
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.colaborador import Colaborador
from app.models.colaborador import StatusColaborador

class DashboardRepository:

    def get_indicators(self, db: Session):

        hoje = date.today()

        inicio_mes = date(
            hoje.year,
            hoje.month,
            1,
        )

        return {
            "total_colaboradores": db.query(
                Colaborador
            ).count(),

            "ativos": db.query(
                Colaborador
            ).filter(
                Colaborador.status == StatusColaborador.ATIVO
            ).count(),

            "afastados": db.query(
                Colaborador
            ).filter(
                Colaborador.status == StatusColaborador.AFASTADO
            ).count(),

            "desligados": db.query(
                Colaborador
            ).filter(
                Colaborador.status == StatusColaborador.DESLIGADO
            ).count(),

            "admissoes_mes": db.query(
                Colaborador
            ).filter(
                Colaborador.data_admissao >= inicio_mes
            ).count(),
        }


dashboard_repository = DashboardRepository()