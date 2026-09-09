from pydantic import BaseModel, EmailStr


class ContatoRequest(BaseModel):
    nome: str
    email: EmailStr
    telefone: str | None = None
    mensagem: str