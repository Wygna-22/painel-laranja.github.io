from uuid import UUID

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.indicador import (
    IndicadorCreate,
    IndicadorResponse,
    IndicadorUpdate,
)
from app.services.indicador_service import indicador_service

router = APIRouter(
    prefix="/indicadores",
    tags=["Indicadores"],
)


@router.post(
    "/",
    response_model=IndicadorResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_indicador(
    indicador: IndicadorCreate,
    db: Session = Depends(get_db),
):
    return indicador_service.create(
        db,
        indicador,
    )


@router.get(
    "/",
    response_model=list[IndicadorResponse],
)
def list_indicadores(
    db: Session = Depends(get_db),
):
    return indicador_service.list_all(db)


@router.get(
    "/{indicador_id}",
    response_model=IndicadorResponse,
)
def get_indicador(
    indicador_id: UUID,
    db: Session = Depends(get_db),
):
    return indicador_service.get(
        db,
        indicador_id,
    )


@router.put(
    "/{indicador_id}",
    response_model=IndicadorResponse,
)
def update_indicador(
    indicador_id: UUID,
    data: IndicadorUpdate,
    db: Session = Depends(get_db),
):
    return indicador_service.update(
        db,
        indicador_id,
        data,
    )


@router.delete(
    "/{indicador_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_indicador(
    indicador_id: UUID,
    db: Session = Depends(get_db),
):
    indicador_service.delete(
        db,
        indicador_id,
    )

    return Response(status_code=status.HTTP_204_NO_CONTENT)