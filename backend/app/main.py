from fastapi import FastAPI
from fastapi import Depends
from app.routers.users import router as user_router
from app.routers.auth import router as auth_router
from app.routers.colaborador import router as colaborador_router
from app.routers import dashboard
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.dependencies.auth import require_role
from app.models.enums import UserRole

app = FastAPI(
    title="Painel Laranja API",
    version="1.0.0",
)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(colaborador_router)
app.include_router(dashboard.router)

@app.get("/")
def root():
    return {"message": "🍊 Painel Laranja API"}

@app.get("/me")
def me(
    current_user: User = Depends(get_current_user),
):
    return {
        "id": str(current_user.id),
        "nome": current_user.nome,
        "email": current_user.email,
        "perfil": current_user.perfil,
    }

@app.get("/admin")
def admin_area(
    current_user=Depends(
        require_role(UserRole.ADMIN)
    ),
):
    return {
        "usuario": current_user.nome,
        "perfil": current_user.perfil,
        "mensagem": "Área exclusiva do administrador."
    }