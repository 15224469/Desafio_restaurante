from estoque import cadastrar_produto_estoque, consultar_estoque, atualizar_estoque
from gestaodacozinha import (cadastrar_cardapio_padrao, preparar_prato, mostrar_fila_de_preparo, atualizar_status_preparo)
from gestaodacozinha import cardapio
from Gestaodepedidos import cadastrar_mesa, visualizar_mesas, atribuir_clientes_mesa, registrar_pedido, visualizar_pedido
from GestaodePagamento import calcular_conta_mesa, dividir_conta, aplicar_taxa_servico, registrar_pagamento

mesas = {}

def menu_inicial():
    print("\n MENU PRINCIPAL ")
    print("1 - Gestão de Estoque")
    print("2 - Gestão da Cozinha")
    print("3 - Gestão de Mesas e Pedidos")
    print("4 - Gestão de Pagamentos")
    print("5 - Relatórios")
    print("6 - Sair")

    return input("Escolha uma opção: ")

# Loop principal
while True:
    opcao = menu_inicial()

    if opcao == "1":
        print("\n GESTÃO DE ESTOQUE")
        print("1 - Cadastrar Produto")
        print("2 - Visualizar Estoque")
        print("3 - Atualizar Estoque")

        G_estoque = input("Digite a opção desejada: ")

        if G_estoque == "1":
            cadastrar_produto_estoque()

        elif G_estoque == "2":
            consultar_estoque()

        elif G_estoque == "3":
            codigo = input("Digite o código do produto: ").strip().upper()        
            campo = input("Qual campo deseja atualizar? (nome, quantidade, unidade, preco_unitario, validade): ").strip()
            novo_valor = input("Novo valor: ").strip()

            atualizar_estoque(codigo, campo, novo_valor)

        else:
            print("Opção inválida.")

    elif opcao == "2":
        cadastrar_cardapio_padrao()

        while True:
            print("\nGESTÃO DA COZINHA")
            print("1 - Preparar prato")
            print("2 - Mostrar fila de preparo")
            print("3 - Atualizar status")
            print("4 - Voltar")

            op = input("Escolha uma opção: ")

            if op == "1":
                prato = input("Nome do prato: ")
                preparar_prato(prato)

            elif op == "2":
                mostrar_fila_de_preparo()

            elif op == "3":
                mostrar_fila_de_preparo()
                idx = int(input("Número do prato na fila: ")) - 1
                status = input("Novo status (Recebido, Em preparo, Pronto): ")
                atualizar_status_preparo(idx, status)

            elif op == "4":
                break

    elif opcao == "3":
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
                cadastrar_mesa(mesas)

            elif G_pedidos == "2":
                visualizar_mesas(mesas)

            elif G_pedidos == "3":
                atribuir_clientes_mesa(mesas)

            elif G_pedidos == "4":
                registrar_pedido(mesas, cardapio)

            elif G_pedidos == "5":
                visualizar_pedido(mesas)

            elif G_pedidos == "6":
                print(" Retornando ao menu principal...")
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
                    print("Você precisa calcular a conta primeiro!")

            elif pagamento == "4":
                if total_com_desconto is not None and numero_mesa is not None:
                    registrar_pagamento(mesas, numero_mesa, total_com_desconto)
                    total = None
                    total_com_desconto = None
                    numero_mesa = None
                else:
                    print("⚠️ Calcule a conta e aplique a taxa antes de registrar o pagamento.")

            elif pagamento == "5":
                break

            elif opcao == "6":
                print("👋 Saindo do sistema...")
                break

            # else:
                # print(" Opção inválida. Tente novamente.")