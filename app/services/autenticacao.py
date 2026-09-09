from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCriacao

from app.utils.seguranca import gerar_hash
from app.utils.seguranca import verificar_senha

def criar_usuario(
    db: Session,
    usuario: UsuarioCriacao
):

    usuario_existente = (
        db.query(Usuario)
        .filter(Usuario.email == usuario.email)
        .first()
    )

    if usuario_existente:
        return None


    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha_hash=gerar_hash(usuario.senha)
    )


    db.add(novo_usuario)

    db.commit()

    db.refresh(novo_usuario)


    return novo_usuario


def autenticar_usuario(
    email: str,
    senha: str,
    db: Session
):
    usuario = db.query(Usuario).filter(
        Usuario.email == email
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos."
        )

    if not verificar_senha(
        senha,
        usuario.senha_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos."
        )

    return usuario


