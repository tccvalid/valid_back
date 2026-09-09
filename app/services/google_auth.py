from sqlalchemy.orm import Session

from app.models.usuario import Usuario


def criar_ou_buscar_usuario_google(
    db: Session,
    nome: str,
    email: str,
    google_id: str
):

    # 1 - Verifica se já existe usuário com esse email
    usuario = db.query(Usuario).filter(
        Usuario.email == email
    ).first()


    # 2 - Se existir, retorna ele
    if usuario:
        return usuario


    # 3 - Se não existir, cria um novo usuário Google
    novo_usuario = Usuario(
        nome=nome,
        email=email,
        google_id=google_id,
        email_verificado=True
    )


    db.add(novo_usuario)

    db.commit()

    db.refresh(novo_usuario)


    return novo_usuario

import httpx

from app.config import (
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET
)


def pegar_dados_google(code: str):

    token_url = "https://oauth2.googleapis.com/token"


    dados = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": "http://localhost:8000/auth/google/callback",
        "grant_type": "authorization_code"
    }


    resposta = httpx.post(
        token_url,
        data=dados
    )


    token_google = resposta.json()


    access_token = token_google["access_token"]


    resposta_usuario = httpx.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )


    return resposta_usuario.json()