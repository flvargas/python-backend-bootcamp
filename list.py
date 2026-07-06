def mostrar_titulo(titulo):
    
    print(f"===== {titulo.upper()} =====\n") 

def mostrar_separador():

    print("========================")
    
def mostrar_rodape(contador):

    mostrar_separador()
    print("Fim da listagem.")
    print(f"Total de clientes: {contador}")
    mostrar_separador()

def listar_clientes(clientes):
    mostrar_titulo("clientes")

    for cliente in clientes:
        listar_cliente(cliente)

    mostrar_rodape(len(clientes))

def listar_cliente(cliente):

    print(f"Id: {cliente['id']}")
    print(f"Nome: {cliente['nome']}")
    print(f"Status: {'Ativo' if cliente['ativo'] else 'Inativo'}")

    if cliente["idade"] >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")

    print("----------------")