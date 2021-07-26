from postgreConnection import query, mutation
from pydantic import BaseModel

class Fornecedor(BaseModel):
    nome: str
    cnpj: str
    email: str

def getFornecedor():
    fornecedores = query("SELECT * FROM FORNECEDOR;")
    return fornecedores

def insertFornecedor(fornecedor: Fornecedor):
    response = mutation(f'INSERT INTO FORNCEDOR (NOME_FORN, CNPJ_FORNECEDOR, EMAIL_FORNECEDOR) values (\'{fornecedor.nome}\', \'{fornecedor.cnpj}\', \'{fornecedor.email}\');')
    return response

def deleteFornecedor(forn_id: int):
    return mutation(f'DELETE FROM FORNECEDOR f WHERE f.FORNECEDOR_ID = {forn_id};')