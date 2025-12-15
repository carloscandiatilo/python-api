import uvicorn
from main import app  # Importa a instância app do main.py

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
