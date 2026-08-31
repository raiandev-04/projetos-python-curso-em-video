

print("=" * 25)
print("SISTEMA CAIXA".center(25))
print("=" * 25)

total_cadastrados = 0

# ===== Entrada de dados =====
nome_cliente = input("Informe seu nome: ")
produtos = []

#Produtos Cadastrados
produtos_cadastrados = int(input('Digite quantos produtos foram cadastrados: '))

#FOR

for produtocadastrado in range(produtos_cadastrados):
   
    nome_produto = input("Informe o nome do produto: ")
    preco_produto = float(input("Informe o preço do produto: R$ "))
    quantidade_produto = int(input("Informe a quantidade do produto: "))
    subtotal = preco_produto * quantidade_produto
    total_cadastrados += subtotal
    produtos.append([nome_produto, 
                     preco_produto,
                       quantidade_produto,
                         subtotal])

print(f'Esse foi o total do subtotal da compra:R${total_cadastrados} ')

# ===== Forma de pagamento =====
opcao_pagamento = int(input(
    "\nEscolha a forma de pagamento:\n"
    "1 - PIX\n"
    "2 - Dinheiro\n"
    "3 - Cartão\n"
    "Opção: "
))

# Valores iniciais
desconto = 0
forma_pagamento = ""
valor_pago = 0
troco = 0

# ===== Desconto =====
if opcao_pagamento == 1:
    desconto = total_cadastrados * 0.10
    forma_pagamento = "PIX"

elif opcao_pagamento == 2:
    desconto = total_cadastrados * 0.05
    forma_pagamento = "Dinheiro"

elif opcao_pagamento == 3:
    forma_pagamento = "Cartão"

else:
    forma_pagamento = "Opção inválida"

# ===== Valor final =====
valor_final = total_cadastrados - desconto

# ===== Valor pago e troco =====
if forma_pagamento == "Dinheiro":
    valor_pago = float(input("Informe o valor pago: R$ "))

    if valor_pago >= valor_final:
        troco = valor_pago - valor_final
    else:
        print("\nValor insuficiente para concluir a compra.")


# ===== Impressão do recibo =====



largura = 35

print("\n" + "=" * largura)
print("RECIBO".center(largura))
print("=" * largura)



print("-" * largura)
print(f'Nome do cliente: {nome_cliente}')
for produto in produtos:
    print(f"Produto: {produto[0]}")
    print(f"Preço Unitário: R$ {produto[1]:.2f}")
    print(f"Quantidade: {produto[2]}")
    print(f"Subtotal: R$ {produto[3]:.2f}")
    

print("-" * largura)


print(f"total da compra:          R$ {total_cadastrados:.2f}")
print(f"Forma Pagamento:   {forma_pagamento}")
print(f"Desconto:          R$ {desconto:.2f}")
print(f"Valor Final:       R$ {valor_final:.2f}")

if forma_pagamento == "Dinheiro":
    print(f"Valor Pago:        R$ {valor_pago:.2f}")
    print(f"Troco:             R$ {troco:.2f}")
print('-' * largura)

print("=" * largura)
print(f'Obrigado pela preferencia {nome_cliente}, volte sempre!!'.center(largura))
print("=" * largura)