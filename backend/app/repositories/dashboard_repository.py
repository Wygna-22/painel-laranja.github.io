from datetime import date
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.colaborador import Colaborador
from app.models.enums import StatusColaborador

class DashboardRepository:

    def get_cards(self, db: Session):

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

    def get_colaboradores_por_setor(
        self,
        db: Session,
    ):

        resultado = (
            db.query(
                Colaborador.setor,
                func.count(Colaborador.id)
            )
            .group_by(
                Colaborador.setor
            )
            .all()
        )

        return [
            {
                "setor": setor,
                "quantidade": quantidade,
            }
            for setor, quantidade in resultado
        ]

    def get_colaboradores_por_cidade(
        self,
        db: Session,
    ):

        resultado = (
            db.query(
                Colaborador.cidade,
                func.count(Colaborador.id)
            )
            .group_by(
                Colaborador.cidade
            )
            .all()
        )

        return [
            {
                "cidade": cidade,
                "quantidade": quantidade,
            }
            for cidade, quantidade in resultado
        ]

dashboard_repository = DashboardRepository()