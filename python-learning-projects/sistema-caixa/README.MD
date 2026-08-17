# Sistema de Caixa em Python

Projeto desenvolvido em Python com objetivo de praticar lógica de programação e simular o funcionamento básico de um sistema de caixa.

O sistema permite cadastrar vários produtos em uma única compra, calcular o valor total, aplicar descontos de acordo com a forma de pagamento e gerar um recibo no final.

## Funcionalidades

* Cadastro do nome do cliente
* Cadastro de vários produtos
* Registro de:

  * nome do produto
  * preço unitário
  * quantidade
* Cálculo automático do subtotal de cada produto
* Soma do valor total da compra
* Formas de pagamento:

  * PIX
  * Dinheiro
  * Cartão
* Desconto de:

  * 10% no PIX
  * 5% no dinheiro
* Cálculo de troco
* Emissão de recibo com todos os produtos cadastrados

## Conceitos utilizados

Durante o desenvolvimento foram utilizados conceitos como:

* Variáveis
* Entrada e saída de dados
* `if`, `elif` e `else`
* Operadores matemáticos
* Listas
* Método `append()`
* Estrutura de repetição `for`
* `range()`
* Acumuladores
* Formatação de strings com `f-string`

## Uso do `for`

Uma das principais evoluções do projeto foi permitir o cadastro de vários produtos.

O primeiro `for` é responsável por repetir o cadastro de acordo com a quantidade de produtos informada pelo usuário.

Durante cada repetição, os dados são armazenados em uma lista.

Depois, um segundo `for` percorre essa lista para exibir todos os produtos no recibo.

## Exemplo de funcionamento

```text
SISTEMA CAIXA

Informe seu nome: Raian
Digite quantos produtos foram cadastrados: 2

Informe o nome do produto: Arroz
Informe o preço do produto: R$ 10
Informe a quantidade do produto: 2

Informe o nome do produto: Feijão
Informe o preço do produto: R$ 8
Informe a quantidade do produto: 3
```

Resultado:

```text
Produto: Arroz
Preço Unitário: R$ 10.00
Quantidade: 2
Subtotal: R$ 20.00

Produto: Feijão
Preço Unitário: R$ 8.00
Quantidade: 3
Subtotal: R$ 24.00

Total da compra: R$ 44.00
```

## Como executar

Tenha o Python instalado no computador.

Clone o repositório:

```bash
git clone https://github.com/raiandev-04/projetos-python-curso-em-video.git
```

Entre na pasta do projeto:

```bash
cd projetos-python-curso-em-video/python-learning-projects/sistema-caixa
```

Execute:

```bash
python sistema_caixa.py
```

## Próximas melhorias

Algumas funcionalidades que podem ser adicionadas futuramente:

* Validar opções de pagamento inválidas
* Impedir valores negativos
* Melhorar a validação do valor recebido em dinheiro
* Permitir adicionar produtos até o usuário escolher encerrar
* Utilizar dicionários para organizar melhor os dados dos produtos
* Separar partes do sistema em funções
* Salvar vendas em arquivo
* Criar histórico de vendas

## Objetivo do projeto

Este projeto faz parte dos meus estudos em Python e está sendo atualizado conforme avanço nos conteúdos de lógica de programação.

A proposta é melhorar gradualmente o código, aplicando novos conceitos em um projeto já existente em vez de apenas criar exercícios isolados.

---

Desenvolvido como projeto de aprendizado em Python.
