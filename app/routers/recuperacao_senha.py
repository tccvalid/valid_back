from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.email import enviar_email

from app.database import get_db

from app.models.usuario import Usuario

from app.schemas.token_usuario import EsqueciSenhaRequest

from app.services.recuperacao_senha import criar_token_recuperacao

from app.schemas.token_usuario import RedefinirSenhaRequest

from app.services.recuperacao_senha import redefinir_senha

import requests


router = APIRouter(
    prefix="/auth",
    tags=["Recuperação de Senha"]
)


@router.post("/esqueci-senha")
def esqueci_senha(
    dados: EsqueciSenhaRequest,
    db: Session = Depends(get_db)
):

    usuario = (
        db.query(Usuario)
        .filter(Usuario.email == dados.email)
        .first()
    )

    if usuario:

        token = criar_token_recuperacao(
            usuario,
            db
        )

        frontend = "http://localhost:5173"

        try:
            requests.get(frontend, timeout=1)
        except:
            frontend = "http://localhost:5174"

        link = f"{frontend}/novaSenha?token={token}"

        mensagem = f"""
        Olá, {usuario.nome}!

        Recebemos uma solicitação para redefinir sua senha na plataforma VALID.

        Clique no link abaixo para criar uma nova senha:

        {link}

        Esse link é válido por 30 minutos.

        Caso você não tenha solicitado essa alteração, ignore este e-mail.
        """

        enviar_email(
            destinatario=usuario.email,
            assunto="Recuperação de senha - VALID",
            mensagem=mensagem
        )

    return {
        "mensagem": "Se o e-mail existir, enviaremos as instruções para recuperação da senha."
    }

@router.post("/redefinir-senha")
def trocar_senha(
    dados: RedefinirSenhaRequest,
    db: Session = Depends(get_db)
):

    redefinir_senha(
        token=dados.token,
        nova_senha=dados.nova_senha,
        db=db
    )


    return {
        "mensagem": "Senha alterada com sucesso!"
    }
