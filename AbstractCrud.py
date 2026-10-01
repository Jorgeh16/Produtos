import json
from pathlib import Path


class AbstractCrud:
    arquivo = Path(__file__).resolve().parent.parent / 'db' / 'produtos.json'

    def detalhar(self):
        return self.__dict__

    def gravarArquivo(self, lista):
        self.arquivo.parent.mkdir(exist_ok=True)
        with self.arquivo.open('w') as file:
            json.dump(lista, file, indent=4)

    def inserir(self):
        lista = self.consultar()
        novo = self.detalhar()

        for i, registro in enumerate(lista):
            if registro.get('codigo') == novo.get('codigo'):
                lista[i] = novo
                self.gravarArquivo(lista)
                print('Registro alterado com sucesso')
                return

        lista.append(novo)
        self.gravarArquivo(lista)
        print('Registro cadastrado com sucesso')

    def alterar(self, valor):
        lista = self.consultar()

        if isinstance(valor, int):
            if valor < 0 or valor >= len(lista):
                print('Produto não encontrado')
                return
            lista[valor] = self.detalhar()
        else:
            for i, registro in enumerate(lista):
                if registro.get('codigo') == valor:
                    lista[i] = self.detalhar()
                    break
            else:
                print('Produto não encontrado')
                return

        self.gravarArquivo(lista)
        print('Registro alterado com sucesso')

    def excluir(self, valor):
        lista = self.consultar()

        if isinstance(valor, int):
            if valor < 0 or valor >= len(lista):
                print('Produto não encontrado')
                return
            del lista[valor]
        else:
            nova_lista = []
            for registro in lista:
                if registro.get('codigo') != valor:
                    nova_lista.append(registro)
            if len(nova_lista) == len(lista):
                print('Produto não encontrado')
                return
            lista = nova_lista

        self.gravarArquivo(lista)
        print('Registro excluído com sucesso')

    @classmethod
    def listarTodos(cls):
        lista = cls.consultar()

        for i, p in enumerate(lista):
            print(f'{i} - {p}')

    @classmethod
    def consultar(cls, item=None):
        try:
            with cls.arquivo.open() as file:
                lista = json.load(file)

                if item is None:
                    return lista

                if isinstance(item, int):
                    return lista[item]

                for registro in lista:
                    if registro.get('codigo') == item:
                        return registro

                return None
        except Exception:
            return []

    @classmethod
    def buscarPorCodigo(cls, codigo):
        return cls.consultar(codigo)