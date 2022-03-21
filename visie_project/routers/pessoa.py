from fastapi import APIRouter,status, Response, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas
from typing import List

router = APIRouter(
    tags=['Pessoa'],
    prefix= '/pessoa'
)


@router.post('/')
def add(request: schemas.Pessoa, db: Session = Depends(get_db)):

    nova_pessoa = models.Pessoa(nome =  request.nome,
                                rg=request.rg,
                                cpf=request.cpf,
                                data_nascimento=request.data_nascimento,
                                data_admissao=request.data_admissao,
                                funcao=request.funcao)
    db.add(nova_pessoa)
    db.commit()
    db.refresh(nova_pessoa)
    return nova_pessoa

@router.get('/')
def pessoas(db: Session = Depends(get_db)):
    pessoas = db.query(models.Pessoa).all()
    return pessoas

@router.get('/{id}')
def pessoa(id, response: Response, db: Session = Depends(get_db)):
    pessoa = db.query(models.Pessoa).filter(models.Pessoa.id == id).first()
    if not pessoa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Pessoa não existente')
    return pessoa

@router.put('/{id}')
def update(id, request: schemas.Pessoa, db: Session = Depends(get_db)):
    pessoa = db.query(models.Pessoa).filter(models.Pessoa.id == id)
    if not pessoa.first():
        pass
    pessoa.update(request.dict())
    db.commit()
    return {'Dados da pessoa reformulados'}

@router.delete('/{id}')
def delete(id, db: Session = Depends(get_db)):
    db.query(models.Pessoa).filter(models.Pessoa.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Pessoa deletada'}