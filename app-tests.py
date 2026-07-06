def mostrar_titulo(titulo):
    
    print(f"===== {titulo.upper()} =====\n") 

def mostrar_cliente(cliente):

    print(f"Nome: {cliente['nome']}")
    print(f"Status: {'Ativo' if cliente['ativo'] else 'Inativo'}")

    if cliente["idade"] >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")

    print("----------------")

def mostrar_separador():
    print("========================")
    
def mostrar_rodape(contador):

    mostrar_separador()
    print("Fim da listagem.")
    print(f"Total de clientes: {contador}")
    mostrar_separador()

clientes = [
    {
        "id": 1,
        "nome": "Flávio",
        "idade": 40,
        "ativo": True
    },
    {
        "id": 2,
        "nome": "Maria",
        "idade": 17,
        "ativo": True
    },
    {
        "id": 3,
        "nome": "João",
        "idade": 25,
        "ativo": False
    }
]    

mostrar_titulo("clientes")

for cliente in clientes:
    mostrar_cliente(cliente)

mostrar_rodape(len(clientes))