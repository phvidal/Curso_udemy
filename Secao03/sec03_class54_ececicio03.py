"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras pelo menos 
escreva: "Seu nome é curto", se tiver entre 5 e 6 letras, escreva "Seu nome é normal" e se 
tiver mais que 6 letras, escreva "Seu nome é muito grande"

"""

nome_usuario = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome_usuario)

if tamanho_nome <= 4:
    print(f'Seu nome é muito curto {nome_usuario}')
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print(f'Seu nome é de tamanho padrão {nome_usuario}')
else:
    print(f'Seu nome é muito grande {nome_usuario}')

