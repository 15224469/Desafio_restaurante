import estoque

cardapio = {}
fila_pedidos = []

def cadastrar_item(nome, descricao, preco, ingredientes):
    cardapio[nome] = {
        "descricao": descricao,
        "preco": preco,
        "ingredientes": ingredientes
    }
    print(f"Item '{nome}' cadastrado no cardápio.")

def consultar_cardapio():
    print("\n📋 CARDÁPIO:")
    for nome, dados in cardapio.items():
        print(f"\n🍴 {nome.upper()} - R${dados['preco']:.2f}")
        print(f"Descrição: {dados['descricao']}")
        print("Ingredientes:")
        for ingrediente, quantidade in dados['ingredientes'].items():
            print(f"  - {ingrediente}: {quantidade}")
    print("")

def atualizar_item(nome, campo, novo_valor):
    if nome in cardapio:
        cardapio[nome][campo] = novo_valor
        print(f"Item '{nome}' atualizado.")
    else:
        print(f"Item '{nome}' não encontrado.")

def verificar_estoque(ingredientes_necessarios):
    for ing, qtd in ingredientes_necessarios.items():
        if estoque.get(ing, 0) < qtd:
            print(f"❌ Ingrediente insuficiente: {ing}")
            return False
    return True

def baixar_estoque(ingredientes_necessarios):
    for ing, qtd in ingredientes_necessarios.items():
        estoque[ing] -= qtd

def registrar_pedido(item_nome):
    if item_nome in cardapio:
        ingredientes = cardapio[item_nome]["ingredientes"]
        if verificar_estoque(ingredientes):
            baixar_estoque(ingredientes)
            pedido = {"item": item_nome, "status": "Recebido"}
            fila_pedidos.append(pedido)
            print(f"✅ Pedido registrado: {item_nome}")
        else:
            print("❌ Não foi possível preparar o pedido por falta de ingredientes.")
    elif item_nome in bebidas:
        if bebidas[item_nome] > 0:
            bebidas[item_nome] -= 1
            print(f"🥤 Bebida vendida: {item_nome}")
        else:
            print("❌ Bebida fora de estoque.")
    else:
        print("❌ Item não encontrado no cardápio ou bebidas.")

def mostrar_fila():
    print("\n📦 FILA DE PREPARO:")
    for i, pedido in enumerate(fila_pedidos):
        print(f"{i+1}. {pedido['item']} - {pedido['status']}")
    print("")

def atualizar_status_pedido(index, novo_status):
    if 0 <= index < len(fila_pedidos):
        fila_pedidos[index]["status"] = novo_status
        print(f"🔄 Pedido atualizado: {fila_pedidos[index]['item']} - {novo_status}")
    else:
        print("❌ Pedido não encontrado.")

if __name__ == "__main__":
    cadastrar_item(
        "pastel de carne",
        "Recheado com carne moída e temperos",
        8.00,
        {
            "massa para pastel": 1,
            "carne moída": 100,
            "cebola": 1,
            "sal": 2,
            "óleo de soja": 300
        }
    )

    cadastrar_item(
        "pastel de frango com catupiry",
        "Frango desfiado com catupiry cremoso",
        9.00,
        {
            "massa para pastel": 1,
            "frango desfiado": 100,
            "catupiry": 50,
            "sal": 2,
            "óleo de soja": 300
        }
    )

    consultar_cardapio()

    registrar_pedido("pastel de carne")
    registrar_pedido("coca-cola")
    registrar_pedido("pastel de frango com catupiry")

    mostrar_fila()

    atualizar_status_pedido(0, "Em preparo")
    atualizar_status_pedido(0, "Pronto para servir")

    mostrar_fila() estoque == {
    "massa para pastel": 100,
    "óleo de soja": 5000,  
    "sal": 500,  
    "alho": 50,
    "cebola": 30,
    "carne moída": 3000, 
    "frango desfiado": 3000,
    "presunto": 2000,
    "queijo mussarela": 2000,
    "calabresa": 2000,
    "bacon": 2000,
    "ovo de codorna": 100,
    "milho verde": 1000,
    "ervilha": 1000,
    "tomate": 50,
    "azeitona": 200,
    "catupiry": 1000
}

bebidas = {
    "água mineral": 20,
    "coca-cola": 20,
    "sprite": 20,
    "pepsi": 20,
    "guaraná antartica": 20
}

cardapio = {}

fila_pedidos = []

def cadastrar_item(nome, descricao, preco, ingredientes):
    cardapio[nome] = {
        "descricao": descricao,
        "preco": preco,
        "ingredientes": ingredientes
    }
    print(f"Item '{nome}' cadastrado no cardápio.")

def consultar_cardapio():
    print("\n📋 CARDÁPIO:")
    for nome, dados in cardapio.items():
        print(f"\n🍴 {nome.upper()} - R${dados['preco']:.2f}")
        print(f"Descrição: {dados['descricao']}")
        print("Ingredientes:")
        for ingrediente, quantidade in dados['ingredientes'].items():
            print(f"  - {ingrediente}: {quantidade}")
    print("")

def atualizar_item(nome, campo, novo_valor):
    if nome in cardapio:
        cardapio[nome][campo] = novo_valor
        print(f"Item '{nome}' atualizado.")
    else:
        print(f"Item '{nome}' não encontrado.")

def verificar_estoque(ingredientes_necessarios):
    for ing, qtd in ingredientes_necessarios.items():
        if estoque.get(ing, 0) < qtd:
            print(f"❌ Ingrediente insuficiente: {ing}")
            return False
    return True

def baixar_estoque(ingredientes_necessarios):
    for ing, qtd in ingredientes_necessarios.items():
        estoque[ing] -= qtd

def registrar_pedido(item_nome):
    if item_nome in cardapio:
        ingredientes = cardapio[item_nome]["ingredientes"]
        if verificar_estoque(ingredientes):
            baixar_estoque(ingredientes)
            pedido = {"item": item_nome, "status": "Recebido"}
            fila_pedidos.append(pedido)
            print(f"✅ Pedido registrado: {item_nome}")
        else:
            print("❌ Não foi possível preparar o pedido por falta de ingredientes.")
    elif item_nome in bebidas:
        if bebidas[item_nome] > 0:
            bebidas[item_nome] -= 1
            print(f"🥤 Bebida vendida: {item_nome}")
        else:
            print("❌ Bebida fora de estoque.")
    else:
        print("❌ Item não encontrado no cardápio ou bebidas.")

def mostrar_fila():
    print("\n📦 FILA DE PREPARO:")
    for i, pedido in enumerate(fila_pedidos):
        print(f"{i+1}. {pedido['item']} - {pedido['status']}")
    print("")

def atualizar_status_pedido(index, novo_status):
    if 0 <= index < len(fila_pedidos):
        fila_pedidos[index]["status"] = novo_status
        print(f"🔄 Pedido atualizado: {fila_pedidos[index]['item']} - {novo_status}")
    else:
        print("❌ Pedido não encontrado.")

if __name__ == "__main__":
    cadastrar_item(
        "pastel de carne",
        "Recheado com carne moída e temperos",
        8.00,
        {
            "massa para pastel": 1,
            "carne moída": 100,
            "cebola": 1,
            "sal": 2,
            "óleo de soja": 300
        }
    )

    cadastrar_item(
        "pastel de frango com catupiry",
        "Frango desfiado com catupiry cremoso",
        9.00,
        {
            "massa para pastel": 1,
            "frango desfiado": 100,
            "catupiry": 50,
            "sal": 2,
            "óleo de soja": 300
        }
    )

    consultar_cardapio()

    registrar_pedido("pastel de carne")
    registrar_pedido("coca-cola")
    registrar_pedido("pastel de frango com catupiry")

    mostrar_fila()

    atualizar_status_pedido(0, "Em preparo")
    atualizar_status_pedido(0, "Pronto para servir")

    mostrar_fila()