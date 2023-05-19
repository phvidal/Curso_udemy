"""
Faça uma iteração de string usando o WHILE colocando um asterisco entre cada letra de sua string original.
Ex:
string01 = 'Paulo'
novaString = "P*a*u*l*o*'

"""

nome = 'Mariana'
novo_nome = ''
index = 0

while index < len(nome):
    letra = nome[index]
    novo_nome += (f'*{letra}')
    index += 1
    if index == len(nome):
        novo_nome += ('*')

print(novo_nome)