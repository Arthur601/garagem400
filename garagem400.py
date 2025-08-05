opcao = 7
while opcao != 0:
    opcao = int(input("Escolha uma opção: \n1. Cadastrar produto👜\n2. Ver lista de compras📄\n3. Atualizar lista de compras📱\n4. Deletar item da lista❌ \n5. limpar lista de compras🧹\n6. para encerrar o programa🔙\n"))
    lista_de_compras = []
    if opcao == 1:
        item = input("Digite o produto que deseja adicionar: \n")
        lista_de_compras.append(item)
        print(f"Produto adicionado com sucesso!👌 {item}")
    elif opcao == 2:
        print("Lista de compras atual:")
        if lista_de_compras:
            for i, item in enumerate(lista_de_compras, start=1):
                print(f"{i}. {item}")
    elif opcao == 3:
        item = input("Digite o produto que deseja atualizar: \n")
        if lista_de_compras:
            if item in lista_de_compras:
                novo_item = input("Digite o novo produto: \n")
                index = lista_de_compras.index(item)
                lista_de_compras[index] = novo_item
                print(f"Produto atualizado com sucesso!👍 {novo_item}")
            else:
                print("Produto não encontrado na lista.")
    elif opcao == 4:
        item = input("Digite o produto que deseja deletar: \n")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f"Produto {item} deletado com sucesso!❌")
        else:
            print("Produto não encontrado na lista.")
    elif opcao == 5:
        lista_de_compras.clear()
        print("Lista de compras limpa com sucesso!🧹")
    elif opcao.lower() == 6:
        print("Encerrando o programa...🔙")
        break
    else:
        print("Opção inválida, tente novamente.❌")