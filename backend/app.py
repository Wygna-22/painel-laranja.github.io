from fastapi import FastAPI
from sqlalchemy import text

from database.session import SessionLocal
from routes.auth_routes import router as auth_router

app = FastAPI()
app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "status": "online",
        "projeto": "Painel Laranja"
    }


@app.get("/db")
def testar_banco():

    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))
        return {"banco": "Conectado com sucesso"}

    except Exception as e:
        return {"erro": str(e)}

    finally:
        db.close()