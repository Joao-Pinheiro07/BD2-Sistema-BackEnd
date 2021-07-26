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
