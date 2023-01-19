# Variáveis são uma forma de associar a um nome um valor, basicamente.
# Esse nome receberá o valor e será chamado de variável
# Podemos atribuir outra variável a uma variável nova, e essa recebera o valor da antiga.

idade = 25
print(idade)
minha_idade = idade

print(minha_idade)

# Cálculos com variáveis 

base = 5
altura = 8
area = (base * altura) / 2
print(area)


# Exemplos de usos de variáveis imprimindo os tipos de dados que vimos até o momento

nome = 'Paulo'
sobrenome = 'Vidal'
idade = 33
ano_nascimento = 1989
maior_de_idade = idade >= 18
altura_metros = 1.85

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?:', maior_de_idade)
print('Altura em metros:', altura_metros)

# Existem regras para criação de variáveis, por convenção elas sempre começam com a letra minúscula
# Podem conter caracteres alfanuméricos (a até z), (A até Z) e (0 até 9).
# Podem conter alguns caracteres especiais, como o underline.
#mas não podem conter algumas palavras, são elas:

""" and, as, assert, break, class, continue, def, del, elif, else, except,
exec, finally, for, from, global, if, import, in, is, lambda, not, or,
pass, print, raise, return, try, while, with, yield """