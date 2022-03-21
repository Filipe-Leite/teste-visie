from pydantic import BaseModel

class Pessoa(BaseModel):
    nome: str
    rg: str
    cpf: str
    data_nascimento: str
    data_admissao: str
    funcao: str

    class Config:
        orm_mode = True