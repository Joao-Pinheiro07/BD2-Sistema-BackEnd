from postgreConnection import query, mutation
from pydantic import BaseModel

class Cliente(BaseModel):
    cpf: str
    celular: str
    endereco: str
    nome: str
    sobrenome: str

def get_clientes():
    clientes = query("SELECT * FROM CLIENTE;")
    return clientes

def insert_cliente(cliente: Cliente):
    response = mutation(f'INSERT INTO CLIENTE (CPF_CLIENTE, CELULAR, ENDERECO_ID, NOME_CLI, SOBRENOME_CLI) values (\'{cliente.cpf}\',\'{cliente.celular}\',{cliente.endereco},\'{cliente.nome}\', \'{cliente.sobrenome}\');')
    return response

def delete_cliente(cliente_id: int):
    response = mutation(f'DELETE FROM CLIENTE c WHERE c.CLIENTE_ID = {cliente_id};')
    return response