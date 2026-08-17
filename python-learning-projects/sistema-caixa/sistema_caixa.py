print("=" * 25)
print("SISTEMA CAIXA".center(25))
print("=" * 25)

# ===== Entrada de dados =====
nome_cliente = input("Informe seu nome: ")
nome_produto = input("Informe o nome do produto: ")
preco_produto = float(input("Informe o preço do produto: R$ "))
quantidade_produto = int(input("Informe a quantidade do produto: "))

# ===== Cálculo do subtotal =====
subtotal = preco_produto * quantidade_produto

# ===== Forma de pagamento =====
opcao_pagamento = int(input(
    "\nEscolha a forma de pagamento:\n"
    "1 - PIX\n"
    "2 - Dinheiro\n"
    "3 - Cartão\n"
    "Opção:   "
))

# Valores iniciais
desconto = 0
forma_pagamento = ""
valor_pago = 0
troco = 0

# ===== Desconto =====
if opcao_pagamento == 1:
    desconto = subtotal * 0.10
    forma_pagamento = "PIX"

elif opcao_pagamento == 2:
    desconto = subtotal * 0.05
    forma_pagamento = "Dinheiro"

elif opcao_pagamento == 3:
    forma_pagamento = "Cartão"

else:
    forma_pagamento = "Opção inválida"

# ===== Valor final =====
valor_final = subtotal - desconto

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

print(f"Cliente: {nome_cliente}")

print("-" * largura)

print(f"Produto: {nome_produto}")
print(f"Preço Unitário: R$ {preco_produto:.2f}")
print(f"Quantidade: {quantidade_produto}")

print("-" * largura)

print(f"Subtotal:          R$ {subtotal:.2f}")
print(f"Forma Pagamento:   {forma_pagamento}")
print(f"Desconto:          R$ {desconto:.2f}")
print(f"Valor Final:       R$ {valor_final:.2f}")

if forma_pagamento == "Dinheiro":
    print(f"Valor Pago:        R$ {valor_pago:.2f}")
    print(f"Troco:             R$ {troco:.2f}")

print("=" * largura)
print("Obrigado pela preferência!".center(largura))
print("=" * largura)