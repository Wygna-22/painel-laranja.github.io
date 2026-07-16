from fastapi import FastAPI
from sqlalchemy import text

from database.session import SessionLocal

app = FastAPI()


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