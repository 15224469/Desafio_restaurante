def calcular_conta_mesa(mesas, cardapio):
    # def para calcular a conta total de uma mesa
    numero_mesa = int(input("Número da mesa: "))
    if numero_mesa not in mesas:
        print("Mesa não encontrada.")
        return
    total = 0
    for pedido in mesas[numero_mesa]["pedidos"]:
        total += cardapio[pedido["item"]]["preco"] * pedido["quantidade"]
    print(f"Total da conta da Mesa {numero_mesa}: R$ {total:.2f}")
    return total

def dividir_conta(total):
    # def para que os clientes consigam dividir a conta entre eles
    # 'total' é o valor total da conta
    num_clientes = int(input("Número de clientes: "))
    valor_por_cliente = total / num_clientes
    print(f"Valor por cliente: R$ {valor_por_cliente:.2f}")

def aplicar_taxa_servico(total):
    # def para aplicar 5% de taxa de serviço
    # retornando para mostrar o 'total' já com a taxa de serviço
    taxa_servico = 0.05  # 5% de taxa de serviço
    total += total * taxa_servico
    return total

def registrar_pagamento(mesas, numero_mesa, total_com_desconto):
    # def para registrar o pagamento da mesa e fechar a mesa.
    # 'numero_mesa' é o número da mesa que o cliente está pagando.
    # 'total_com_desconto' é o valor total da conta com a taxa de serviço.
    forma_pagamento = input("Forma de pagamento (dinheiro ou cartão): ")
    if forma_pagamento.lower() == "dinheiro":
        valor_pago = float(input("Valor pago: "))
        troco = valor_pago - total_com_desconto
        if troco > 0:
            print(f"Troco: R$ {troco:.2f}")
        else:
            print("Pagamento recebido.")
    else:
        print("Pagamento registrado.")
    mesas[numero_mesa]["status"] = "livre"
    mesas[numero_mesa]["pedidos"] = []
    print("Mesa fechada.")
