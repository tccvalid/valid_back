from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database import get_db
from app.schemas.usuario import UsuarioCriacao
from app.services.autenticacao import criar_usuario

from app.utils.seguranca import criar_access_token

from app.services.dois_fatores import criar_token_2fa
from app.schemas.dois_fatores import Verificar2FARequest
from app.services.dois_fatores import verificar_codigo_2fa


router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)


@router.post("/cadastro")
def cadastro(
    usuario: UsuarioCriacao,
    db: Session = Depends(get_db)
):

    novo_usuario = criar_usuario(db, usuario)

    if novo_usuario is None:
        raise HTTPException(
            status_code=400,
            detail="Email já cadastrado."
        )

    return {
        "mensagem": "Usuário criado com sucesso!",
        "id_usuario": novo_usuario.id_usuario
    }

from app.schemas.usuario import UsuarioLogin
from app.services.autenticacao import autenticar_usuario

@router.post("/login")
def login(
    dados: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    usuario = autenticar_usuario(
        email=dados.username,
        senha=dados.password,
        db=db
    )

    # Verifica se o usuário possui 2FA ativo
    if usuario.dois_fatores_ativo:

        criar_token_2fa(db, usuario)

        return {
            "status": "2fa",
            "mensagem": "Enviamos um código de verificação para seu e-mail.",
            "email": usuario.email
        }

    token = criar_access_token(
        {
            "sub": str(usuario.id_usuario)
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.post("/verificar-2fa")
def verificar_2fa(
    dados: Verificar2FARequest,
    db: Session = Depends(get_db)
):

    access_token = verificar_codigo_2fa(
        db=db,
        email=dados.email,
        codigo=dados.codigo
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }