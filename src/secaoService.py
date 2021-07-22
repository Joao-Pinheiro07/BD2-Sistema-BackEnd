from postgreConnection import query

def get_all_secoes():
    secoes = query("SELECT s.secao_id, s.nome_sec, array_agg(p.produto_id) as produtos\
                    FROM SECAO s INNER JOIN produto p ON p.secao_id = s.secao_id\
                    GROUP BY s.secao_id, s.nome_sec;")
    return secoes
