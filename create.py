from save import salvar_clientes

def gerar_novo_id(clientes):

    maior_id = 0

    for cliente in clientes:

        if cliente["id"] > maior_id:

            maior_id = cliente["id"]

    novo_id = maior_id + 1

    return novo_id

def cadastrar_cliente(clientes):

    print("\n===== CADASTRAR =====\n")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    novo_id = gerar_novo_id(clientes)
    
    novo_cliente = {
        "id": novo_id,
        "nome": nome,
        "idade": idade,
        "ativo": True 
    }

    clientes.append(novo_cliente)
    salvar_clientes(clientes)

    print("Cliente cadastrado com sucesso!")