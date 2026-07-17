from fastapi import FastAPI
from fastapi import Depends
from app.routers.users import router as user_router
from app.routers.auth import router as auth_router
from app.dependencies.auth import get_current_token

app = FastAPI(
    title="Painel Laranja API",
    version="1.0.0",
)

app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "🍊 Painel Laranja API"}

@app.get("/me")
def me(
    token: str = Depends(get_current_token),
):
    return {
        "token": token
    }