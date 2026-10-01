from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.autenticacao import obter_usuario_atual
from app.models.analise import Analise
from app.models.usuario import Usuario
from app.schemas.analise import AnaliseCriacao


router = APIRouter(
    prefix="/analises",
    tags=["Análises"]
)


def _status_por_classificacao(classificacao: str) -> str:
    texto = (classificacao or "").lower()

    if "alta" in texto:
        return "suspeito"

    return "autentico"


def _formatar_tamanho(bytes_total: int) -> str:
    try:
        tamanho = int(bytes_total or 0)
    except (TypeError, ValueError):
        tamanho = 0

    if tamanho < 1024:
        return f"{tamanho} B"

    if tamanho < 1024 * 1024:
        return f"{tamanho / 1024:.1f} KB"

    return f"{tamanho / (1024 * 1024):.1f} MB"


@router.post("/")
def criar_analise(
    dados: AnaliseCriacao,
    usuario: Usuario = Depends(obter_usuario_atual),
    db: Session = Depends(get_db)
):
    analise_global = dados.resultado.get("analise_global") or {}

    classificacao = str(
        analise_global.get(
            "classification",
            "Não identificada"
        )
    )

    try:
        score = float(
            analise_global.get(
                "combined_score",
                0
            ) or 0
        )
    except (TypeError, ValueError):
        score = 0.0

    registro = Analise(
        id_usuario=usuario.id_usuario,
        nome_arquivo=dados.nome_arquivo,
        tamanho_bytes=dados.tamanho_bytes,
        resultado=dados.resultado,
        classificacao=classificacao,
        score_suspeita=score,
        status=_status_por_classificacao(classificacao)
    )

    db.add(registro)
    db.commit()
    db.refresh(registro)

    return {
        "mensagem": "Análise salva no histórico.",
        "id": registro.id_analise
    }


@router.get("/")
def listar_analises(
    usuario: Usuario = Depends(obter_usuario_atual),
    db: Session = Depends(get_db)
):
    registros = (
        db.query(Analise)
        .filter(Analise.id_usuario == usuario.id_usuario)
        .order_by(Analise.data_analise.desc())
        .all()
    )

    return [
        {
            "id": item.id_analise,
            "nome": item.nome_arquivo,
            "tamanho": _formatar_tamanho(item.tamanho_bytes),
            "data": item.data_analise.strftime("%d/%m/%Y"),
            "hora": item.data_analise.strftime("%H:%M"),
            "status": item.status,
            "classificacao": item.classificacao,
            "score_suspeita": round(float(item.score_suspeita or 0), 2),
            "resultado": item.resultado
        }
        for item in registros
    ]


@router.get("/resumo")
def resumo_analises(
    usuario: Usuario = Depends(obter_usuario_atual),
    db: Session = Depends(get_db)
):
    query = db.query(Analise).filter(
        Analise.id_usuario == usuario.id_usuario
    )

    total = query.count()

    ultima = (
        query
        .order_by(Analise.data_analise.desc())
        .first()
    )

    media = (
        db.query(func.avg(Analise.score_suspeita))
        .filter(Analise.id_usuario == usuario.id_usuario)
        .scalar()
    )

    historico = (
        query
        .order_by(Analise.data_analise.desc())
        .limit(10)
        .all()
    )

    return {
        "documentos": total,
        "ultimaHora": (
            ultima.data_analise.strftime("%d/%m/%Y às %H:%M")
            if ultima
            else "Nenhuma"
        ),
        "ultimoArquivo": (
            ultima.nome_arquivo
            if ultima
            else "Sem análises"
        ),
        "taxa": (
            f"{float(media):.1f}%"
            if media is not None
            else "—"
        ),
        "historico": [
            {
                "id": item.id_analise,
                "nome": item.nome_arquivo,
                "tamanho": _formatar_tamanho(item.tamanho_bytes),
                "data": item.data_analise.strftime("%d/%m/%Y"),
                "hora": item.data_analise.strftime("%H:%M"),
                "status": item.status,
                "classificacao": item.classificacao,
                "score_suspeita": round(float(item.score_suspeita or 0), 2)
            }
            for item in historico
        ]
    }
