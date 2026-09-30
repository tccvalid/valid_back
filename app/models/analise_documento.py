from datetime import datetime, timezone
from sqlalchemy import DateTime, ForeignKey, Integer, Float, String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class AnaliseDocumento(Base):
    __tablename__ = "analise_documento"
    id_analise: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuario.id_usuario", ondelete="CASCADE"), index=True)
    nome_arquivo: Mapped[str] = mapped_column(String(255), nullable=False)
    tamanho_bytes: Mapped[int] = mapped_column(Integer, nullable=False)
    classificacao: Mapped[str] = mapped_column(String(100), nullable=False)
    score_suspeita: Mapped[float | None] = mapped_column(Float, nullable=True)
    resultado: Mapped[dict] = mapped_column(JSON, nullable=False)
    data_analise: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)
