from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from repositories.user_repository import UserRepository
from schemas.user_schema import UserCreate, UserResponse
from services.user_service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    data: UserCreate,
    db: Session = Depends(get_db)
):
    repository = UserRepository(db)
    service = UserService(repository)

    user = service.create_user(data)

    return user