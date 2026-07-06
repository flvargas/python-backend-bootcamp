from save import salvar_clientes
from list import listar_cliente

def excluir_cliente(clientes):

    id_cliente = int(input("Informe o ID: "))

    for cliente in clientes:

        if cliente['id'] == id_cliente:
    
            print("\n")
            listar_cliente(cliente)            

            confirma = input("Confoirma exclusão? <S/N>: ").strip().upper()

            if confirma == "S":
            
                clientes.remove(cliente)
                salvar_clientes(clientes)
                print("Cliente removido.")
                return
            
            return
        
    print("Cliente não encontrado.")