from save import salvar_clientes

def cadastrar_cliente(clientes):

    print("\n===== CADASTRAR =====\n")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    novo_id = len(clientes) + 1
    
    novo_cliente = {
        "id": novo_id,
        "nome": nome,
        "idade": idade,
        "ativo": True 
    }

    clientes.append(novo_cliente)
    salvar_clientes(clientes)

    print("Cliente cadastrado com sucesso!")