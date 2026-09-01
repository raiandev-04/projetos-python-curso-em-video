# Sistema de Caixa em Python

Projeto desenvolvido com o objetivo de praticar e consolidar os fundamentos de Python aprendidos durante meus estudos.

O sistema simula um caixa simples, permitindo cadastrar diferentes produtos, calcular o valor total da compra, aplicar descontos conforme a forma de pagamento, validar entradas e gerar um recibo organizado no final da operação.

## Funcionalidades

* Cadastro do nome do cliente
* Cadastro de vários tipos de produtos
* Definição de preço e quantidade de cada produto
* Cálculo automático do subtotal de cada produto
* Cálculo do valor total da compra
* Armazenamento dos produtos em lista
* Escolha da forma de pagamento
* Validação da forma de pagamento
* Desconto de acordo com a forma de pagamento
* Validação de valor insuficiente para pagamentos em dinheiro
* Cálculo automático do troco
* Geração de recibo
* Numeração dos produtos cadastrados no recibo

## Formas de pagamento

O sistema atualmente trabalha com três formas de pagamento:

* PIX
* Dinheiro
* Cartão

As regras de desconto são aplicadas sobre o valor total da compra.

## Conceitos de Python praticados

Durante o desenvolvimento deste projeto foram utilizados:

* Variáveis
* `input()`
* Conversão de tipos com `int()` e `float()`
* Operadores matemáticos
* Estruturas condicionais `if`, `elif` e `else`
* Estrutura de repetição `for`
* Estrutura de repetição `while`
* `while True`
* Uso de `break`
* Listas
* Método `append()`
* Função `range()`
* Função `enumerate()`
* F-strings
* Formatação de valores monetários
* Acumuladores
* Validação de dados

## Uso do FOR

O `for` é utilizado principalmente no cadastro dos produtos.

O usuário informa quantos tipos diferentes de produtos deseja cadastrar e o sistema repete o processo de cadastro de acordo com essa quantidade.

Também é utilizado na impressão do recibo para percorrer a lista de produtos cadastrados.

## Uso do WHILE

O projeto utiliza `while` em situações onde não é possível determinar antecipadamente quantas repetições serão necessárias.

### Validação da forma de pagamento

O sistema continua solicitando uma opção enquanto o usuário não escolher uma forma de pagamento válida.

### Validação do pagamento em dinheiro

Quando a opção escolhida é dinheiro, o sistema continua solicitando o valor pago enquanto ele for menor que o valor final da compra.

## Estrutura dos produtos

Cada produto cadastrado possui:

* Nome
* Preço unitário
* Quantidade
* Subtotal

Essas informações são armazenadas em uma lista para posteriormente serem utilizadas na geração do recibo.

## Exemplo de funcionamento

```text
=========================
      SISTEMA CAIXA
=========================

Informe seu nome: Raian

Quantos produtos diferentes serão cadastrados? 3

Informe o nome do produto: Maçã
Informe o preço do produto: R$ 5
Informe a quantidade do produto: 2

Informe o nome do produto: Banana
Informe o preço do produto: R$ 4
Informe a quantidade do produto: 1

Informe o nome do produto: Laranja
Informe o preço do produto: R$ 3
Informe a quantidade do produto: 3
```

Ao final, o sistema apresenta um recibo com os produtos, subtotais, total da compra, desconto, forma de pagamento e valor final.

## Evolução do projeto

O projeto foi desenvolvido de forma incremental durante meus estudos de Python.

### Versão inicial

* Cadastro de um único produto
* Cálculo de subtotal
* Escolha da forma de pagamento
* Cálculo de desconto
* Cálculo de troco
* Impressão de recibo

### Implementação do FOR

Posteriormente, o sistema passou a permitir:

* Cadastro de vários produtos
* Uso de listas
* Armazenamento dos produtos cadastrados
* Soma automática dos subtotais
* Impressão de vários produtos no recibo
* Uso de `enumerate()` para organizar a exibição dos produtos

### Implementação do WHILE

Na evolução seguinte foram adicionadas:

* Validação da forma de pagamento
* Repetição automática em caso de opção inválida
* Validação do valor pago em dinheiro
* Repetição enquanto o valor informado for insuficiente

## Próximas melhorias

Algumas melhorias que poderão ser implementadas futuramente:

* Validar preços negativos
* Validar quantidades inválidas
* Permitir cadastrar produtos até o usuário decidir encerrar
* Permitir realizar uma nova venda sem reiniciar o programa
* Separar o código em funções
* Criar histórico de vendas
* Salvar dados em arquivos
* Implementar tratamento de erros
* Evoluir futuramente para banco de dados
* Criar uma interface para o sistema

## Objetivo do projeto

Este projeto foi desenvolvido principalmente como exercício de consolidação dos fundamentos de Python.

A intenção é aplicar os conceitos estudados em um problema próximo de uma situação real, evoluindo o sistema gradualmente conforme novos conhecimentos forem adquiridos.

## Status

Fundamentos do projeto concluídos.

O projeto continua aberto para melhorias conforme avanço nos estudos de Python.
