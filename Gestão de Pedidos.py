def cadastrar_mesa(mesas):
    # Cadastrando uma nova mesa, 'mesas' é onde está armazenado as informações sobre elas
    numero = int(input("Número da mesa: "))
    capacidade = int(input("Capacidade da mesa (Até 4 pessoas): "))
    mesas[numero] = {
        "capacidade": capacidade, # Capacidade de pessoas na mesa
        "status": "livre", # Se está livre, ocupada ou reservada
        "pedidos": []
    }
    print("Mesa cadastrada com sucesso!")

def visualizar_mesas(mesas):
    # def para que consigamos ver o status da mesa, se está disponível ou não
    print("Status das mesas:")
    for numero, mesa in mesas.items():
        print(f"- Mesa {numero}: Capacidade {mesa['capacidade']}, Status: {mesa['status']}")

def atribuir_clientes_mesa(mesas):
    # def para adicionar clientes na mesa
    numero_mesa = int(input("Número da mesa: "))
    if numero_mesa not in mesas:
        print("Mesa não encontrada.")
        return
    if mesas[numero_mesa]["status"] != "livre":
        print("Mesa ocupada ou reservada.")
        return
    mesas[numero_mesa]["status"] = "ocupada"
    print("Clientes atribuídos à mesa.")

def registrar_pedido(mesas, cardapio):
    # def para registrar o pedido na mesa, o 'cardápio é onde está armazenado as comidas e bebidas
    numero_mesa = int(input("Número da mesa: "))
    if numero_mesa not in mesas:
        print("Mesa não encontrada.")
        return
    while True:
        nome_item = input("Nome do item do pedido (ou 'fim' para terminar): ")
        if nome_item.lower() == "fim":
            break
        if nome_item not in cardapio:
            print("Item não encontrado no cardápio.")
            continue
        quantidade = int(input("Quantidade: "))
        mesas[numero_mesa]["pedidos"].append({"item": nome_item, "quantidade": quantidade})
    print("Pedido registrado com sucesso!")

def visualizar_pedido(mesas):
    # def para visualizar os pedidos da mesa
    numero_mesa = int(input("Número da mesa: "))
    if numero_mesa not in mesas:
        print("Mesa não encontrada.")
        return
    print(f"Pedidos da Mesa {numero_mesa}:")
    for pedido in mesas[numero_mesa]["pedidos"]:
        print(f"- {pedido['item']}: {pedido['quantidade']}")
