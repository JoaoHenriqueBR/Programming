# Tuplas = ()
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# Tuplas são imutáveis
# lanche[1] = 'Refrigerante' --> TypeError: 'tuple' object does not support item assignment

# Imprime toda a Tupla
print(lanche)

# imprime cada item da Tupla.
for comida in lanche:
    print(f'Eu vou comer {comida}')

# Tamanho da Tupla
print(len(lanche))

# Imprimir os conteúdos da tupla com base em seu tamanho, retorna a posição de cada.
for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} na posição {cont}')

# Imprime a posição e o conteúdo da tupla, retorna em diferentes variáveis.
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

# Imprime toda a Tupla em ordem alfabética (Não altera a Tupla)
print(sorted(lanche))

# Soma de Tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

# Contagem de Elementos
print(c.count(2))

# Posição do Elemento (n, pos:)
print(c.index(2, 1))

# Tuplas podem conter vários tipos
pessoa = ('João', 19, 'M', 99.88)
print(pessoa)

# Apagar a tupla
del(pessoa)
# print(pessoa) --> NameError: name 'pessoa' is not defined
# del(pessoa[0]) --> Não é possivel apagar o conteúdo da Tupla, apenas ela como um todo.
