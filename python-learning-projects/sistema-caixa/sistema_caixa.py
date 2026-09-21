

print("=" * 25)
print("SISTEMA CAIXA".center(25))
print("=" * 25)

total_cadastrados = 0

# ===== Entrada de dados =====
nome_cliente = input("Informe seu nome: ")
produtos = []

#Produtos Cadastrados
tipos_produtos = int(input('Quantos produtos diferentes serão cadastrados? '))

#Estrutura repitção for pra cada contagem de produtos

for tipos_produtos in range(tipos_produtos):
   
    nome_produto = input("Informe o nome do produto: ")
    preco_produto = float(input("Informe o preço do produto: R$ "))
    quantidade_produto = int(input("Informe a quantidade do produto: "))
    subtotal = preco_produto * quantidade_produto
    total_cadastrados += subtotal
    # Cada produto é armazenado como uma TUPLA
    produto = (
        nome_produto,
        preco_produto,
        quantidade_produto,
        subtotal
    )

    # A tupla é adicionada à lista de produtos
    produtos.append(produto)

print(f'Esse foi o total do subtotal da compra:R${total_cadastrados} ')

# ===== Forma de pagamento =====

# Valores iniciais
desconto = valor_pago = troco = 0
forma_pagamento = ""

while True:
    opcao_pagamento = int(input(
        "\nEscolha a forma de pagamento:\n"
        "1 - PIX\n"
        "2 - Dinheiro\n"
        "3 - Cartão\n"
        "Opção: "
    ))

    if opcao_pagamento == 1:
        desconto = total_cadastrados * 0.10
        forma_pagamento = "PIX"
        break

    elif opcao_pagamento == 2:
        desconto = total_cadastrados * 0.05
        forma_pagamento = "Dinheiro"
        break

    elif opcao_pagamento == 3:
        forma_pagamento = "Cartão"
        break
    else:
        print('Operação invalida.')
       
        
        
# ===== Valor final =====
valor_final = total_cadastrados - desconto

# ===== Valor pago e troco =====
if forma_pagamento == "Dinheiro":

    while valor_pago < valor_final:
        valor_pago = float(input("Informe o valor pago: R$ "))

        if valor_pago < valor_final:
            print("\nValor insuficiente para concluir a compra.")

    troco = valor_pago - valor_final

# ===== Impressão do recibo =====

largura = 35

print("\n" + "=" * largura)
print("RECIBO".center(largura))
print("=" * largura)

print(f"Cliente: {nome_cliente}")
print("-" * largura)

for numero, produto in enumerate(produtos, start=1):

    print(f"PRODUTO {numero}".center(largura))
    print(f"Nome: {produto[0]}")
    print(f"Preço Unitário: R$ {produto[1]:.2f}")
    print(f"Quantidade: {produto[2]}")
    print(f"Subtotal: R$ {produto[3]:.2f}")
    print("-" * largura)

print(f"Total da compra:   R$ {total_cadastrados:.2f}")
print(f"Forma Pagamento:   {forma_pagamento}")
print(f"Desconto:          R$ {desconto:.2f}")
print(f"Valor Pago:        R$ {valor_pago:.2f}")

if forma_pagamento == "Dinheiro":
    print(f"Valor Final:       R$ {valor_final:.2f}")
    print(f"Troco:             R$ {troco:.2f}")

print("=" * largura)
print(f"Obrigado, {nome_cliente}!".center(largura))
print("Volte sempre!".center(largura))
print("=" * largura)