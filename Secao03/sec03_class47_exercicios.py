"""
Exercício:
Peça ao usuário para digitar seu nome;
Peça ao usuário para digitar sua idade;
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome ten {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba: 'Desculpe, você deixou campos vazios.'

"""

username = input('Digite seu nome: ')
user_age = input('Digite sua idade (números apenas): ')
num_letter = len(username)


if len(username) > 0 and len(user_age) > 0:
    print(f'Seu nome é {username}')
    print(f'Seu nome invertido é: {username[::-1]}')
    print(f'A primeira letra do seu nome é {username[0]}')
    print(f'A última letra do seu nome é {username [-1]}')
    if ' ' in username:
        print('Seu nome contém espaços')
        print(f'Seu nome contém {num_letter -1} letras')
    elif ' ' not in username:
        print('Seu nome não contém espaços')
        print(f'Seu nome contém {num_letter} letras')
else: 
    print('Você esta deixando algo passar')

