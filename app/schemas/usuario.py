from pydantic import BaseModel, EmailStr
from fastapi.security import OAuth2PasswordRequestForm


class UsuarioCriacao(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str

class UsuarioAtualizacao(BaseModel):
    nome: str
    email: EmailStr

class RedefinirSenha(BaseModel):
    token: str
    nova_senha: str

