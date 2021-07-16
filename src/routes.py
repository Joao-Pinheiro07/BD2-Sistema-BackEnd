from typing import Optional
from fastapi import FastAPI
from gerenteService import getAllGerentes, insertGerente
from gerenteService import Gerente
app = FastAPI()


@app.get("/gerente")
def read_item():
    return getAllGerentes()

@app.post("/gerente/")
def create_gerente(gerente: Gerente):
    return insertGerente(gerente)