from datetime import datetime

from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database import Base


class TokenUsuario(Base):

    __tablename__ = "token_usuario"

    id_token: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuario.id_usuario"),
        nullable=False
    )

    token: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    tipo_token: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    utilizado: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    data_criacao: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    data_expiracao: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    usuario = relationship(
        "Usuario",
        back_populates="tokens"
    )