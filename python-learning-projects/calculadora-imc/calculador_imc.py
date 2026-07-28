print("=" * 25)
print("Calculadora IMC".center(25))
print("=" * 25)


#CALCULADORA IMC

#DECLARAÇÃO DE VARIAVEIS

nome = str(input('NOME: '))
peso = float(input('PESO: '))
altura = float(input('ALTURA: '))

#2 Calculo IMC
calculo_imc = peso /(altura ** 2)
# 3. Exibição do resultado formatado com 2 casas decimais


#Abaixo de 18,5: Baixo pesoEntre 18,5
# Abaixo de 18,5: ABAIXO DO PESO
if calculo_imc < 18.5:
    classificacao = 'ABAIXO DO  PESO'

# Entre 18,5 e 24,9: PESO NORMAL
elif calculo_imc < 25.0:
    classificacao = 'PESO NORMAL'
# Entre 25,0 e 29,9: SOBREPESO
elif calculo_imc < 30.0:
    classificacao = 'SOBREPESO'

# Entre 30,0 e 34,9: OBESIDADE GRAU I
elif calculo_imc < 35.0:
    classificacao = 'OBESIDADE GRAU I'

# Entre 35,0 e 39,9: OBESIDADE GRAU II
elif calculo_imc < 40.0:
   classificacao = 'OBESIDADE GRAU II'

# Maior ou igual a 40,0: OBESIDADE GRAU III
else:
    classificacao = 'OBESIDADE GRAU III'

print(f'Classificação:{classificacao}')

largura = 35

print('\n' + '=' * largura)
print('Descrição'.center(largura))
print('=' * largura)
print(f"Nome: {nome}")
print(f"Peso: {peso:.1f} kg")
print(f"Altura: {altura}m")
print(f"\nSeu IMC é: {calculo_imc:.2f}")
print("-" * largura)