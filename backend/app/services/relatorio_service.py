from sqlalchemy.orm import Session
from app.reports.colaborador_excel import ColaboradorExcel
from app.repositories.relatorio_repository import (
    relatorio_repository,
)

class RelatorioService:

    def __init__(self, repository):
        self.repository = repository

    async def gerar_excel_colaboradores(
        self,
        db: Session,
    ):

        colaboradores = self.repository.listar_colaboradores(db)

        report = ColaboradorExcel(colaboradores)

        return report.generate()

relatorio_service = RelatorioService(
    relatorio_repository
)