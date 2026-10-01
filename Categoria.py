from pathlib import Path
from AbstractCrud import AbstractCrud

class Categoria(AbstractCrud):
    
    arquivo = Path(__file__).resolve().parent.parent / 'db' / 'categorias.json'
    
    def __init__(self,  nome):
        self.nome = nome
        
