""" Calculadora usando WHILE """

while True:

    numero_01 = input('Digite um número: ')
    numero_02 = input('Digite mais um número: ')
    operador = input('Qual operação deseja efetuar? (+-/*): ')

    numeros_validos = None
    num_01_float = 0
    num_02_float = 0

    try:
        num_01_float = float(numero_01)
        num_02_float = float(numero_02)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Em um ou ambos os campos você não digitou um número, tente novamente')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta, confira o resultado abaixo: ')
    
    if operador == '+':
        print(num_01_float + num_02_float)
    elif operador == '-':
        print(num_01_float - num_02_float)
    elif operador == '*':
        print(num_01_float * num_02_float)
    elif operador == '/':
        print(num_01_float / num_02_float)
    else:
        print('O código não deveria exibir isso nunca')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')


    if sair is True:
        break
    

    