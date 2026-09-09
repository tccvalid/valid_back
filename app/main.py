from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import autenticacao

from app.routers import perfil

from app.routers import recuperacao_senha

from app.routers import google_auth

from app.routers.contato import router as contato_router

app = FastAPI(
    title="VALID API",
    description="API responsável pelo gerenciamento da plataforma VALID.",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    autenticacao.router
)

app.include_router(
    perfil.router
)

app.include_router(
    recuperacao_senha.router
)

app.include_router(
    google_auth.router
)

app.include_router(contato_router)

@app.get("/")
def raiz():
    return {
        "mensagem": "API VALID funcionando"
    }