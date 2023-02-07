# Usando os operadores lógicos 'AND' e 'OR'

entrar = input('[E] para entrar ou [S] para sair: ')
senha = input('Digite sua senha: ')
senha_autorizada = '102030'

if (entrar == 'E' or entrar == 'e') and senha == senha_autorizada:
    print('Entrada liberada')
   
else:
    print('Saindo do sistema!')

# Utilizando o Operador Lógico 'NOT'

senha = input('Digite sua senha: ')

senha_correta = '123456'

if not senha:
    print('Você não digitou a senha!')
elif senha != senha_correta:
    print('Senha incorreta!')
else:
    print('Bem vindo ao sistema!')