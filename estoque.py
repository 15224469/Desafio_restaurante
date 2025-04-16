#def menu_inicial ():
#   print("1 - Gestão de Estoque")
#   print("2 - Gestão da Cozinha")
#   print("3 - Gestão de Mesas e Pedidos")
#   print("4 - Gestão de Pagamentos")
#   print("5 - Relatórios")
#   print("6 - Sair")

#   menu = input("Digite o número que corresponde ao que você deseja: ")
#   return menu

from datetime import datetime, timedelta

estoque = [
    {"codigo": "ING001", "nome": "Massa para pastel", "quantidade": 20, "unidade": "pacote (1kg)", "preco_unitario": 6.50, "validade": "2025-08-30"},
    {"codigo": "ING002", "nome": "Óleo de soja", "quantidade": 10, "unidade": "litro", "preco_unitario": 7.80, "validade": "2025-07-20"},
    {"codigo": "ING003", "nome": "Sal", "quantidade": 5, "unidade": "kg", "preco_unitario": 3.00, "validade": "2026-09-15"},
    {"codigo": "ING004", "nome": "Alho", "quantidade": 2, "unidade": "kg", "preco_unitario": 12.00, "validade": "2025-04-28"},
    {"codigo": "ING005", "nome": "Cebola", "quantidade": 3, "unidade": "kg", "preco_unitario": 4.00, "validade": "2025-04-26"},
    {"codigo": "ING006", "nome": "Carne moída", "quantidade": 5, "unidade": "kg", "preco_unitario": 28.00, "validade": "2025-04-18"},
    {"codigo": "ING007", "nome": "Frango desfiado", "quantidade": 10, "unidade": "kg", "preco_unitario": 22.00, "validade": "2025-04-19"},
    {"codigo": "ING008", "nome": "Presunto", "quantidade": 4, "unidade": "kg", "preco_unitario": 18.50, "validade": "2025-04-20"},
    {"codigo": "ING009", "nome": "Queijo mussarela", "quantidade": 6, "unidade": "kg", "preco_unitario": 25.00, "validade": "2025-04-22"},
    {"codigo": "ING010", "nome": "Calabresa", "quantidade": 3, "unidade": "kg", "preco_unitario": 21.00, "validade": "2025-04-23"},
    {"codigo": "ING011", "nome": "Bacon", "quantidade": 2, "unidade": "kg", "preco_unitario": 30.00, "validade": "2025-04-24"},
    {"codigo": "ING012", "nome": "Ovo de codorna", "quantidade": 80, "unidade": "unidade", "preco_unitario": 0.50, "validade": "2025-04-17"},
    {"codigo": "ING013", "nome": "Milho verde", "quantidade": 10, "unidade": "lata", "preco_unitario": 3.80, "validade": "2025-08-15"},
    {"codigo": "ING014", "nome": "Ervilha", "quantidade": 8, "unidade": "lata", "preco_unitario": 3.70, "validade": "2025-08-18"},
    {"codigo": "ING015", "nome": "Tomate", "quantidade": 2, "unidade": "kg", "preco_unitario": 6.50, "validade": "2025-04-17"},
    {"codigo": "ING016", "nome": "Azeitona", "quantidade": 5, "unidade": "vidro (500g)", "preco_unitario": 7.20, "validade": "2025-10-20"},
    {"codigo": "ING018", "nome": "Catupiry", "quantidade": 4, "unidade": "pote (400g)", "preco_unitario": 9.50, "validade": "2025-04-30"},
    # Bebidas
    {"codigo": "BEB001", "nome": "Água mineral", "quantidade": 60, "unidade": "garrafa (500ml)", "preco_unitario": 2.50, "validade": "2030-01-01"},
    {"codigo": "BEB002", "nome": "Coca-Cola", "quantidade": 60, "unidade": "lata (350ml)", "preco_unitario": 4.50, "validade": "2025-12-01"},
    {"codigo": "BEB003", "nome": "Sprite", "quantidade": 60, "unidade": "lata (350ml)", "preco_unitario": 4.50, "validade": "2025-11-15"},
    {"codigo": "BEB004", "nome": "Pepsi", "quantidade": 60, "unidade": "lata (350ml)", "preco_unitario": 4.50, "validade": "2025-12-10"},
    {"codigo": "BEB005", "nome": "Guaraná Antartica", "quantidade": 60, "unidade": "lata (350ml)", "preco_unitario": 4.00, "validade": "2025-11-25"}
]

# Data atual e limite para vencimento próximo
hoje = datetime.today().date()
limite_validade = hoje + timedelta(days=7)

# Exibe apenas os produtos com estoque baixo ou próximos do vencimento
for item in estoque:
    if item["quantidade"] <= 10:
        validade = datetime.strptime(item["validade"], "%Y-%m-%d").date()
        if validade <= limite_validade:
            print(f"Produto: {item['nome']}, Estoque baixo, Validade: {item['validade']}")
        else:
            print(f"Produto: {item['nome']}, Estoque baixo")