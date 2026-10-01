from sqlalchemy import BigInteger, DateTime, Float, ForeignKey, JSON, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.database import Base


class Analise(Base):
    __tablename__ = "analise"

    id_analise: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuario.id_usuario", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    nome_arquivo: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    tamanho_bytes: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
        default=0
    )

    resultado: Mapped[dict] = mapped_column(
        JSON,
        nullable=False
    )

    classificacao: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="Não identificada"
    )

    score_suspeita: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.0
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="autentico"
    )

    data_analise: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )
