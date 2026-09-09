from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
import requests

from urllib.parse import urlencode

from app.utils.seguranca import criar_access_token

from app.database import get_db
from app.config import GOOGLE_CLIENT_ID

from app.services.google_auth import (
    criar_ou_buscar_usuario_google,
    pegar_dados_google
)


router = APIRouter(
    prefix="/auth/google",
    tags=["Google"]
)


@router.post("/teste")
def teste_google(
    db: Session = Depends(get_db)
):

    usuario = criar_ou_buscar_usuario_google(
        db=db,
        nome="Ana Google",
        email="anagoogle@gmail.com",
        google_id="123456789"
    )


    return {
        "id": usuario.id_usuario,
        "nome": usuario.nome,
        "email": usuario.email
    }



@router.get("")
def login_google():

    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": "http://localhost:8000/auth/google/callback",
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline"
    }


    url = (
        "https://accounts.google.com/o/oauth2/auth?"
        + urlencode(params)
    )


    return RedirectResponse(url)



@router.get("/callback")
def google_callback(
    code: str,
    db: Session = Depends(get_db)
):
    dados_google = pegar_dados_google(code)

    usuario = criar_ou_buscar_usuario_google(
        db=db,
        nome=dados_google["name"],
        email=dados_google["email"],
        google_id=dados_google["id"]
    )

    token = criar_access_token(
        {
            "sub": str(usuario.id_usuario)
        }
    )

    frontend = "http://localhost:5173"

    try:
        requests.get(frontend, timeout=1)
    except:
        frontend = "http://localhost:5174"

    return RedirectResponse(
        f"{frontend}/google/callback?token={token}"
    )