from fastapi import FastAPI

app = FastAPI(
    title="Painel Laranja API",
    version="1.0.0"
)

@app.get("/")
async def home():

    return {
        "status": "online",
        "projeto": "Painel Laranja"
    }