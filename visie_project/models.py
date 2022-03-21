from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100),nullable=False)
    rg = Column(String(100),nullable=False)
    cpf = Column(String(100),nullable=False)
    data_nascimento = Column(String(10))
    data_admissao = Column(String(10))
    funcao = Column(String(100))