from postgreConnection import query, mutation
from pydantic import BaseModel

class Franquia(BaseModel):
   gerente_id: int
   endereco_id: int
   unidade: str

def get_franquias():
    return query('SELECT * FROM FRANQUIA;')