from postgreConnection import query, mutation
from pydantic import BaseModel

class Carro(BaseModel):
    franquia_id: int
    placa: str
    modelo: str
    ano: int
    marca: str

def getCarros():
    carros = query("SELECT * FROM CARRO;")
    return carros

def insertCarro(carro: Carro):
    response = mutation(f'INSERT INTO CARRO (FRANQUIA_ID, PLACA, MODELO, ANO, MARCA_CARRO) values ({carro.franquia_id}, \'{carro.placa}\', \'{carro.modelo}\', {carro.ano}, \'{carro.marca}\');')
    return response

def deleteCarro(carro_id: int):
    response = mutation(f'DELETE FROM CARRO c WHERE c.CARRO_ID = {carro_id};')
    return response
