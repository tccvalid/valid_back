import random
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.models.token_usuario import TokenUsuario
from app.enums.tipo_token import TipoToken

from fastapi import HTTPException, status

from app.utils.seguranca import criar_access_token


def gerar_codigo():
    return str(random.randint(100000, 999999))


def criar_token_2fa(db: Session, usuario: Usuario):
    codigo = gerar_codigo()

    tokens_antigos = (
        db.query(TokenUsuario)
        .filter(
            TokenUsuario.id_usuario == usuario.id_usuario,
            TokenUsuario.tipo_token == TipoToken.DOIS_FATORES,
            TokenUsuario.utilizado == False
        )
        .all()
    )

    for token in tokens_antigos:
        token.utilizado = True

    novo_token = TokenUsuario(
        id_usuario=usuario.id_usuario,
        token=codigo,
        tipo_token=TipoToken.DOIS_FATORES,
        utilizado=False,
        data_criacao=datetime.now(),
        data_expiracao=datetime.now() + timedelta(minutes=10)
    )

    db.add(novo_token)
    db.commit()

    enviar_codigo_2fa(usuario, codigo)

    return codigo

def verificar_codigo_2fa(
    db: Session,
    email: str,
    codigo: str
):

    usuario = (
        db.query(Usuario)
        .filter(
            Usuario.email.ilike(email.strip())
        )
        .first()
    )

    print("EMAIL RECEBIDO:", email)

    todos = db.query(Usuario).all()

    for u in todos:
        print("EMAIL BANCO:", u.email)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado."
        )

    token = (
        db.query(TokenUsuario)
        .filter(
            TokenUsuario.id_usuario == usuario.id_usuario,
            TokenUsuario.tipo_token == TipoToken.DOIS_FATORES,
            TokenUsuario.token == codigo,
            TokenUsuario.utilizado == False
        )
        .first()
    )

    if not token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Código inválido."
        )

    if token.data_expiracao < datetime.now():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Código expirado."
        )

    token.utilizado = True

    db.commit()

    access_token = criar_access_token(
        {
            "sub": str(usuario.id_usuario)
        }
    )

    return access_token

from app.services.email import enviar_email

def enviar_codigo_2fa(usuario: Usuario, codigo: str):

    assunto = "Código de verificação - VALID"

    mensagem = f"""
        Olá, {usuario.nome}!

        Recebemos uma solicitação de login na sua conta da plataforma VALID.

        Código de verificação:

        {codigo}

        ⚠ Este código é válido por apenas 10 minutos.

        Caso você não tenha feito esta solicitação, desconsidere este e-mail.

        Equipe VALID
        """

    enviar_email(
        destinatario=usuario.email,
        assunto=assunto,
        mensagem=mensagem
    )
