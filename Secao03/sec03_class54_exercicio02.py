"""
Faça um programa que pergunte a hora ao usuário e baseando-se no horário descrito, exiba a saudação 
apropriada. Exemplo: Bom dia de 0 até 11 horas, Boa tarde de 12 até 17 horas e Boa noite das 18 até 23 horas.

"""

hora = input('Digite uma hora entre (0-23) somente números inteiros: ')

try:
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Hora inválida')
except:
    print('Você não digitou um número inteiro')



