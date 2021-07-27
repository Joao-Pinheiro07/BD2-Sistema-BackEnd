from typing import List
from funcionarioService import Funcionario
from postgreConnection import query, mutation
from pydantic import BaseModel

class Venda(BaseModel):
    funcionario_id: int
    fraquia_id: int
    cliente_id: int
    caixa: str
    valor: str
    data: str
    parcelas: int

def get_vendas():
    return query("SELECT * FROM VENDA;")

def insert_venda(venda: Venda):
    return mutation(f'INSERT INTO VENDA (FUNCIONARIO_ID, FRANQUIA_ID, CLIENTE_ID, CAIXA, VALOR, DATA_VENDA, PARCELAS) values ({venda.funcionario_id}, {venda.franquia_id}, {venda.cliente_id}, \'{venda.caixa}\', \'{venda.valor}\', \'{venda.data}\', {venda.parcelas});')
