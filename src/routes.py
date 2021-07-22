from typing import Optional
from fastapi import FastAPI
from secaoService import get_all_secoes
from produtoService import get_produtos_by_secao
from promocaoService import get_all_promo, insert_promo, Promocao, delete_promo
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/secao")
def get_secao():
    return get_all_secoes()

@app.get("/produto/{secao_id}")
def get_produto(secao_id: int):
    return get_produtos_by_secao(secao_id)

@app.get("/promocao")
def get_all_promos():
    return get_all_promo()

@app.post("/promocao")
def new_promo(promocao: Promocao):
    return insert_promo(promocao)

@app.delete("/promocao/{promoId}")
def del_promo(promo_id: int):
    return delete_promo(promo_id)



