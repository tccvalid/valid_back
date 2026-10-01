from typing import Any

from pydantic import BaseModel


class AnaliseCriacao(BaseModel):
    nome_arquivo: str
    tamanho_bytes: int = 0
    resultado: dict[str, Any]
