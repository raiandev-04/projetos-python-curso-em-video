# Sistema de Caixa em Python

Projeto desenvolvido durante meus estudos de Python com o objetivo de praticar, na prática, os principais fundamentos da linguagem.

A ideia começou como um caixa simples, com cadastro de um único produto, cálculo de subtotal e escolha da forma de pagamento. Com o avanço dos estudos, fui incrementando novas funcionalidades e aplicando novos conceitos conforme fui aprendendo.

Hoje o sistema já permite cadastrar vários produtos, armazenar os dados em lista e tuplas, remover itens antes de finalizar a compra, consultar a quantidade de produtos cadastrados, aplicar descontos, validar formas de pagamento e gerar um recibo ao final.

## Funcionalidades atuais

- Cadastro do nome do cliente
- Cadastro de vários produtos
- Cadastro de preço e quantidade de cada produto
- Cálculo automático do subtotal
- Soma automática do valor total da compra
- Armazenamento dos produtos em lista
- Armazenamento dos dados de cada produto em tupla
- Menu antes da finalização da compra
- Remoção de produtos cadastrados
- Atualização automática do valor total após remover um produto
- Consulta da quantidade de produtos cadastrados
- Escolha da forma de pagamento
- Validação de opção inválida
- Desconto conforme a forma de pagamento
- Validação de valor insuficiente em pagamentos em dinheiro
- Cálculo automático do troco
- Geração de recibo com os produtos cadastrados

## Formas de pagamento

O sistema trabalha atualmente com:

- PIX
- Dinheiro
- Cartão

As regras atuais são:

- PIX: 10% de desconto
- Dinheiro: 5% de desconto
- Cartão: sem desconto

No recibo, o sistema apresenta apenas as informações que fazem sentido para cada forma de pagamento.

Para PIX e cartão, é exibido o valor final da compra.

Para pagamentos em dinheiro, são exibidos:

- Valor final
- Valor pago
- Troco

## Menu da compra

Depois do cadastro dos produtos, o usuário pode escolher entre:

```text
1 - Finalizar compra
2 - Remover produto
3 - Ver quantidade de produtos cadastrados
```

### Remoção de produto

Ao escolher remover um produto, o sistema mostra os itens cadastrados de forma numerada.

Exemplo:

```text
1 - Maçã
2 - Banana
3 - Laranja
```

O usuário escolhe o número correspondente ao produto desejado.

A remoção é feita utilizando a posição do item na lista e, depois disso, o valor total da compra também é atualizado.

### Quantidade de produtos

O sistema também permite consultar quantos produtos diferentes ainda estão cadastrados na compra.

## Estrutura dos produtos

A lista principal é utilizada para armazenar todos os produtos:

```python
produtos = []
```

Cada produto é armazenado como uma tupla contendo:

```text
Nome
Preço unitário
Quantidade
Subtotal
```

Exemplo:

```python
("Maçã", 5.00, 2, 10.00)
```

Com vários produtos cadastrados, a estrutura fica semelhante a:

```python
[
    ("Maçã", 5.00, 2, 10.00),
    ("Banana", 3.00, 1, 3.00),
    ("Laranja", 4.00, 3, 12.00)
]
```

A lista pode receber e remover produtos durante a execução, enquanto cada tupla representa os dados de um produto cadastrado.

## Conceitos de Python praticados

Durante a evolução deste projeto foram utilizados:

- Variáveis
- `input()`
- `int()`
- `float()`
- Operadores matemáticos
- Acumuladores
- `if`
- `elif`
- `else`
- `for`
- `while`
- `while True`
- `break`
- Listas
- Tuplas
- `append()`
- `pop()`
- `len()`
- `range()`
- `enumerate()`
- Operador `in`
- Índices
- F-strings
- Formatação de valores monetários

## Uso do FOR

O `for` é utilizado no cadastro dos produtos.

O usuário informa quantos tipos diferentes deseja cadastrar e o programa repete o processo conforme essa quantidade.

Também é utilizado em outros pontos, como:

- exibição dos produtos disponíveis para remoção;
- impressão dos produtos no recibo;
- numeração dos itens com `enumerate()`.

## Uso do WHILE

O projeto possui diferentes usos de `while`.

### Menu principal da compra

O menu utiliza:

```python
while True:
```

Ele continua sendo exibido enquanto o usuário não escolher finalizar a compra.

### Forma de pagamento

Também é utilizado um `while True` para impedir que o sistema avance caso o usuário informe uma opção de pagamento inválida.

### Pagamento em dinheiro

Nesse caso, o `while` utiliza uma condição.

Enquanto o valor pago for menor que o valor final da compra, o sistema continua solicitando um novo valor.

## Evolução do projeto

O projeto foi sendo construído de forma incremental, acompanhando minha evolução nos estudos.

### Primeira versão

- Cadastro de um produto
- Cálculo de subtotal
- Forma de pagamento
- Desconto
- Troco
- Recibo simples

### Implementação do FOR

- Cadastro de vários produtos
- Repetição automática do processo de cadastro
- Soma dos subtotais
- Exibição de vários produtos no recibo

### Implementação do WHILE

- Validação da forma de pagamento
- Repetição em caso de opção inválida
- Validação de pagamento insuficiente em dinheiro

### Implementação de tuplas

- Cada produto passou a ser representado por uma tupla
- Nome, preço, quantidade e subtotal ficaram agrupados em uma única estrutura

### Evolução com listas

- Lista utilizada para armazenar os produtos
- Uso de `append()` para adicionar produtos
- Uso de `len()` para consultar a quantidade cadastrada
- Uso de `pop()` para remover produtos
- Uso de índices para selecionar itens
- Atualização do valor total após uma remoção
- Criação de um menu para manipular a compra antes da finalização

## Exemplo de fluxo

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

Digite uma opção:

1 - Finalizar compra
2 - Remover produto
3 - Ver quantidade de produtos cadastrados
```

O usuário pode revisar a compra antes de seguir para o pagamento.

Depois disso, o sistema solicita a forma de pagamento e gera o recibo final.

## Próximas melhorias

O projeto continua aberto para evoluções conforme avanço nos estudos de Python.

Algumas melhorias que pretendo explorar futuramente:

- Validar números de produtos inexistentes na remoção
- Impedir cadastro de valores negativos
- Impedir quantidades inválidas
- Tratar entradas que não sejam números
- Permitir adicionar novos produtos pelo próprio menu
- Permitir realizar uma nova venda sem reiniciar o programa
- Separar partes do sistema em funções
- Criar histórico de vendas
- Salvar dados em arquivos
- Trabalhar com tratamento de erros
- Evoluir futuramente para banco de dados
- Criar uma interface para o sistema

## Objetivo do projeto

Este projeto não foi criado com a intenção de ser um sistema comercial completo.

O objetivo principal é servir como um projeto de aprendizado, onde consigo aplicar os conceitos estudados em uma situação prática e acompanhar minha própria evolução na linguagem Python.

Em vez de criar tudo de uma vez, estou desenvolvendo o sistema aos poucos, adicionando novas funcionalidades conforme aprendo novos conteúdos.

## Status

Projeto de estudos em desenvolvimento.

Atualmente já foram aplicados conceitos de:

```text
Variáveis
→ Condicionais
→ FOR
→ WHILE
→ Tuplas
→ Listas
```

Novas funcionalidades serão adicionadas conforme o avanço nos estudos de Python.
