from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.relatorio_service import relatorio_service

router = APIRouter(
    prefix="/relatorios",
    tags=["Relatórios"],
)


@router.get("/colaboradores/excel")
async def gerar_excel(
    db: Session = Depends(get_db),
):

    arquivo = await relatorio_service.gerar_excel_colaboradores(db)

    return StreamingResponse(
        arquivo,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": 'attachment; filename="colaboradores.xlsx"'
        },
    )