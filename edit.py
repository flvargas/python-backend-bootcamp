from save import salvar_clientes
from list import listar_cliente

def editar_cliente(clientes):

    id_cliente = int(input("Informe o ID: "))

    for cliente in clientes:

        if cliente['id'] == id_cliente:
    
            print("\n")
            listar_cliente(cliente)            

            print("\n1 - Alterar nome")
            print("2 - Alterar idade")
            print("3 - Alterar status")
            print("4 - Cancelar")

            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
            
                novo_nome = input("Novo nome: ")
                cliente["nome"] = novo_nome
            
            elif opcao == 2:                
            
                nova_idade = int(input("Nova idade: "))
                cliente["idade"] = nova_idade
            
            elif opcao ==3:
            
                ativo = input("Cliente ativo? <S/N>: ").strip().upper()
                cliente["ativo"] = ativo == "S"
            
            elif opcao == 4:
            
                return
            
            salvar_clientes(clientes)

            print("Cliente atualizado!")

            return
        
    print("Cliente não encontrado.")