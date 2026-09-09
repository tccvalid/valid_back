from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCriacao

from app.utils.seguranca import gerar_hash
from app.utils.seguranca import verificar_senha

from datetime import datetime, timedelta
import secrets
from app.models.token_usuario import TokenUsuario
from app.enums.tipo_token import TipoToken


def criar_token_recuperacao(
    usuario: Usuario,
    db: Session
) -> str:
    """
    Cria um token temporário para recuperação de senha.
    """

    token = secrets.token_urlsafe(32)

    expiracao = datetime.now() + timedelta(minutes=30)

    tokens_antigos = (
    db.query(TokenUsuario)
    .filter(
        TokenUsuario.id_usuario == usuario.id_usuario,
        TokenUsuario.tipo_token == TipoToken.RECUPERACAO_SENHA.value,
        TokenUsuario.utilizado == False
    )
    .all()
    )

    for token_antigo in tokens_antigos:
        token_antigo.utilizado = True

    db.commit()

    novo_token = TokenUsuario(
        id_usuario=usuario.id_usuario,
        token=token,
        tipo_token=TipoToken.RECUPERACAO_SENHA.value,
        data_expiracao=expiracao
    )

    db.add(novo_token)
    db.commit()
    db.refresh(novo_token)

    return token

def redefinir_senha(
    token: str,
    nova_senha: str,
    db: Session
):

    token_usuario = (
        db.query(TokenUsuario)
        .filter(
            TokenUsuario.token == token,
            TokenUsuario.tipo_token == TipoToken.RECUPERACAO_SENHA.value
        )
        .first()
    )


    if not token_usuario:
        raise HTTPException(
            status_code=400,
            detail="Token inválido."
        )


    if token_usuario.utilizado:
        raise HTTPException(
            status_code=400,
            detail="Token já utilizado."
        )


    if token_usuario.data_expiracao < datetime.now():
        raise HTTPException(
            status_code=400,
            detail="Token expirado."
        )


    usuario = (
        db.query(Usuario)
        .filter(
            Usuario.id_usuario == token_usuario.id_usuario
        )
        .first()
    )


    if not usuario:
        raise HTTPException(
            status_code=400,
            detail="Usuário não encontrado."
        )


    usuario.senha_hash = gerar_hash(nova_senha)

    token_usuario.utilizado = True


    db.commit()


    return usuario