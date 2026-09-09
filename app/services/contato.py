from app.schemas.contato import ContatoRequest
from app.services.email import enviar_email

print(enviar_email.__module__)

def enviar_contato(dados: ContatoRequest):

    assunto = f"Novo contato - {dados.nome}"

    corpo = f"""
Novo contato recebido pelo site VALID

Nome:
{dados.nome}

Email:
{dados.email}

Telefone:
{dados.telefone or "Não informado"}

Mensagem:

{dados.mensagem}
"""

    enviar_email(
        destinatario="tccvalid@gmail.com",
        assunto=assunto,
        mensagem=corpo
    )