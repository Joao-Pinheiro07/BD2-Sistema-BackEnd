from postgreConnection import query, mutation
from pydantic import BaseModel

class Funcionario(BaseModel):
    nome: str
    sobrenome: str
    cargo: str
    supervisor_id: int
    franquia_id: int
    data_admissao: str
    cpf: str

def getFuncionarios():
    return query('SELECT * FROM FUNCIONARIO')

def insertFuncionario(funcionario: Funcionario):
    return mutation(f"INSERT INTO FUNCIONARIO (NOME_FUNC, SOBRENOME_FUNC, CARGO, FRANQUIA_ID, DATA_ADMISSAO, CPF_FUNC) values (\'{funcionario.nome}\', \'{funcionario.sobrenome}\', \'{funcionario.cargo}\', {funcionario.franquia_id}, \'{funcionario.data_admissao}\', \'{funcionario.cpf}\');")

def deleteFunc(funcionario_id: int):
    return mutation(f"DELETE FROM FUNCIONARIO f WHERE f.FUNCIONARIO_ID = {funcionario_id};")