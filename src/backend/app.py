from fastapi import FastAPI

app = FastAPI(title="Career-AI API", version="1.0.0", description="Backend do MVP da SECOMP 2026")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do Career-AI!"}

@app.get("/health")
def health_check():
    return {"status": "Tudo rodando perfeitamente!"}

# TODO: Importar as rotas que chamarão o LangGraph e o ChromaDB
