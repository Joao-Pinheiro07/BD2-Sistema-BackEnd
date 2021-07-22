from postgreConnection import query

def get_produtos_by_secao(secaoId: int):
    produtos = query(f'SELECT p.nome_produto, p.preco_unitario, p.marca_produto, s.nome_sec\
     FROM PRODUTO p INNER JOIN SECAO s ON p.secao_id = s.secao_id\
     WHERE s.secao_id = {secaoId};')

    return produtos