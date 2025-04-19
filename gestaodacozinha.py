from estoque import estoque, atualizar_estoque

cardapio = {}
fila_de_preparo = []

def cadastrar_cardapio_padrao():
    global cardapio

    cardapio = {
        "Pastel de Carne": {
            "descricao": "Massa crocante com carne moída e cebola",
            "preco": 12.00,
            "ingredientes": {
                "ING001": 1,       # Massa para pastel (1 pacote)
                "ING004": 0.5,     # Carne moída (kg)
                "ING003": 0.2      # Cebola (kg)
            }
        },
        "Pastel de Frango com Catupiry": {
            "descricao": "Recheado com frango desfiado e catupiry",
            "preco": 14.00,
            "ingredientes": {
                "ING001": 1,
                "ING005": 0.4,
                "ING013": 0.5
            }
        },
        "Pastel de Calabresa com Queijo": {
            "descricao": "Calabresa moída com queijo mussarela",
            "preco": 13.00,
            "ingredientes": {
                "ING001": 1,
                "ING008": 0.3,
                "ING007": 0.3
            }
        },
        "Pastel de Presunto e Queijo": {
            "descricao": "Presunto com queijo mussarela",
            "preco": 12.00,
            "ingredientes": {
                "ING001": 1,
                "ING006": 0.3,
                "ING007": 0.3
            }
        },
        "Pastel Vegetariano": {
            "descricao": "Tomate, milho, ervilha, cebola e azeitona",
            "preco": 11.00,
            "ingredientes": {
                "ING001": 1,
                "ING013": 0.3,
                "ING003": 0.2,
                "ING011": 1,
                "ING012": 1,
                "ING014": 0.2
            }
        }
    }

def preparar_prato(nome_prato):
    if nome_prato not in cardapio:
        print("❌ Prato não encontrado no cardápio.")
        return

    ingredientes = cardapio[nome_prato]["ingredientes"]

    # Verifica disponibilidade no estoque
    for codigo, quantidade in ingredientes.items():
        if codigo not in estoque or estoque[codigo]["quantidade"] < quantidade:
            print(f"⚠️ Ingrediente insuficiente: {estoque.get(codigo, {'nome': 'Desconhecido'})['nome']}")
            return

    # Dá baixa no estoque
    for codigo, quantidade in ingredientes.items():
        estoque[codigo]["quantidade"] -= quantidade

    fila_de_preparo.append({
        "prato": nome_prato,
        "status": "Recebido"
    })

    print(f"✅ Prato '{nome_prato}' adicionado à fila de preparo.")

def mostrar_fila_de_preparo():
    if not fila_de_preparo:
        print("📭 Nenhum prato na fila de preparo.")
        return

    print("\n📋 Fila de Preparo:")
    for i, pedido in enumerate(fila_de_preparo, 1):
        print(f"{i}. {pedido['prato']} - Status: {pedido['status']}")

def atualizar_status_preparo(index, novo_status):
    if 0 <= index < len(fila_de_preparo):
        fila_de_preparo[index]["status"] = novo_status
        print("🔄 Status atualizado com sucesso.")
    else:
        print("❌ Pedido inválido.")