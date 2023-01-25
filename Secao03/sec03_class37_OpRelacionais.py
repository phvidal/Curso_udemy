"""
Operadores de comparação (relacionais)
OP..........Significados..........Exemplo (True)
>...........maior.................2 > 1
>=..........maior ou igual........2 >= 2
<...........menor.................1 < 2
<=..........menor ou igual........2 <= 2
==..........igual.................'a' == 'a'
!=..........diferente.............'a' != 'b'

"""

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'

print('Maior', type(maior), maior)
print('Maior ou Igual',type(maior_ou_igual),maior_ou_igual)
print('Menor', type(menor), menor)
print('Menor ou Igual', type(menor_ou_igual), menor_ou_igual)
print('Igual', type(igual), igual)
print('Diferente', type(diferente), diferente)
