from pydantic import BaseModel, Field
class CriarAnalise(BaseModel):
    nome_arquivo: str = Field(min_length=1, max_length=255)
    tamanho_bytes: int = Field(ge=0)
    resultado: dict
