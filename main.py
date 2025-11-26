import os
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# 1. Configuração do Banco de Dados
# Pega a URL da variável de ambiente (definida no docker-compose)
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. Modelo da Tabela (SQLAlchemy) - O que vai pro Banco
class ProdutoModel(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    preco = Column(Float)

# 3. Cria as tabelas automaticamente ao iniciar
Base.metadata.create_all(bind=engine)

# 4. Schemas (Pydantic) - O que a API recebe/envia
class ProdutoSchema(BaseModel):
    nome: str
    preco: float

class ProdutoResponse(ProdutoSchema):
    id: int
    class Config:
        orm_mode = True

# 5. Dependência para pegar a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="Minicurso DevOps - Com Postgres")

@app.get("/")
def read_root():
    return {"message": "API rodando com Postgres!"}

@app.post("/produtos", response_model=ProdutoResponse)
def criar_produto(produto: ProdutoSchema, db: Session = Depends(get_db)):
    # Cria o objeto do modelo
    novo_produto = ProdutoModel(nome=produto.nome, preco=produto.preco)
    # Adiciona e salva no banco
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

@app.get("/produtos", response_model=List[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(ProdutoModel).all()

@app.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoModel).filter(ProdutoModel.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    db.delete(produto)
    db.commit()
    return {"message": "Produto removido com sucesso"}