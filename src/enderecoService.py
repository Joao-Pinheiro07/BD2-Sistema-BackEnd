from postgreConnection import query, mutation
from pydantic import BaseModel

class Endereco(BaseModel):
    rua: str
    bairro: str
    cidade: str
    estado: str
    cep: str

def getEnderecos():
    enderecos = query("SELECT * FROM ENDERECO;")
    return enderecos

def insertEnderecos(endereco: Endereco):
    response = mutation(f'insert into endereco(rua, bairro, cidade, estado, cep) values (\'{endereco.rua}\', \'{endereco.bairro}\', \'{endereco.cidade}\', \'{endereco.estado}\', \'{endereco.cep}\');')
    return response

def deleteEnderecos(endereco_id: int):
    response = mutation(f'DELETE FROM ENDERECO c WHERE c.ENDERECO_ID = {endereco_id};')
    return response
