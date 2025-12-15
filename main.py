from fastapi import FastAPI
from database import Base, engine
from routers.user import router as user_router

app = FastAPI()

# Cria as tabelas automaticamente
Base.metadata.create_all(bind=engine)

# Incluir router
app.include_router(user_router)

@app.get("/")
def home():
    return {"mensagem": "Olá, mundo!"}
