from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database import Base


class Usuario(Base):

    __tablename__ = "usuario"

    id_usuario: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    nome: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    senha_hash: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    google_id: Mapped[str | None] = mapped_column(
        String(255),
        unique=True,
        nullable=True
    )

    email_verificado: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    dois_fatores_ativo: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    data_cadastro: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    ultimo_login: Mapped[DateTime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    tokens = relationship(
        "TokenUsuario",
        back_populates="usuario"
    )