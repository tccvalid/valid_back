from pydantic import BaseModel


class Verificar2FARequest(BaseModel):
    email: str
    codigo: str


class Reenviar2FARequest(BaseModel):
    email: str


class Atualizar2FARequest(BaseModel):
    ativo: bool