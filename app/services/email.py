import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD


def enviar_email(
    destinatario: str,
    assunto: str,
    mensagem: str
):
    email = MIMEMultipart()

    email["From"] = EMAIL_USER
    email["To"] = destinatario
    email["Subject"] = assunto

    email.attach(
        MIMEText(
            mensagem,
            "plain"
        )
    )

    servidor = smtplib.SMTP(
        EMAIL_HOST,
        EMAIL_PORT
    )

    servidor.starttls()

    servidor.login(
        EMAIL_USER,
        EMAIL_PASSWORD
    )

    servidor.send_message(email)

    servidor.quit()


