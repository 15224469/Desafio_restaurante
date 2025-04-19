from datetime import datetime, timedelta

estoque = {}

# Inicializando os dados como dicionário, com validade convertida para datetime.date
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
    {"codigo": "ING013", "nome": "Catupiry", "quantidade": 4, "unidade": "pote (400g)", "Valor_Unitario": 9.50, "validade": "2025-04-30"},
    #bebidas
    {"codigo": "BEB001", "nome": "Água mineral", "quantidade": 60, "unidade": "garrafa (500ml)", "Valor_Unitario": 2.50, "validade": "2030-01-01"},
    {"codigo": "BEB002", "nome": "Coca-Cola", "quantidade": 60, "unidade": "lata (350ml)", "Valor_Unitario": 4.50, "validade": "2025-12-01"},
    {"codigo": "BEB003", "nome": "Sprite", "quantidade": 60, "unidade": "lata (350ml)", "Valor_Unitario": 4.50, "validade": "2025-11-15"},
    {"codigo": "BEB004", "nome": "Pepsi", "quantidade": 60, "unidade": "lata (350ml)", "Valor_Unitario": 4.50, "validade": "2025-12-10"},
    {"codigo": "BEB005", "nome": "Guaraná Antartica", "quantidade": 60, "unidade": "lata (350ml)", "Valor_Unitario": 4.00, "validade": "2025-11-25"}
]

for produto in produtos:
    produto['validade'] = datetime.strptime(produto['validade'], "%Y-%m-%d").date()
    estoque[produto['codigo']] = produto

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

        print(" Produto cadastrado com sucesso!")

    except ValueError:
        print(" Erro nos dados inseridos. Tente novamente.")

# Consultar produtos com alertas
def consultar_estoque():
    print("\n ESTOQUE:")
    for codigo, produto in estoque.items():
        dias_restantes = (produto['validade'] - datetime.today().date()).days
        alerta_validade = "Vencimento próximo" if dias_restantes < 5 else ""
        alerta_quantidade = " Estoque baixo" if produto['quantidade'] < 5 else ""
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
        print(" Produto atualizado com sucesso.")
    else:
        print(" Produto não encontrado no estoque.")

    atualizar_estoque(codigo, campo, novo_valor)