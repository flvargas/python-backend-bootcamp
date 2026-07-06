import json

def carregar_clientes():

    with open("clientes.json", "r", encoding="utf-8") as arquivo:

        clientes = json.load(arquivo)
    
    return clientes