# Usando a função INPUT para alimentar as variáveis.

nome = input('Qual o seu nome? ')
idade = input('Quantos anos você tem? ')
altura = input('Qual a sua altura? ')
cidade = input('Onde você mora? ')

print(f'Olá {nome} você possui {altura} metros de altura, tem {idade} anos de idade e mora na cidade de {cidade}')

# Os dados recebidos através da função INPUT são por padrão strings, por isso para efetuar uma operação aritmética 
# é preciso efetuar uma coerção desses dados antes.

valor_01 = input('Qual a sua idade? ')
valor_02 = input('Qual a idade se sua mãe? ')
resultado = int(valor_01) + int(valor_02)

print(f'A idade de sua mãe e a sua somadas é {resultado}')