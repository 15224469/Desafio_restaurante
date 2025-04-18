import datetime

# Estoque
estoque = {}
produtos_estoque = {}

# Cardápio
cardapio = {}

# Fila de Pedidos
fila_pedidos = []

# Mesas
mesas = {}

# Funções de Estoque
def cadastrar_produto():
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    unidade = input("Unidade de medida: ")
    preco_unitario = float(input("Preço unitário: "))
    validade = input("Data de validade (dd/mm/yyyy): ")
    validade = datetime.datetime.strptime(validade, "%d/%m/%Y")
    
    estoque[codigo] = {
        "nome": nome,
        "quantidade": quantidade,
        "unidade": unidade,
        "preco_unitario": preco_unitario,
        "validade": validade
    }
    print(f"Produto '{nome}' cadastrado com sucesso!")

def consultar_estoque():
    print("\n📦 Estoque:")
    for codigo, produto in estoque.items():
        print(f"Código: {codigo} - {produto['nome']}, Quantidade: {produto['quantidade']} {produto['unidade']}, Preço: R${produto['preco_unitario']:.2f}, Validade: {produto['validade'].strftime('%d/%m/%Y')}")
    
def atualizar_estoque():
    codigo = input("Código do produto para atualizar: ")
    if codigo in estoque:
        quantidade = int(input("Nova quantidade: "))
        estoque[codigo]['quantidade'] = quantidade
        print(f"Produto '{estoque[codigo]['nome']}' atualizado com sucesso!")
    else:
        print("Produto não encontrado no estoque.")

def verificar_estoque_baixo():
    for codigo, produto in estoque.items():
        if produto['quantidade'] < 10:
            print(f"⚠️ Estoque baixo: {produto['nome']} - Quantidade: {produto['quantidade']}")

# Funções de Cardápio
def cadastrar_item_cardapio():
    nome = input("Nome do item: ")
    descricao = input("Descrição do item: ")
    preco = float(input("Preço do item: "))
    ingredientes = {}
    
    while True:
        ingrediente = input("Ingrediente (ou 'sair' para finalizar): ")
        if ingrediente == 'sair':
            break
        quantidade = int(input(f"Quantidade de {ingrediente}: "))
        ingredientes[ingrediente] = quantidade
    
    cardapio[nome] = {
        "descricao": descricao,
        "preco": preco,
        "ingredientes": ingredientes
    }
    print(f"Item '{nome}' cadastrado no cardápio.")

def consultar_cardapio():
    print("\n📋 Cardápio:")
    for nome, dados in cardapio.items():
        print(f"Nome: {nome} - Preço: R${dados['preco']:.2f}")
        print(f"Descrição: {dados['descricao']}")
        print("Ingredientes:")
        for ingrediente, quantidade in dados['ingredientes'].items():
            print(f"  - {ingrediente}: {quantidade}")
    
def atualizar_item_cardapio():
    nome = input("Nome do item a ser atualizado: ")
    if nome in cardapio:
        campo = input("Qual campo deseja atualizar? (preço, descrição): ")
        novo_valor = input(f"Novo valor para {campo}: ")
        if campo == "preço":
            novo_valor = float(novo_valor)
        cardapio[nome][campo] = novo_valor
        print(f"Item '{nome}' atualizado.")
    else:
        print(f"Item '{nome}' não encontrado no cardápio.")

# Funções de Pedidos
def registrar_pedido():
    item_nome = input("Nome do item a ser pedido: ")
    if item_nome in cardapio:
        ingredientes = cardapio[item_nome]["ingredientes"]
        if verificar_estoque(ingredientes):
            baixar_estoque(ingredientes)
            pedido = {"item": item_nome, "status": "Recebido"}
            fila_pedidos.append(pedido)
            print(f"Pedido registrado: {item_nome}")
        else:
            print("Não há ingredientes suficientes.")
    else:
        print("Item não encontrado no cardápio.")

def mostrar_fila_pedidos():
    print("\n📦 Fila de Pedidos:")
    for i, pedido in enumerate(fila_pedidos):
        print(f"{i + 1}. {pedido['item']} - Status: {pedido['status']}")

def atualizar_status_pedido():
    index = int(input("Digite o número do pedido a ser atualizado: ")) - 1
    if 0 <= index < len(fila_pedidos):
        novo_status = input("Novo status (Recebido, Em preparo, Pronto para servir): ")
        fila_pedidos[index]["status"] = novo_status
        print(f"Status do pedido '{fila_pedidos[index]['item']}' atualizado para {novo_status}.")
    else:
        print("Pedido não encontrado.")

# Funções de Mesas
def cadastrar_mesa():
    numero = int(input("Número da mesa: "))
    capacidade = int(input("Capacidade da mesa: "))
    mesas[numero] = {"capacidade": capacidade, "status": "Livre"}
    print(f"Mesa {numero} cadastrada com sucesso!")

def visualizar_mesas():
    print("\n🪑 Mesas:")
    for numero, dados in mesas.items():
        print(f"Mesa {numero} - Status: {dados['status']} - Capacidade: {dados['capacidade']}")

def atribuir_cliente_a_mesa():
    numero = int(input("Número da mesa: "))
    if numero in mesas and mesas[numero]["status"] == "Livre":
        mesas[numero]["status"] = "Ocupada"
        print(f"Mesa {numero} agora está ocupada.")
    else:
        print("Mesa não disponível ou já ocupada.")

# Funções de Pagamento
def calcular_conta():
    mesa = int(input("Número da mesa: "))
    total = 0
    if mesa in mesas:
        for pedido in fila_pedidos:
            total += cardapio[pedido["item"]]["preco"]
        print(f"Total da mesa {mesa}: R${total:.2f}")
    else:
        print("Mesa não encontrada.")

def registrar_pagamento():
    mesa = int(input("Número da mesa: "))
    if mesa in mesas:
        pagamento = float(input("Valor do pagamento: R$"))
        print(f"Pagamento de R${pagamento:.2f} registrado para a mesa {mesa}.")
        mesas[mesa]["status"] = "Livre"
        print(f"Mesa {mesa} agora está livre.")
    else:
        print("Mesa não encontrada.")

# Função principal para menu interativo
def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Gestão de Estoque")
        print("2. Gestão da Cozinha")
        print("3. Gestão de Pedidos")
        print("4. Gestão de Mesas")
        print("5. Gestão de Pagamento")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\nGestão de Estoque:")
            print("1. Cadastrar Produto")
            print("2. Consultar Estoque")
            print("3. Atualizar Estoque")
            print("4. Verificar Estoque Baixo")
            opcao_estoque = input("Escolha uma opção: ")
            if opcao_estoque == '1':
                cadastrar_produto()
            elif opcao_estoque == '2':
                consultar_estoque()
            elif opcao_estoque == '3':
                atualizar_estoque()
            elif opcao_estoque == '4':
                verificar_estoque_baixo()
        
        elif opcao == '2':
            print("\nGestão da Cozinha:")
            print("1. Cadastrar Item no Cardápio")
            print("2. Consultar Cardápio")
            print("3. Atualizar Item do Cardápio")
            opcao_cozinha = input("Escolha uma opção: ")
            if opcao_cozinha == '1':
                cadastrar_item_cardapio()
            elif opcao_cozinha == '2':
                consultar_cardapio()
            elif opcao_cozinha == '3':
                atualizar_item_cardapio()

        elif opcao == '3':
            print("\nGestão de Pedidos:")
            print("1. Registrar Pedido")
            print("2. Mostrar Fila de Pedidos")
            print("3. Atualizar Status de Pedido")
            opcao_pedidos = input("Escolha uma opção: ")
            if opcao_pedidos == '1':
                registrar_pedido()
            elif opcao_pedidos == '2':
                mostrar_fila_pedidos()
            elif opcao_pedidos == '3':
                atualizar_status_pedido()

        elif opcao == '4':
            print("\nGestão de Mesas:")
            print("1. Cadastrar Mesa")
            print("2. Visualizar Mesas")
            print("3. Atribuir Cliente a Mesa")
            opcao_mesas = input("Escolha uma opção: ")
            if opcao_mesas == '1':
                cadastrar_mesa()
            elif opcao_mesas == '2':
                visualizar_mesas()
            elif opcao_mesas == '3':
                atribuir_cliente_a_mesa()

        elif opcao == '5':
            print("\nGestão de Pagamento:")
            print("1. Calcular Conta")
            print("2. Registrar Pagamento")
            opcao_pagamento = input("Escolha uma opção: ")
            if opcao_pagamento == '1':
                calcular_conta()
            elif opcao_pagamento == '2':
                registrar_pagamento()

        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Rodar o menu interativo
if __name__ == "__main__":
    menu()
