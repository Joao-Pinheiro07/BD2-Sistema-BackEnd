from typing import Optional
from fastapi import FastAPI
from carroService import Carro, deleteCarro, getCarros, insertCarro
from clienteService import Cliente, delete_cliente, get_clientes, insert_cliente
from enderecoService import Endereco, deleteEnderecos, getEnderecos, insertEnderecos
from entregaService import Entrega, deleteEntrega, getEntrega, insertEntrega
from fornecedorService import Fornecedor, deleteFornecedor, getFornecedor, insertFornecedor
from fornecimentoService import Fornecimento, delete_fornecimento, get_fornecimento, insert_fornecimento
from fraquiaService import get_franquias
from funcionarioService import Funcionario, deleteFunc, getFuncionarios, insertFuncionario
from secaoService import get_all_secoes
from produtoService import Produto, add_produto_na_venda, get_produtos_by_secao, get_produtos_nao_vendidos, get_produtos_vendidos, insertProduto
from promocaoService import get_all_promo, insert_promo, Promocao, delete_promo
from fastapi.middleware.cors import CORSMiddleware

from vendaService import Venda, insert_venda

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{entidade}")
def get_entidade(entidade: str):
    if entidade == "carro":
        return getCarros()
    elif entidade == "cliente":
        return get_clientes()
    elif entidade == "endereco":
        return getEnderecos()
    elif entidade == "entrega":
        return getEntrega()
    elif entidade == "fornecedor":
        return getFornecedor()
    elif entidade == "fornecimento":
        return get_fornecimento()
    elif entidade == "franquia":
        return get_franquias()
    elif entidade == "funcionario":
        return getFuncionarios()
    elif entidade == "promocao":
        return get_all_promo()
    elif entidade == "secao":
        return get_all_secoes()
    elif entidade == "venda":
        return getFuncionarios()

@app.delete("/{entidade}/{item_id}")
def get_entidade(entidade: str, item_id):
    if entidade == "carro":
        return deleteCarro(item_id)
    elif entidade == "cliente":
        return delete_cliente(item_id)
    elif entidade == "endereco":
        return deleteEnderecos(item_id)
    elif entidade == "entrega":
        return deleteEntrega(item_id)
    elif entidade == "fornecedor":
        return deleteFornecedor(item_id)
    elif entidade == "fornecimento":
        return delete_fornecimento(item_id)
    elif entidade == "funcionario":
        return deleteFunc(item_id)
    elif entidade == "promocao":
        return delete_promo(item_id)

@app.post("/insert/carro")
def newCarro(carro: Carro):
    return insertCarro(carro)

@app.post("/insert/cliente")
def new_cliente(cliente: Cliente):
    return insert_cliente(cliente)

@app.post("/insert/endereco")
def new_endereco(endereco: Endereco):
    return insertEnderecos(endereco)

@app.post("/insert/entrega")
def new_entrega(entrega: Entrega):
    return insertEntrega(entrega)

@app.post("/insert/fornecedor")
def new_fornecedor(fornecedor: Fornecedor):
    return insertFornecedor(fornecedor)

@app.post("/insert/fornecimento")
def new_fornecimento(fornecimento: Fornecimento):
    return insert_fornecimento(fornecimento)

@app.post("/insert/funcionario")
def new_funcionario(funcionario: Funcionario):
    return insertFuncionario(funcionario)

@app.post("/insert/funcionario")
def new_funcionario(funcionario: Funcionario):
    return insertFuncionario(funcionario)

@app.post("/insert/produto")
def new_produto(produto: Produto):
    return insertProduto(produto)

@app.post("/insert/promocao")
def new_promo(promocao: Promocao):
    return insert_promo(promocao)

@app.post("/insert/venda")
def new_venda(venda: Venda):
    return insert_venda(venda)

@app.get("/produto/{secao_id}")
def get_produto(secao_id: int):
    return get_produtos_by_secao(secao_id)

@app.get("/produto/vendidos")
def get_vendidos():
    return get_produtos_vendidos()

@app.get("/produto/nao-vendidos")
def get_nao_vendidos():
    return get_produtos_nao_vendidos()

@app.put("/venda/add-produto/{prod_id}")
def add_prod_venda(prod_id: int):
    return add_produto_na_venda(prod_id)

