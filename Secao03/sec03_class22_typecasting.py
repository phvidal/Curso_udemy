'''
Coerção de tipos de dados 

Podemos fazer a coerção dos dados em Python para que possamos fazer comparações,
somas, análises desses dados. É importante pois podemos receber de uma mesma tabela
dados que são str, int e float por exemplo, mas queremos trabalhar apenas com INT,
então para isso precisamos fazer a coerção desses dados.

Abaixo seguem exemplos de como realizar essas coerções.'''


a = 25.5
b = 30
res = a + b
print(res)
print(type(res))

# Converte FLOAT para INT
a = 25.5
b = 30
res = int(a) + b
print(res)
print(type(res))

# Converte INT para STR
x = 10
s = str(x)
print(s)

# Exemplo de erro que o Python não consegue juntar, pois são tipos diferentes
print("a" + 1)

# Concatenando Strs 
print('Paulo' + 'Vidal')

# Strs vazias e seus resultados Boolianos 
print(bool(""))
print(bool(" "))