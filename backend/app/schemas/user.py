from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr
from app.models.enums import UserRole

class UserBase(BaseModel):
    nome: str
    email: EmailStr

class UserCreate(UserBase):
    senha: str
    perfil: UserRole = UserRole.COLABORADOR

class UserUpdate(BaseModel):
    nome: str | None = None
    email: EmailStr | None = None
    senha: str | None = None
    perfil: UserRole | None = None
    ativo: bool | None = None

class UserResponse(UserBase):
    id: UUID
    perfil: UserRole
    ativo: bool

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    senha: str