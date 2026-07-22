from sqlalchemy.orm import Session

from app.models.indicador import Indicador
from app.repositories.base import BaseRepository
from app.models.user import User


class IndicadorRepository(BaseRepository[Indicador]):

    def __init__(self):
        super().__init__(Indicador)

    def get_by_user_mes_ano(
        self,
        db: Session,
        user_id,
        mes: int,
        ano: int,
    ) -> Indicador | None:

        return (
            db.query(Indicador)
            .filter(
                Indicador.user_id == user_id,
                Indicador.mes == mes,
                Indicador.ano == ano,
            )
            .first()
        )

    def get_by_mes(
        self,
        db: Session,
        mes: int,
        ano: int,
    ):

        indicadores = (
            db.query(
                Indicador,
                User.nome,
            )
            .join(
                User,
                Indicador.user_id == User.id,
            )
            .filter(
                Indicador.mes == mes,
                Indicador.ano == ano,
            )
            .all()
        )

        return [
            {
                **indicador.__dict__,
                "gestor": nome,
            }
            for indicador, nome in indicadores
        ]

    def get_all_with_gestor(
        self,
        db: Session,
    ):

        indicadores = (
            db.query(
                Indicador,
                User.nome,
            )
            .join(
                User,
                Indicador.user_id == User.id,
            )
            .all()
        )

        return [
            {
                **indicador.__dict__,
                "gestor": nome,
            }
            for indicador, nome in indicadores
        ]


indicador_repository = IndicadorRepository()