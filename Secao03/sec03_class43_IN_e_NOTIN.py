# Operadores IN e NOT IN (Está ou Não está)
''' Strings são ITERÁVEIS em Python, ou seja, podemos acessar qualquer letra 
dentro da string através do seu índice '''
# Índices:
# 0 1 2 3 4
# P a u l 0
# -5-4-3-2-1

# Pode mos acessar através de um índice positivo ou negativo.

nome = 'Paulo'
print(nome[1])
print(nome[-4])

print(10 * '-')
'''No exemplo acima, a letra "a" será exibida nos dois prints'''

nome_02 = 'Elétrico'
print('tri' in nome_02)
print('let' in nome_02)

print(10 * '-')

print('tri' not in nome_02)
print('let' not in nome_02)


