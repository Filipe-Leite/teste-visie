from fastapi import FastAPI
from . import models
from .database import engine
from .routers import pessoa

app = FastAPI(
    title="Teste Visie",
    description="Este é um teste de recrutamento Full-stack",
)

app.include_router(pessoa.router)

models.Base.metadata.create_all(engine)