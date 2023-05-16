"""
Faça um programa que peça ao usuário para digitar um número inteiro, 
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
"""

numero_usuario = input('Digite um número inteiro: ')


try:
    numero_usuario = int(numero_usuario)
    if numero_usuario % 2 == 0:
        print(f'O número digitado foi {numero_usuario}, e esse número é PAR')
    else:
        print(f'O número digitado foi {numero_usuario}, e esse número é IMPAR')
except:
    print('Você não digitou um número inteiro!!!')


