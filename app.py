from menu import mostrar_menu
from list import listar_clientes
from load import carregar_clientes
from create import cadastrar_cliente

clientes = carregar_clientes()

opcao = ""

while opcao != "3":

    mostrar_menu()

    opcao = input("Escolha: ")

    if opcao == "1":

        listar_clientes(clientes)

    elif opcao == "2":

        cadastrar_cliente(clientes)

    elif opcao == "3":

        print("Até logo!")

    else:

        print("Opção inválida.")

    print("\n")