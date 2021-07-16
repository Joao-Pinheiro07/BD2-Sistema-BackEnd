from postgreConnection import query, mutation
from pydantic import BaseModel

class Gerente(BaseModel):
    id: int
    email: str
    cpf: str
    nome: str
    sobrenome: str

def getAllGerentes():    
    gerentes = query("SELECT * FROM GERENTE")    
    return gerentes

def insertGerente(gerente: Gerente):
    mutation(f'INSERT INTO GERENTE (GERENTE_ID, EMAIL, CPF_GERENTE, NOME_GER, SOBRENOME_GER) values ({gerente.id},\'{gerente.email}\',\'{gerente.cpf}\',\'{gerente.nome}\',\'{gerente.sobrenome}\');')
    return
