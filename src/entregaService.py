from postgreConnection import query, mutation
from pydantic import BaseModel

class Entrega(BaseModel):
    carro_id: int
    venda_id: int
    endereco_id: int
    funcionario_id: int
    date: str

def getEntrega():
    entregas = query("SELECT * FROM ENTREGA;")
    return entregas

def insertEntrega(entrega: Entrega):
    response = mutation(f'INSERT INTO ENTREGA (CARRO_ID, VENDA_ID, ENDERECO_ID, FUNCIONARIO_ID, DATA_ENTREGA) values ({entrega.carro_id}, {entrega.venda_id}, {entrega.endereco_id}, {entrega.funcionario_id}, {entrega.date});')
    return response

def deleteCarro(entrega_id: int):
    response = mutation(f'DELETE FROM ENTREGA e WHERE e.ENTREGA_ID = {entrega_id};')
    return response
