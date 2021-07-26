from postgreConnection import query, mutation
from pydantic import BaseModel

class Fornecimento(BaseModel):
    franquia_id: int
    fornecedor_id: int
    data: str

def get_fornecimento():
    return query("SELECT * FROM FORNECIMENTO;")

def insert_fornecimento(forncimento: Fornecimento):
    return mutation(f'INSERT INTO FORNECIMENTO (FRANQUIA_ID, FORNECEDOR_ID, DATA_FORN) values ({forncimento.franquia}, {forncimento.fornecedor}, \'{forncimento.data}\');')

def delete_fornecimento(fornecimento_id: int):
    return mutation(f'DELETE FROM FORNECIMENTO f WHERE f.FORNECIMENTO_ID = {fornecimento_id};')