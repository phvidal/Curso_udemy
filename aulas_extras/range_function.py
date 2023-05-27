""" Podemos usar a função range() para criar uma lista de números, se usarmos o range de (1, 10)
por exemplo, nossa lista começará do item um até o nove, o número 10 não será exibido."""

for value in range(1,10):
    print(value)

""" Podemos usar a função list() junto com a função range() para criar uma lista de números de forma mais rápida.
Usando o exemplo anterior, vamos criar uma lista usando essas duas funções """

numbers = list(range(1,10))
print(numbers)

""" Há como criar listas que saltam de dois em dois, três em três, ou da forma que desejar, basta informar ao final da 
função range, a quantidade de números que deseja pular, por exemplo, para contar de dois em dois até 10, basta criar a função
dessa forma: """

numbers_02 = list(range(2,11,2))
print(numbers_02)

""" Podemos usar as duas funções para preencher uma lista vazia por exemplo, imagina que queremos 
montar uma lista com o resultado da raiz de cada número entre um e dez """

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

""" Poderíamos escrever essa função de uma forma mais simplificada """

squares_01 = []
for value in range(1,11):
    squares_01.append(value**2)
print(squares_01)

""" Há uma terceira forma de escrever o código acima que é utilizando LIST COMPREHENSIONS
não é muito comum para quem está começando a escrever códigos em Python, mas é uma forma de simplificar a leitura do
seu código e diminuir algumas linhas escritas também, veja """

squares_02 = [value**2 for value in range(1,11)]
print(squares_02)

""" Para usarmos essa sintaxe acima, começamos definindo um nome para nossa lista, depois abrimos
os colchetes e definimos a expressão, a nossa foi value**2, que eleva nossos números da lista a segunda potência,
e então escrevemos o for loop, que irá passar número por número de nossa lista executando a expressão, e 
por fim definimos o nosso range() que será a quantidade de números que nossa lista terá e então, fechamos os 
colchetes. Uma coisa importante é que não usamos os dois pontos ao final, pois todo o loop ira acontecer dentro 
dos colchetes """



""" Em Python algumas funções são específicas para trabalharmos com números, por exemplo, é muito simples
descobri o mínimo valor em uma lista, o máximo valor ou a soma dos valores dessa lista, veja abaixo """

digits = list(range(1,30,4))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

