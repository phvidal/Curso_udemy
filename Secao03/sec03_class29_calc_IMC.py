# Usando os operadores e suas precedências para calcular o IMC

nome = "Vidal"
altura = 1.85
peso = 102
imc = peso / (altura * altura)

print(round(imc,3))
print((f'O valor do IMC de {nome} é {imc:.2f}'))

# Veja que usamos o ROUND para definir a quantidade de casas decimais mostradas
