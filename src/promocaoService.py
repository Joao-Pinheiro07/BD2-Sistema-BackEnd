from postgreConnection import query, mutation
from pydantic import BaseModel

class Promocao(BaseModel):
    porcentagem: int
    secaoId: int

def get_all_promo():
    promos = query("SELECT * FROM PROMOCAO;")
    return promos

def insert_promo(promocao: Promocao):
    response = mutation(f'insert into PROMOCAO (porcentagem, secao_id) values ({promocao.porcentagem}, {promocao.secaoId});')
    return response

def delete_promo(promoId: int):
    response = mutation(f'DELETE FROM PROMOCAO p WHERE p.promocao_id = {promoId};')
    return response