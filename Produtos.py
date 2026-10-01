from pathlib import Path
from AbstractCrud import AbstractCrud


class Produtos(AbstractCrud):
    arquivo = Path(__file__).resolve().parent.parent / 'db' / 'produtos.json'

    def __init__(self, codigo, nome, quantidade, valor):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        
    def inserir(self):
        lista = self.consultar()
        produtoDuplicado = filter(lambda p: p['codigo'] == self.codigo, lista)
        
        if len(list(produtoDuplicado)):
            print()
            print("Já existe um produto com esse código")
        else:
            super().inserir()