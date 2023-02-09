"""
Interpolação básica de strings

## s >> representa strings
## d , i >> são inteiros
## f >> representa float
## x , X >> são números Hexadecimais (ABCDEF0123456789)

"""

nome = 'Paulo'
preco = 100.8759829
frase = '%s, o preço do produto é R$%f' % (nome, preco)
frase_02 = '%s, o preço do produto é R$%.2f' % (nome, preco)
print(frase)
print(frase_02)
""" print(f'{nome}, o preço do produto é {preco}') """