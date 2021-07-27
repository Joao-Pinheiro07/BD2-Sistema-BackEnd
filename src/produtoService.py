from postgreConnection import query, mutation
from pydantic import BaseModel

class Produto(BaseModel):
    secao_id: int
    franquia_id: int
    fornecimento_id: int
    marca: str
    preco: str
    nome: str

def get_produtos_by_secao(secaoId: int):
    produtos = query(f'SELECT p.nome_produto, p.preco_unitario, p.marca_produto, s.nome_sec\
     FROM PRODUTO p INNER JOIN SECAO s ON p.secao_id = s.secao_id\
     WHERE s.secao_id = {secaoId};')

    return produtos

def get_produtos_vendidos():
    return query("SELECT p.*, s.nome_sec FROM PRODUTO p INNER JOIN SECAO s ON p.secao_id = s.secao_id WHERE p.VENDA_ID IS NOT NULL;")

def get_produtos_nao_vendidos():
    return query("SELECT p.*, s.nome_sec FROM PRODUTO p INNER JOIN SECAO s ON p.secao_id = s.secao_id WHERE p.VENDA_ID IS NULL;")

def insertProduto(produto: Produto):
    return mutation(f'INSERT INTO PRODUTO(SECAO_ID, FRANQUIA_ID, FORNECIMENTO_ID, MARCA_PRODUTO, PRECO_UNITARIO, NOME_PRODUTO) values ({produto.secao_id}, {produto.franquia_id}, {produto.fornecimento_id}, \'{produto.marca}\', \'{produto.preco}\', \'{produto.nome}\');')

def add_produto_na_venda(produto_id: int, venda_id: int):
    return mutation(f'UPDATE PRODUTO SET VENDA_ID = {venda_id} WHERE PRODUTO_ID = {produto_id};')

def deleteProduto(produto_id: int):
    return mutation(f'DELETE FROM PRODUTO p WHERE p.PRODUTO_ID = {produto_id};')