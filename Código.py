from datetime import datetime

estoque = {}
cardapio = {}
fila_pedidos = []

# Carga inicial do estoque
produtos = [
    {"codigo": "ING001", "nome": "Massa para pastel", "quantidade": 20, "unidade": "pacote (1kg)", "Valor_Unitario": 6.50, "validade": "2025-08-30"},
    {"codigo": "ING002", "nome": "Óleo de soja", "quantidade": 10, "unidade": "litro", "Valor_Unitario": 7.80, "validade": "2025-07-20"},
    {"codigo": "ING003", "nome": "Cebola", "quantidade": 3, "unidade": "kg", "Valor_Unitario": 4.00, "validade": "2025-04-26"},
    {"codigo": "ING004", "nome": "Carne moída", "quantidade": 5, "unidade": "kg", "Valor_Unitario": 28.00, "validade": "2025-04-18"},
    {"codigo": "ING005", "nome": "Frango desfiado", "quantidade": 10, "unidade": "kg", "Valor_Unitario": 22.00, "validade": "2025-04-19"},
    {"codigo": "ING006", "nome": "Presunto", "quantidade": 4, "unidade": "kg", "Valor_Unitario": 18.50, "validade": "2025-04-20"},
    {"codigo": "ING007", "nome": "Queijo mussarela", "quantidade": 6, "unidade": "kg", "Valor_Unitario": 25.00, "validade": "2025-04-22"},
    {"codigo": "ING008", "nome": "Calabresa", "quantidade": 3, "unidade": "kg", "Valor_Unitario": 21.00, "validade": "2025-04-23"},
    {"codigo": "ING009", "nome": "Bacon", "quantidade": 2, "unidade": "kg", "Valor_Unitario": 30.00, "validade": "2025-04-24"},
    {"codigo": "ING010", "nome": "Ovo de codorna", "quantidade": 80, "unidade": "unidade", "Valor_Unitario": 0.50, "validade": "2025-04-17"},
    {"codigo": "ING011", "nome": "Milho verde", "quantidade": 10, "unidade": "lata", "Valor_Unitario": 3.80, "validade": "2025-08-15"},
    {"codigo": "ING012", "nome": "Ervilha", "quantidade": 8, "unidade": "lata", "Valor_Unitario": 3.70, "validade": "2025-08-18"},
    {"codigo": "ING013", "nome": "Tomate", "quantidade": 2, "unidade": "kg", "Valor_Unitario": 6.50, "validade": "2025-04-17"},
    {"codigo": "ING014", "nome": "Azeitona", "quantidade": 5, "unidade": "vidro (500g)", "Valor_Unitario": 7.20, "validade": "2025-10-20"},
    {"codigo": "ING015", "nome": "Catupiry", "quantidade": 4, "unidade": "pote (400g)", "Valor_Unitario": 9.50, "validade": "2025-04-30"},
    {"codigo": "BEB001", "nome": "Água mineral", "quantidade": 60, "unidade": "garrafa (500ml)", "Valor_Unitario": 2.50, "validade": "2030-01-01"},
    {"codigo": "BEB002", "nome": "Coca-Cola", "quantidade": 60, "unidade": "lata (350ml)", "Valor_Unitario": 4.50, "validade": "2025-12-01"},
    {"codigo": "BEB003", "nome": "Sprite", "quantidade": 60, "unidade": "lata (350ml)", "Valor_Unitario": 4.50, "validade": "2025-11-15"},
    {"codigo": "BEB004", "nome": "Pepsi", "quantidade": 60, "unidade": "lata (350ml)", "Valor_Unitario": 4.50, "validade": "2025-12-10"},
    {"codigo": "BEB005", "nome": "Guaraná Antartica", "quantidade": 60, "unidade": "lata (350ml)", "Valor_Unitario": 4.00, "validade": "2025-11-25"}
]

for produto in produtos:
    produto['validade'] = datetime.strptime(produto['validade'], "%Y-%m-%d").date()
    estoque[produto['codigo']] = produto

# Cardápio baseado no estoque
cardapio = {
    "pastel de carne": {
        "descricao": "Pastel com recheio de carne moída e temperos.",
        "preco": 8.00,
        "ingredientes": {
            "ING001": 0.1,  # massa
            "ING004": 0.15,  # carne moída
            "ING003": 0.05  # cebola
        }
    },
    "pastel de frango com catupiry": {
        "descricao": "Pastel de frango desfiado com catupiry.",
        "preco": 9.00,
        "ingredientes": {
            "ING001": 0.1,
            "ING005": 0.15,
            "ING015": 0.05
        }
    },
    "pastel de presunto e queijo": {
        "descricao": "Presunto e queijo mussarela derretido.",
        "preco": 9.00,
        "ingredientes": {
            "ING001": 0.1,
            "ING006": 0.1,
            "ING007": 0.1
        }
    },
    "pastel de calabresa com queijo": {
        "descricao": "Calabresa fatiada e queijo mussarela.",
        "preco": 9.50,
        "ingredientes": {
            "ING001": 0.1,
            "ING008": 0.1,
            "ING007": 0.1
        }
    },
    "pastel de bacon com ovo": {
        "descricao": "Pastel recheado com bacon e ovo de codorna.",
        "preco": 10.00,
        "ingredientes": {
            "ING001": 0.1,
            "ING009": 0.05,
            "ING010": 2
        }
    },
    "pastel de frango com milho e ervilha": {
        "descricao": "Frango, milho verde e ervilha.",
        "preco": 9.50,
        "ingredientes": {
            "ING001": 0.1,
            "ING005": 0.1,
            "ING011": 0.05,
            "ING012": 0.05
        }
    },
    "pastel de carne com tomate e azeitona": {
        "descricao": "Carne moída, tomate e azeitona.",
        "preco": 9.50,
        "ingredientes": {
            "ING001": 0.1,
            "ING004": 0.1,
            "ING013": 0.05,
            "ING014": 0.05
        }
    },
    "água mineral": {
        "descricao": "Água mineral gelada 500ml.",
        "preco": 2.50,
        "ingredientes": {
            "BEB001": 1
        }
    },
    "coca-cola": {
        "descricao": "Refrigerante Coca-Cola lata 350ml.",
        "preco": 4.50,
        "ingredientes": {
            "BEB002": 1
        }
    },
    "sprite": {
        "descricao": "Refrigerante Sprite lata 350ml.",
        "preco": 4.50,
        "ingredientes": {
            "BEB003": 1
        }
    },
    "pepsi": {
        "descricao": "Refrigerante Pepsi lata 350ml.",
        "preco": 4.50,
        "ingredientes": {
            "BEB004": 1
        }
    },
    "guaraná antartica": {
        "descricao": "Refrigerante Guaraná Antartica lata 350ml.",
        "preco": 4.00,
        "ingredientes": {
            "BEB005": 1
        }
    }
}

# Cadastrar novo produto
def cadastrar_produto_estoque():
    print("\n Cadastro de Produto no Estoque")
    
    codigo = input("Código do produto: ").strip().upper()
    
    if codigo in estoque:
        print(" Já existe um produto com esse código.")
        return

    nome = input("Nome do produto: ").strip()
    
    try:
        quantidade = float(input("Quantidade: "))
        unidade = input("Unidade de medida (ex: kg, litro, unidade): ").strip()
        Valor_Unitario = float(input("Preço unitário (R$): "))
        validade = input("Data de validade (YYYY-MM-DD): ").strip()
        validade_date = datetime.strptime(validade, "%Y-%m-%d").date()

        estoque[codigo] = {
            'nome': nome,
            'quantidade': quantidade,
            'unidade': unidade,
            'Valor_Unitario': Valor_Unitario,
            'validade': validade_date
        }

        print("✅ Produto cadastrado com sucesso!")

    except ValueError:
        print("❌ Erro nos dados inseridos. Tente novamente.")

# Consultar produtos com alertas
def consultar_estoque():
    print("\n📦 ESTOQUE:")
    for codigo, produto in estoque.items():
        dias_restantes = (produto['validade'] - datetime.today().date()).days
        alerta_validade = "⚠️ Vencimento próximo" if dias_restantes < 5 else ""
        alerta_quantidade = "⚠️ Estoque baixo" if produto['quantidade'] < 5 else ""
        print(f"{codigo} - {produto['nome']} ({produto['quantidade']} {produto['unidade']}) - R${produto['Valor_Unitario']:.2f} - Venc: {produto['validade']} {alerta_validade} {alerta_quantidade}")

# Atualizar produto específico
def atualizar_estoque(codigo, campo, novo_valor):
    if codigo in estoque:
        if campo == "validade":
            if isinstance(novo_valor, str):  # Só tenta converter se for string
                novo_valor = datetime.strptime(novo_valor, "%Y-%m-%d").date()
        elif campo in ["quantidade", "preco_unitario"]:
            novo_valor = float(novo_valor)

        estoque[codigo][campo] = novo_valor
        print("✅ Produto atualizado com sucesso.")
    else:
        print("❌ Produto não encontrado no estoque.")

    atualizar_estoque(codigo, campo, novo_valor)

# Funções de Cardápio e Pedidos
def cadastrar_item_cardapio():
    print("\n📋 Cadastro de Item no Cardápio")
    nome = input("Nome do prato: ").strip().lower()
    descricao = input("Descrição: ").strip()
    preco = float(input("Preço (R$): "))
    ingredientes = {}

    while True:
        codigo = input("Código do ingrediente (ou 'fim'): ").strip().upper()
        if codigo == "FIM":
            break
        if codigo not in estoque:
            print("❌ Código inválido.")
            continue
        qtd = float(input(f"Qtd de {estoque[codigo]['nome']}: "))
        ingredientes[codigo] = qtd

    cardapio[nome] = {"descricao": descricao, "preco": preco, "ingredientes": ingredientes}
    print(f"✅ Prato '{nome}' cadastrado com sucesso!")

def consultar_cardapio():
    print("\n📜 CARDÁPIO:")
    for nome, dados in cardapio.items():
        print(f"\n🍴 {nome.upper()} - R${dados['preco']:.2f}")
        print(f"Descrição: {dados['descricao']}")
        print("Ingredientes:")
        for cod, qtd in dados['ingredientes'].items():
            print(f"  - {estoque[cod]['nome']} ({cod}): {qtd} {estoque[cod]['unidade']}")

def atualizar_item_cardapio():
    nome = input("Nome do prato: ").strip().lower()
    if nome in cardapio:
        campo = input("Campo (descricao/preco): ").strip().lower()
        if campo == "descricao":
            cardapio[nome][campo] = input("Nova descrição: ")
        elif campo == "preco":
            cardapio[nome][campo] = float(input("Novo preço: "))
        else:
            print("❌ Campo inválido.")
            return
        print("✅ Atualizado com sucesso!")
    else:
        print("❌ Prato não encontrado.")

def verificar_estoque_ingredientes(ingredientes):
    for cod, qtd in ingredientes.items():
        if estoque[cod]['quantidade'] < qtd:
            print(f"❌ Ingrediente insuficiente: {estoque[cod]['nome']} ({cod})")
            return False
    return True

def baixar_estoque_ingredientes(ingredientes):
    for cod, qtd in ingredientes.items():
        estoque[cod]['quantidade'] -= qtd

def registrar_pedido():
    item = input("Prato: ").strip().lower()
    if item in cardapio:
        ingredientes = cardapio[item]['ingredientes']
        if verificar_estoque_ingredientes(ingredientes):
            baixar_estoque_ingredientes(ingredientes)
            fila_pedidos.append({"item": item, "status": "Recebido"})
            print("✅ Pedido enviado para preparo.")
        else:
            print("❌ Ingredientes insuficientes.")
    else:
        print("❌ Prato não encontrado.")

def mostrar_fila():
    print("\n📦 FILA DE PREPARO:")
    for i, pedido in enumerate(fila_pedidos):
        print(f"{i+1}. {pedido['item']} - {pedido['status']}")

def atualizar_status():
    mostrar_fila()
    try:
        index = int(input("Número do pedido: ")) - 1
        if 0 <= index < len(fila_pedidos):
            novo_status = input("Novo status: ").strip().title()
            fila_pedidos[index]["status"] = novo_status
            print("🔄 Status atualizado.")
        else:
            print("❌ Pedido inválido.")
    except:
        print("❌ Entrada inválida.")

# Menu principal
def menu_inicial():
    print("\n==== MENU PRINCIPAL ====")
    print("1 - Gestão de Estoque")
    print("2 - Gestão da Cozinha")
    print("0 - Sair")
    return input("Escolha uma opção: ")

# Loop principal
while True:
    opcao = menu_inicial()

    if opcao == "1":
        print("\n📦 GESTÃO DE ESTOQUE")
        print("1 - Cadastrar Produto")
        print("2 - Visualizar Estoque")
        print("3 - Atualizar Produto")
        G_estoque = input("Digite a opção desejada: ")

        if G_estoque == "1":
            cadastrar_produto_estoque()
        elif G_estoque == "2":
            consultar_estoque()
        elif G_estoque == "3":
            codigo = input("Código do produto: ").strip().upper()
            campo = input("Campo (nome, quantidade, unidade, Valor_Unitario, validade): ").strip()
            novo_valor = input("Novo valor: ").strip()
            atualizar_estoque(codigo, campo, novo_valor)
        else:
            print("❌ Opção inválida.")

    elif opcao == "2":
        while True:
            print("""
=== GESTÃO DA COZINHA ===
1. Cadastrar item no cardápio
2. Consultar cardápio
3. Atualizar item do cardápio
4. Registrar novo pedido
5. Ver fila de preparo
6. Atualizar status do pedido
0. Voltar ao menu principal
""")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                cadastrar_item_cardapio()
            elif escolha == "2":
                consultar_cardapio()
            elif escolha == "3":
                atualizar_item_cardapio()
            elif escolha == "4":
                registrar_pedido()
            elif escolha == "5":
                mostrar_fila()
            elif escolha == "6":
                atualizar_status()
            elif escolha == "0":
                break
            else:
                print("❌ Opção inválida.")

    elif opcao == "0":
        print("👋 Encerrando o sistema...")
        break

    else:
        print("❌ Opção inválida.")

if opcao == "3":
            while True:
                print("\n GESTÃO DE MESAS E PEDIDOS")
                print("1 - Cadastrar Mesa")
                print("2 - Visualizar Mesa")
                print("3 - Reservar Mesa")
                print("4 - Fazer Pedido")
                print("5 - Visualizar Pedido")
                print("6 - Voltar ao MENU")

                G_pedidos = input("O que deseja: ")

                if G_pedidos == "1":
                    "cadastrar_mesa(mesas)"

                elif G_pedidos == "2":
                   "visualizar_mesas(mesas)"

                elif G_pedidos == "3":
                    atribuir_clientes_mesa(mesas)

                elif G_pedidos == "4":
                    registrar_pedido(mesas, cardapio)

                elif G_pedidos == "5":
                    visualizar_pedido(mesas)

                elif G_pedidos == "6":
                    print("🔙 Retornando ao menu principal...")
                break

elif opcao == "4":
                total = None
                total_com_desconto = None
numero_mesa = None

while True:
            print("\n GESTÃO DE PAGAMENTO")
            print("1 - Calcular Conta da Mesa")
            print("2 - Dividir Conta")
            print("3 - Aplicar Taxa de Serviço")
            print("4 - Registrar Pagamento")
            print("5 - Voltar ao MENU")

            pagamento = input("Escolha o que deseja fazer: ")

            if pagamento == "1":
                numero_mesa = int(input("Número da mesa: "))
                total = calcular_conta_mesa(mesas, cardapio, numero_mesa)

            elif pagamento == "2":
                if total is not None:
                    dividir_conta(total)
                else:
                    print("⚠️ Você precisa calcular a conta primeiro!")

            elif pagamento == "3":
                if total is not None:
                    total_com_desconto = aplicar_taxa_servico(total)
                    print(f"Total com taxa de serviço: R$ {total_com_desconto:.2f}")
                else:
                    print("⚠️ Você precisa calcular a conta primeiro!")

            elif pagamento == "4":
                if total_com_desconto is not None and numero_mesa is not None:
                    registrar_pagamento(mesas, numero_mesa, total_com_desconto)
                    total = None
                    total_com_desconto = None
                    numero_mesa = None
                else:
                    print("⚠️ Calcule a conta e aplique a taxa antes de registrar o pagamento.")

            elif opcao == "6":
                print("👋 Saindo do sistema...")
                break

      # else:
       # print(" Opção inválida. Tente novamente.")

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
