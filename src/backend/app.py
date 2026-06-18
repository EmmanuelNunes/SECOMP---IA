from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.backend.routes import router as api_router

app = FastAPI(
    title="Career-AI API", 
    version="1.0.0", 
    description="Backend do MVP da SECOMP 2026 - Workshop de IA e Agentes Autônomos"
)

# Configura CORS para permitir requisições de qualquer origem (essencial para testes locais)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do Career-AI!"}

@app.get("/health")
def health_check():
    return {"status": "Tudo rodando perfeitamente!"}

# Inclui as rotas dos agentes integrados ao RAG
app.include_router(api_router)
