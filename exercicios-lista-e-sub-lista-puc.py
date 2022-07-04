# -*- coding: utf-8 -*-
"""
Escreva uma função que receba a lista de preços e o nome de um
produto e retorne uma lista onde cada elemento é uma sublista conforme o
exemplo abaixo (para o produto 'frango'):
[['MaxCompras', 15.02], ['Disco', 15.12], ['PegPag', 15.12]]

Exemplo da lista de preços:
[['MaxCompras', ['picanha',30.10],['frango',15.02],['maça red',
10.00],['maça gala', 12.50],['pera',8.00],['tomate',6.50],['cebola',6.50]],
['Disco', ['maça red',
16.00],['picanha',37.12],['tomate',3.50],['cenoura',1.50],
['pera',7.50], ['frango',15.12]],
['PegPag', ['melancia',6.00],['maça red', 6.50], ['maça gala', 7.50],
['maça nacional',
5.00],['picanha',53.12],['tomate',3.50],['cenoura',1.50],['pera',7.50],['frango',15.12]]]
"""

listaDePrecos = [
    [
        "MaxCompras",
        ["picanha", 30.10],
        ["frango", 15.02],
        ["maça red", 10.00],
        ["maça gala", 12.50],
        ["pera", 8.00],
        ["tomate", 6.50],
        ["cebola", 6.50],
    ],
    [
        "Disco",
        ["maça red", 16.00],
        ["picanha", 37.12],
        ["tomate", 3.50],
        ["cenoura", 1.50],
        ["pera", 7.50],
        ["frango", 15.12],
    ],
    [
        "PegPag",
        ["melancia", 6.00],
        ["maça red", 6.50],
        ["maça gala", 7.50],
        ["maça nacional", 5.00],
        ["picanha", 53.12],
        ["tomate", 3.50],
        ["cenoura", 1.50],
        ["pera", 7.50],
        ["frango", 15.12],
    ],
]


def valorProduto(lista, produto):
    # Criando lista vazia
    listaFinal = []

    # Iterando sob lista principal
    for _, v in enumerate(lista):
        # Iterando sob sublista
        for j in v:
            # Verificando se o item esta dentro de algum item na sublista
            if produto in j:
                # Caso exista, adicionando o item a uma nova lista
                novalista = [v[0], j[1]]
                print(v[0], j[1])
                # Adicionando a novalista a lista final
                listaFinal += [novalista]

    print(listaFinal)


valorProduto(listaDePrecos, "frango")


"""
2) Escreva uma função que receba a lista retornada pela função anterior
e imprima as informações da forma abaixo:
*** Produto: frango ***
Mercado Preço
MaxCompras R$ 15.02
Disco R$ 15.12
PegPag R$ 15.12

"""
