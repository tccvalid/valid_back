from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies.autenticacao import obter_usuario_atual
from app.models.usuario import Usuario
from app.models.analise_documento import AnaliseDocumento
from app.schemas.analise_documento import CriarAnalise

router = APIRouter(prefix="/analises", tags=["Análises"])

def resumo(a):
    return {"id": a.id_analise, "nome": a.nome_arquivo, "tamanho_bytes": a.tamanho_bytes,
            "classificacao": a.classificacao, "score_suspeita": a.score_suspeita,
            "data_analise": a.data_analise}

@router.post("/", status_code=status.HTTP_201_CREATED)
def salvar_analise(dados: CriarAnalise, usuario: Usuario = Depends(obter_usuario_atual),
                   db: Session = Depends(get_db)):
    info = dados.resultado.get("analise_global")
    if not isinstance(info, dict):
        raise HTTPException(status_code=422, detail="Resultado da análise inválido")
    classificacao = str(info.get("classification") or "Não identificada")[:100]
    raw = info.get("combined_score")
    try:
        score = float(raw) if raw is not None else None
    except (ValueError, TypeError):
        raise HTTPException(status_code=422, detail="Score inválido")
    if score is not None and not 0 <= score <= 100:
        raise HTTPException(status_code=422, detail="Score fora da escala")
    a = AnaliseDocumento(id_usuario=usuario.id_usuario, nome_arquivo=dados.nome_arquivo,
        tamanho_bytes=dados.tamanho_bytes, classificacao=classificacao,
        score_suspeita=score, resultado=dados.resultado)
    db.add(a)
    db.commit()
    db.refresh(a)
    return resumo(a)

@router.get("/")
def listar_analises(limite: int = 10, deslocamento: int = 0,
                    usuario: Usuario = Depends(obter_usuario_atual), db: Session = Depends(get_db)):
    limite = max(1, min(limite, 100))
    deslocamento = max(0, deslocamento)
    q = db.query(AnaliseDocumento).filter(AnaliseDocumento.id_usuario == usuario.id_usuario)
    return {"total": q.count(), "itens": [resumo(a) for a in q.order_by(
        AnaliseDocumento.data_analise.desc(), AnaliseDocumento.id_analise.desc()
    ).offset(deslocamento).limit(limite).all()]}

@router.get("/estatisticas")
def estatisticas(usuario: Usuario = Depends(obter_usuario_atual), db: Session = Depends(get_db)):
    q = db.query(AnaliseDocumento).filter(AnaliseDocumento.id_usuario == usuario.id_usuario)
    ultima = q.order_by(AnaliseDocumento.data_analise.desc(), AnaliseDocumento.id_analise.desc()).first()
    media = db.query(func.avg(AnaliseDocumento.score_suspeita)).filter(
        AnaliseDocumento.id_usuario == usuario.id_usuario).scalar()
    return {"documentos": q.count(), "ultima_analise": resumo(ultima) if ultima else None,
            "score_medio_suspeita": round(float(media), 1) if media is not None else None}

@router.get("/{id_analise}")
def detalhe(id_analise: int, usuario: Usuario = Depends(obter_usuario_atual),
            db: Session = Depends(get_db)):
    a = db.query(AnaliseDocumento).filter(AnaliseDocumento.id_analise == id_analise,
        AnaliseDocumento.id_usuario == usuario.id_usuario).first()
    if not a:
        raise HTTPException(status_code=404, detail="Análise não encontrada")
    return {**resumo(a), "resultado": a.resultado}
