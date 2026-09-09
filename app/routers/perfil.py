from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app.dependencies.autenticacao import obter_usuario_atual
from app.schemas.usuario import UsuarioAtualizacao
from app.models.usuario import Usuario

from app.schemas.dois_fatores import Atualizar2FARequest


router = APIRouter(
    prefix="/perfil",
    tags=["Perfil"]
)

@router.get("/")
def visualizar_perfil(
    usuario: Usuario = Depends(obter_usuario_atual)
):

    return {
        "id": usuario.id_usuario,
        "nome": usuario.nome,
        "email": usuario.email,
        "dois_fatores_ativo": usuario.dois_fatores_ativo
    }

@router.put("/")
def atualizar_perfil(
    dados: UsuarioAtualizacao,
    usuario: Usuario = Depends(obter_usuario_atual),
    db: Session = Depends(get_db)
):

    usuario.nome = dados.nome
    usuario.email = dados.email

    db.commit()
    db.refresh(usuario)

    return {
        "mensagem": "Perfil atualizado com sucesso!",
        "usuario": {
            "nome": usuario.nome,
            "email": usuario.email
        }
    }

@router.put("/2fa")
def atualizar_2fa(
    dados: Atualizar2FARequest,
    usuario: Usuario = Depends(obter_usuario_atual),
    db: Session = Depends(get_db)
):

    usuario.dois_fatores_ativo = dados.ativo

    db.commit()
    db.refresh(usuario)

    return {
        "mensagem": "Configuração de 2FA atualizada!",
        "dois_fatores_ativo": usuario.dois_fatores_ativo
    }

@router.get("/teste-google")
def teste_google(
    usuario = Depends(obter_usuario_atual)
):

    return {
        "id": usuario.id_usuario,
        "nome": usuario.nome,
        "email": usuario.email,
        "dois_fatores_ativo": usuario.dois_fatores_ativo
    }