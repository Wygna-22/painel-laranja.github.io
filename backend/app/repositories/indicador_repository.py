from sqlalchemy.orm import Session

from app.models.indicador import Indicador
from app.repositories.base import BaseRepository


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
    ) -> list[Indicador]:

        return (
            db.query(Indicador)
            .filter(
                Indicador.mes == mes,
                Indicador.ano == ano,
            )
            .all()
        )


indicador_repository = IndicadorRepository()