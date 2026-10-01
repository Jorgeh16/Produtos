from Produtos import Produtos

def menu():
    print()
    print("1 - Listar Produto")
    print("2 - Insserir Produto")
    print("3 - Alterar Produto")
    print("4 - Excluir Produto")
    print("0 - Sair")
    print()
    
    opcao = 1
    
    while opcao != 0:
        opcao = int(input("Escolha uma opção:"))
        
        match opcao:
            case 1:
                print("***************************************")
                Produtos.listarTodos()
                print("***************************************")
                
            case 2:
                codigo = input("Digite o código: ")
                nome = input("Digite o nome: ")
                quantidade = input("Digite quantidade: ")
                valor = float(input("Digite o valor: ").replace(',', '.'))
                
                produto = Produtos(codigo, nome, quantidade, valor)
                produto.inserir()
            case 3:
                Produtos.listarTodos()
                selecionado = int(input("Qual item deseja alterar"))
                item = Produtos.consultar(selecionado)

                if item:
                    quantidade = int(input("Qual  a nova Quantidade"))
                    valor = float(input("Qual o novo Valor").replace(',', '.'))

                    produto = Produtos(item["codigo"], item["nome"], quantidade, valor)
                    produto.alterar(selecionado)
                else:
                    print("Produto não encontrado")
                
            case 4:
                Produtos.listarTodos()
                selecionado = int(input("Qual item deseja excluir"))
                item = Produtos.consultar(selecionado)

                if item:
                    produto = Produtos(item["codigo"], item["nome"], item["quantidade"], item["valor"])
                    produto.excluir(selecionado)
                else:
                    print("Produto não encontrado")


menu()