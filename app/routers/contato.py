from fastapi import APIRouter

from app.schemas.contato import ContatoRequest
from app.services.contato import enviar_contato

router = APIRouter(
    prefix="/contato",
    tags=["Contato"]
)


@router.post("/")
def contato(dados: ContatoRequest):

    enviar_contato(dados)

    return {
        "mensagem": "Mensagem enviada com sucesso."
    }